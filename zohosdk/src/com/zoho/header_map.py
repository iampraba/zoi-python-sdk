try:
    from zohosdk.src.com.zoho.util.header_param_validator import HeaderParamValidator
    from zohosdk.src.com.zoho.header import Header
    from zohosdk.src.com.zoho.exception import SDKException
    from zohosdk.src.com.zoho.util.constants import Constants
    from zohosdk.src.com.zoho.util.datatype_converter import DataTypeConverter

except Exception:
    from .util import HeaderParamValidator
    from .header import Header
    from .exception import SDKException
    from .util import Constants
    from .util import DataTypeConverter

class HeaderMap(object):

    """
    This class represents the HTTP header name and value.
    """

    def __init__(self):
        """Creates an instance of HeaderMap Class"""

        self.request_headers = dict()

    def add(self, header, value):

        """
        The method to add the parameter name and value.

        Parameters:
            header (Header): A Header class instance.
            value (object): An object containing the header value.
        """

        if header is None:
            raise SDKException(Constants.HEADER_NONE_ERROR, Constants.HEADER_INSTANCE_NONE_ERROR)

        header_name = header.name

        if header_name is None:
            raise SDKException(Constants.HEADER_NAME_NONE_ERROR, Constants.HEADER_NAME_NULL_ERROR_MESSAGE)

        if value is None:
            raise SDKException(Constants.HEADER_NONE_ERROR, header_name + Constants.NONE_VALUE_ERROR_MESSAGE)

        header_class_name = header.class_name

        if header_class_name is not None:
            value = HeaderParamValidator().validate(header_name, header_class_name, value)
        else:
            try:
                value = DataTypeConverter.post_convert(value, type(value))
            except Exception as e:
                value = str(value)

        if header_name not in self.request_headers:
            self.request_headers[header_name] = str(value)

        else:
            header_value = self.request_headers[header_name]
            self.request_headers[header_name] = header_value + ',' + str(value)
