try:
    from zohosdk.src.com.zoho.util.header_param_validator import HeaderParamValidator
    from zohosdk.src.com.zoho.param import Param
    from zohosdk.src.com.zoho.exception import SDKException
    from zohosdk.src.com.zoho.util.constants import Constants
    from zohosdk.src.com.zoho.util.datatype_converter import DataTypeConverter

except Exception:
    from .util import HeaderParamValidator
    from .param import Param
    from .exception import SDKException
    from .util import Constants
    from .util import DataTypeConverter

class ParameterMap(object):

    """
    This class represents the HTTP parameter name and value.
    """

    def __init__(self):
        """Creates an instance of ParameterMap Class"""

        self.request_parameters = dict()

    def add(self, param, value):

        """
        The method to add parameter name and value.

        Parameters:
            param (Param): A Param class instance.
            value (object): An object containing the parameter value.
        """

        if param is None:
            raise SDKException(Constants.PARAMETER_NONE_ERROR, Constants.PARAM_INSTANCE_NONE_ERROR)

        param_name = param.name
        
        if param_name is None:
            raise SDKException(Constants.PARAM_NAME_NONE_ERROR, Constants.PARAM_NAME_NONE_ERROR_MESSAGE)

        if value is None:
            raise SDKException(Constants.PARAMETER_NONE_ERROR, param_name + Constants.NONE_VALUE_ERROR_MESSAGE)

        param_class_name = param.class_name

        if param_class_name is not None:
            value = HeaderParamValidator().validate(param_name, param_class_name, value)
        else:
            try:
                value = DataTypeConverter.post_convert(value, type(value))
            except Exception as e:
                value = str(value)

        if param_name not in self.request_parameters:
            self.request_parameters[param_name] = str(value)

        else:
            parameter_value = self.request_parameters[param_name]
            self.request_parameters[param_name] = parameter_value + ',' + str(value)
