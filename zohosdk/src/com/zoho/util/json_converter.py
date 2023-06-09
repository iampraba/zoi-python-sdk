try:
    import importlib
    import re
    import json
    from zohosdk.src.com.zoho.util import Converter, DataTypeConverter, Constants
    from zohosdk.src.com.zoho.exception.sdk_exception import SDKException
except Exception:
    import importlib
    import re
    from ..exception import SDKException
    from .constants import Constants
    from .datatype_converter import DataTypeConverter
    from .converter import Converter


class JSONConverter(Converter):
    """
    This class processes the API response to the object and an object to a JSON object, containing the request body.
    """

    def __init__(self, common_api_handler):

        super().__init__(common_api_handler)
        self.unique_dict = {}
        self.common_api_handler = common_api_handler

    def append_to_request(self, request_base, request_object):
        return json.dumps(request_object).encode('utf-8')

    def form_request(self, request_instance, pack, instance_number, class_member_detail):
        path_split = str(pack).rpartition(".")
        class_name = self.module_to_class(path_split[-1])
        pack = path_split[0] + "." + class_name

        try:
            from zohosdk.src.com.zoho.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        class_detail = dict(Initializer.json_details[str(pack)])

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

        return self.is_not_record_request(request_instance, class_name, class_detail,
                                          instance_number, class_member_detail)

    def is_not_record_request(self, request_instance, class_name, class_detail, instance_number, class_member_detail):
        lookup = False
        skip_mandatory = False
        class_member_name = None
        if class_member_detail is not None:
            lookup = class_member_detail[Constants.LOOKUP] if Constants.LOOKUP in class_member_detail else False
            skip_mandatory = class_member_detail[Constants.SKIP_MANDATORY] \
                if Constants.SKIP_MANDATORY in class_member_detail else False
            class_member_name = class_member_detail[Constants.NAME]

        request_json = {}
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

            field_value = None
            if modification is not None and modification != 0:
                field_value = getattr(request_instance,
                                      self.construct_private_member(class_name=class_name, member_name=member_name))

                if self.value_checker(class_name=class_name, member_name=member_name, key_details=member_detail,
                                      value=field_value, unique_values_map=self.unique_dict,
                                      instance_number=instance_number) is True:
                    if field_value is not None:
                        required_keys.pop(key_name, None)
                        primary_keys.pop(key_name, None)
                        required_in_update_keys.pop(key_name, None)

                    request_json[key_name] = self.set_data(member_detail, field_value)

        if skip_mandatory or self.check_exception(class_member_name, request_instance, instance_number,
                                                  lookup, required_keys, primary_keys, required_in_update_keys) is True:
            return request_json

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
        try:
            return self.get_response(response.json(), pack)

        except ValueError:
            return None

    def get_response(self, response, package_name):
        try:
            from zohosdk.src.com.zoho.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        if response is None or response == '' or response == "None" or response == "null":
            return None

        response_json = dict(response)
        path_split = str(package_name).rpartition(".")
        class_name = self.module_to_class(path_split[-1])
        package_name = path_split[0] + "." + class_name
        class_detail = dict(Initializer.json_details[str(package_name)])
        instance = None

        if Constants.INTERFACE in class_detail and class_detail[Constants.INTERFACE] is not None:
            classes = class_detail[Constants.CLASSES]
            instance = self.find_match(classes, response_json)
        else:
            imported_module = importlib.import_module(path_split[0])
            class_holder = getattr(imported_module, class_name)
            instance = class_holder()

            instance = self.not_record_response(instance=instance, class_name=class_name,
                                                response_json=response_json, class_detail=class_detail)

        return instance

    def not_record_response(self, instance, class_name, response_json, class_detail):
        for member_name, key_detail in class_detail.items():
            key_name = key_detail[Constants.NAME] if Constants.NAME in key_detail else None

            if key_name is not None and key_name in response_json and response_json.get(key_name) is not None:
                key_data = response_json[key_name]
                member_value = self.get_data(key_data, key_detail)
                setattr(instance, self.construct_private_member(class_name=class_name, member_name=member_name),
                        member_value)

        return instance

    def get_data(self, key_data, member_detail):
        member_value = None

        if key_data is not None:

            data_type = member_detail.get(Constants.TYPE)

            if data_type == Constants.LIST_NAMESPACE:
                member_value = self.get_collections_data(key_data, member_detail)

            elif data_type == Constants.MAP_NAMESPACE:
                member_value = self.get_map_data(key_data, member_detail)

            elif data_type == Constants.CHOICE_NAMESPACE or (
                    Constants.STRUCTURE_NAME in member_detail
                    and member_detail[Constants.STRUCTURE_NAME] == Constants.CHOICE_NAMESPACE):
                member_value = self.__get_choice_instance(key_data)

            elif Constants.STRUCTURE_NAME in member_detail:
                member_value = self.get_response(key_data, member_detail[Constants.STRUCTURE_NAME])

            else:
                member_value = DataTypeConverter.pre_convert(key_data, data_type)

        return member_value

    def get_map_data(self, response, member_detail):
        map_instance = {}

        if len(response) > 0:
            if member_detail is None or (member_detail is not None and Constants.KEYS not in member_detail):
                for key, value in response.items():
                    map_instance[key] = self.redirector_for_json_to_object(value)

            else:
                if Constants.KEYS in member_detail:
                    keys_detail = member_detail[Constants.KEYS]

                    for key_detail in keys_detail:
                        key_name = key_detail[Constants.NAME]
                        if key_name in response and response[key_name] is not None:
                            key_value = self.get_data(response[key_name], key_detail)
                            map_instance[key_name] = key_value

        return map_instance

    def get_collections_data(self, responses, member_detail):
        values = []

        if len(responses) > 0:
            if member_detail is None or (member_detail is not None and Constants.STRUCTURE_NAME not in member_detail):
                for response in responses:
                    values.append(self.redirector_for_json_to_object(response))

            else:
                pack = member_detail[Constants.STRUCTURE_NAME]
                if pack == Constants.CHOICE_NAMESPACE:
                    for response in responses:
                        values.append(self.__get_choice_instance(response))
                else:
                    for response in responses:
                        values.append(self.get_response(response, pack))

        return values

    def redirector_for_json_to_object(self, key_data):
        if isinstance(key_data, dict):
            return self.get_map_data(key_data, None)

        elif isinstance(key_data, list):
            return self.get_collections_data(key_data, None)

        else:
            return key_data

    def find_match(self, classes, response_json):
        pack = ""
        ratio = 0

        for class_name in classes:
            match_ratio = self.find_ratio(class_name, response_json)

            if match_ratio == 1.0:
                pack = class_name
                ratio = 1
                break

            elif match_ratio > ratio:
                ratio = match_ratio
                pack = class_name

        return self.get_response(response_json, pack)

    def find_ratio(self, class_name, response_json):
        try:
            from zohosdk.src.com.zoho.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        class_detail = dict(Initializer.json_details[str(class_name)])
        total_points = len(class_detail.keys())
        matches = 0

        if total_points == 0:
            return

        else:
            for member_name in class_detail:
                member_detail = class_detail[member_name]
                key_name = member_detail[Constants.NAME] if Constants.NAME in member_detail else None
                if key_name is not None and key_name in response_json and response_json.get(key_name) is not None:
                    key_data = response_json[key_name]
                    data_type = type(key_data).__name__
                    structure_name = member_detail[
                        Constants.STRUCTURE_NAME] if Constants.STRUCTURE_NAME in member_detail else None

                    if isinstance(key_data, dict):
                        data_type = Constants.MAP_NAMESPACE

                    if isinstance(key_data, list):
                        data_type = Constants.LIST_NAMESPACE

                    if data_type == member_detail[Constants.TYPE] or (
                            member_detail[Constants.TYPE] in Constants.DATA_TYPE and
                            isinstance(key_data, Constants.DATA_TYPE.get(member_detail[Constants.TYPE]))):

                        matches += 1
                    elif key_name.lower() == Constants.COUNT.lower() and \
                            member_detail[Constants.TYPE].lower() == Constants.LONG_NAMESPACE.lower():
                        matches += 1
                    elif member_detail[Constants.TYPE] == Constants.CHOICE_NAMESPACE:
                        values = list(member_detail[Constants.VALUES])
                        for value in values:
                            if value == key_data:
                                matches += 1
                                break

                    if structure_name is not None and structure_name == member_detail[Constants.TYPE]:
                        if Constants.VALUES in member_detail:
                            for value in member_detail[Constants.VALUES]:
                                if value == key_data:
                                    matches += 1
                                    break
                        else:
                            matches += 1

        return matches / total_points

    def build_name(self, key_name):
        name_split = str(key_name).split('_')
        sdk_name = name_split[0].lower()

        if len(name_split) > 1:
            for i in range(1, len(name_split)):
                if len(name_split[i]) > 0:
                    sdk_name += '_' + name_split[i].lower()

        return sdk_name

    @staticmethod
    def __get_instance_from_name(class_path):
        path_split = str(class_path).rpartition('.')
        imported_module = importlib.import_module(path_split[0])
        class_holder = getattr(imported_module, path_split[-1])

        return class_holder()

    def construct_private_member(self, class_name, member_name):
        return '_' + class_name + '__' + member_name

    def __get_choice_instance(self, data):
        choice_split = Constants.CHOICE_NAMESPACE.rpartition('.')
        imported_module = importlib.import_module(choice_split[0])
        class_holder = getattr(imported_module, choice_split[-1])
        choice_instance = class_holder(data)

        return choice_instance
