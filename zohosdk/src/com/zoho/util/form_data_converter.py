try:
    import importlib
    import logging
    import re
    import json
    from zohosdk.src.com.zoho.util import Converter, Constants, StreamWrapper, DataTypeConverter
    from zohosdk.src.com.zoho.exception.sdk_exception import SDKException

except Exception:
    import importlib
    import logging
    import re
    from .converter import Converter
    from .constants import Constants
    from .datatype_converter import DataTypeConverter
    from .stream_wrapper import StreamWrapper
    from ..exception import SDKException


class FormDataConverter(Converter):
    """
    This class to process the upload file and stream.
    """

    logger = logging.getLogger('SDKLogger')

    def __init__(self, common_api_handler):

        super().__init__(common_api_handler)
        self.unique_dict = {}
        self.common_api_handler = common_api_handler

    def append_to_request(self, request_base, request_object):
        form_data_request_body = []
        request_base.file = True
        if self.check_file_request(request_object):
            self.add_file_body(request_object, form_data_request_body)
        else:
            self.add_multi_part_body(request_object, form_data_request_body)
        return form_data_request_body

    def check_file_request(self, request_object):
        for key_name, key_value in request_object.items():
            if isinstance(key_value, list):
                for each_object in key_value:
                    if not isinstance(each_object, StreamWrapper):
                        return False
            elif not isinstance(key_value, StreamWrapper):
                return False
        return True

    def add_multi_part_body(self, request_object, request_body):
        for key_name, key_value in request_object.items():
            if isinstance(key_value, list):
                for each_object in key_value:
                    if isinstance(each_object, StreamWrapper):
                        request_body.append((key_name, each_object.get_stream()))
                    else:
                        request_body.append((key_name, (None, json.dumps(key_value))))
            elif isinstance(key_value, StreamWrapper):
                request_body.append((key_name, key_value.get_stream()))
            else:
                request_body.append((key_name, (None, json.dumps(key_value))))

    def add_file_body(self, request_object, request_body):
        for key_name, key_value in request_object.items():
            if isinstance(key_value, list):
                for each_object in key_value:
                    if isinstance(each_object, StreamWrapper):
                        request_body.append((key_name, each_object.get_stream()))
                    else:
                        request_body.append((key_name, key_value))
            elif isinstance(key_value, StreamWrapper):
                request_body.append((key_name, key_value.get_stream()))
            else:
                request_body.append((key_name, key_value))

    def form_request(self, request_instance, pack, instance_number, class_member_detail):
        path_split = str(pack).rpartition(".")
        class_name = self.module_to_class(path_split[-1])
        pack = path_split[0] + "." + class_name

        try:
            from zohosdk.src.com.zoho.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        class_detail = dict(Initializer.json_details[str(pack)])
        request = dict()

        if Constants.INTERFACE in class_detail and class_detail[Constants.INTERFACE] is not None:
            request_object_class_name = request_instance.__class__.__module__
            request_object_class_name = str(request_object_class_name)
            path_split = str(request_object_class_name).rpartition(".")
            request_class_name = self.module_to_class(path_split[-1])
            request_object_class_name = path_split[0] + "." + request_class_name
            classes = class_detail[Constants.CLASSES]

            for class_name in classes:
                class_name_interface_lower = str(class_name).lower()
                request_class_path_lower = request_object_class_name.lower()
                if class_name_interface_lower == request_class_path_lower:
                    class_detail = dict(Initializer.json_details[str(class_name)])
                    class_name = str(class_name).rpartition(".")
                    class_name = self.module_to_class(class_name[-1])
                    break
        lookup = False
        skip_mandatory = False
        class_member_name = None
        if class_member_detail is not None:
            lookup = class_member_detail[Constants.LOOKUP] if Constants.LOOKUP in class_member_detail else False
            skip_mandatory = class_member_detail[Constants.SKIP_MANDATORY] \
                if Constants.SKIP_MANDATORY in class_member_detail else False
            class_member_name = class_member_detail[Constants.NAME]

        required_keys, primary_keys, required_in_update_keys = {}, {}, {}
        for member_name, member_detail in class_detail.items():

            if ((Constants.WRITE_ONLY in member_detail and not bool(
                    member_detail[Constants.WRITE_ONLY])) and (Constants.UPDATE_ONLY in member_detail and not bool(
                    member_detail[Constants.UPDATE_ONLY])) and (Constants.READ_ONLY in member_detail and bool(
                    member_detail[Constants.READ_ONLY]))) or (Constants.NAME not in member_detail):
                continue
            key_name = member_detail[Constants.NAME]
            try:
                modification = getattr(request_instance, Constants.IS_KEY_MODIFIED)(key_name)
            except Exception as e:
                raise SDKException(code=Constants.EXCEPTION_IS_KEY_MODIFIED, cause=e)
            if Constants.REQUIRED in member_detail and member_detail[Constants.REQUIRED]:
                required_keys[key_name] = True

            if Constants.PRIMARY in member_detail and member_detail[Constants.PRIMARY] and \
                    (Constants.REQUIRED_IN_UPDATE not in member_detail or member_detail[Constants.REQUIRED_IN_UPDATE]):
                primary_keys[key_name] = True

            if Constants.REQUIRED_IN_UPDATE in member_detail and member_detail[Constants.REQUIRED_IN_UPDATE]:
                required_in_update_keys[key_name] = True

            field_value = getattr(request_instance, self.construct_private_member(class_name=class_name, member_name=member_name))

            if modification is not None and modification != 0 and field_value is not None and self.value_checker(class_name=class_name, member_name=member_name, key_details=member_detail, value=field_value, unique_values_map=self.unique_dict, instance_number=instance_number) is True:
                if field_value is not None:
                    required_keys.pop(key_name, None)
                    primary_keys.pop(key_name, None)
                    required_in_update_keys.pop(key_name, None)
                
                if field_value is not None:
                    data_type = member_detail[Constants.TYPE]

                    if data_type == Constants.LIST_NAMESPACE:
                        request[key_name] = self.set_json_array(field_value, member_detail)

                    elif data_type == Constants.MAP_NAMESPACE:
                        request[key_name] = self.set_json_object(field_value, member_detail)

                    elif data_type == Constants.CHOICE_NAMESPACE or \
                            (Constants.STRUCTURE_NAME in member_detail and
                            member_detail[Constants.STRUCTURE_NAME] == Constants.CHOICE_NAMESPACE):
                        request[key_name] = field_value.get_value()

                    elif Constants.STRUCTURE_NAME in member_detail:
                        request[key_name] = self.form_request(field_value, member_detail[Constants.STRUCTURE_NAME], None, member_detail)

                    else:
                        request[key_name] = field_value
                    
        if skip_mandatory or self.check_exception(class_member_name, request_instance, instance_number, lookup, required_keys, primary_keys, required_in_update_keys) is True:
            return request

    def check_exception(self, member_name, request_instance, instance_number,
                        lookup, required_keys, primary_keys, required_in_update_keys):
        if bool(required_in_update_keys) and self.common_api_handler is not None and self.common_api_handler.get_category_method() is not None and \
                self.common_api_handler.get_category_method().upper() == Constants.REQUEST_CATEGORY_UPDATE:
            error = {
                Constants.FIELD: member_name,
                Constants.TYPE: request_instance.__module__,
                Constants.KEYS: str(list(required_in_update_keys.keys()))
            }
            if instance_number is not None:
                error[Constants.INSTANCE_NUMBER] = instance_number

            raise SDKException(Constants.MANDATORY_VALUE_ERROR, Constants.MANDATORY_KEY_ERROR, error)

        if self.common_api_handler is not None and self.common_api_handler.get_mandatory_checker() is not None and \
                self.common_api_handler.get_mandatory_checker():
            if self.common_api_handler.get_category_method().upper() == Constants.REQUEST_CATEGORY_CREATE:
                if lookup:
                    if bool(primary_keys):
                        error = {
                            Constants.FIELD: member_name,
                            Constants.TYPE: request_instance.__module__,
                            Constants.KEYS: str(list(primary_keys.keys()))
                        }
                        if instance_number is not None:
                            error[Constants.INSTANCE_NUMBER] = instance_number

                        raise SDKException(Constants.MANDATORY_VALUE_ERROR, Constants.MANDATORY_KEY_ERROR, error)

                elif bool(required_keys):
                    error = {
                        Constants.FIELD: member_name,
                        Constants.TYPE: request_instance.__module__,
                        Constants.KEYS: str(list(required_keys.keys()))
                    }
                    if instance_number is not None:
                        error[Constants.INSTANCE_NUMBER] = instance_number

                    raise SDKException(Constants.MANDATORY_VALUE_ERROR, Constants.MANDATORY_KEY_ERROR, error)

            if self.common_api_handler.get_category_method().upper() == Constants.REQUEST_CATEGORY_UPDATE and \
                    bool(primary_keys):
                error = {
                    Constants.FIELD: member_name,
                    Constants.TYPE: request_instance.__module__,
                    Constants.KEYS: str(list(primary_keys.keys()))
                }
                if instance_number is not None:
                    error[Constants.INSTANCE_NUMBER] = instance_number

                raise SDKException(Constants.MANDATORY_VALUE_ERROR, Constants.PRIMARY_KEY_ERROR, error)

        elif lookup and self.common_api_handler is not None and self.common_api_handler.get_category_method().upper() == Constants.REQUEST_CATEGORY_UPDATE:
            if bool(primary_keys):
                error = {
                    Constants.FIELD: member_name,
                    Constants.TYPE: request_instance.__module__,
                    Constants.KEYS: str(list(primary_keys.keys()))
                }
                if instance_number is not None:
                    error[Constants.INSTANCE_NUMBER] = instance_number

                raise SDKException(Constants.MANDATORY_VALUE_ERROR, Constants.PRIMARY_KEY_ERROR, error)

        return True

    def set_data(self, member_detail, field_value):
        if field_value is not None:
            data_type = member_detail[Constants.TYPE]

            if data_type == Constants.LIST_NAMESPACE:
                return self.set_json_array(field_value, member_detail)

            elif data_type == Constants.MAP_NAMESPACE:
                return self.set_json_object(field_value, member_detail)

            elif data_type == Constants.CHOICE_NAMESPACE or \
                    (Constants.STRUCTURE_NAME in member_detail and
                     member_detail[Constants.STRUCTURE_NAME] == Constants.CHOICE_NAMESPACE):
                return field_value.get_value()

            elif Constants.STRUCTURE_NAME in member_detail:
                return self.form_request(field_value, member_detail[Constants.STRUCTURE_NAME], None, member_detail)

            else:
                return DataTypeConverter.post_convert(field_value, data_type)

        return None

    def set_json_object(self, field_value, member_detail):
        json_object = {}
        request_object = dict(field_value)

        if len(request_object) > 0:
            if member_detail is None or (member_detail is not None and Constants.KEYS not in member_detail):
                for key, value in request_object.items():
                    json_object[key] = self.redirector_for_object_to_json(value)

            else:
                if Constants.KEYS in member_detail:
                    keys_detail = member_detail[Constants.KEYS]

                    for key_detail in keys_detail:
                        key_name = key_detail[Constants.NAME]

                        if key_name in request_object and request_object[key_name] is not None:
                            key_value = self.set_data(key_detail, request_object[key_name])
                            json_object[key_name] = key_value

        return json_object

    def set_json_array(self, field_value, member_detail):
        json_array = []
        request_objects = list(field_value)

        if len(request_objects) > 0:
            if member_detail is None or (member_detail is not None and Constants.STRUCTURE_NAME not in member_detail):
                for request in request_objects:
                    json_array.append(self.redirector_for_object_to_json(request))

            else:
                pack = member_detail[Constants.STRUCTURE_NAME]

                if pack == Constants.CHOICE_NAMESPACE:
                    for request in request_objects:
                        json_array.append(request.get_value())

                else:
                    instance_count = 0
                    for request in request_objects:
                        json_array.append(self.form_request(request, pack, instance_count, member_detail))
                        instance_count += 1

        return json_array

    def redirector_for_object_to_json(self, request):
        if isinstance(request, list):
            return self.set_json_array(request, None)

        elif isinstance(request, dict):
            return self.set_json_object(request, None)

        else:
            return request

    def get_wrapped_response(self, response, pack):
        return None

    def get_response(self, response, pack):
        return None

    def construct_private_member(self, class_name, member_name):
        return '_' + class_name + '__' + member_name



