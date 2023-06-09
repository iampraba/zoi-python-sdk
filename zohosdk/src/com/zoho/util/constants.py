import datetime


class Constants(object):
    """
    This class uses the SDK constants name reference.
    """

    DATA_TYPE_ERROR = "DATA TYPE ERROR"

    ERROR = "error"

    REQUEST_METHOD_GET = "GET"

    REQUEST_METHOD_POST = "POST"

    REQUEST_METHOD_PUT = "PUT"

    REQUEST_METHOD_DELETE = "DELETE"

    GIVEN_VALUE = "given-value"

    REQUEST_METHOD_PATCH = 'PATCH'

    OAUTH_HEADER_PREFIX = "Zoho-oauthtoken "

    AUTHORIZATION = "Authorization"

    API_NAME = "api_name"

    PHOTO = "photo"

    API_VERSION = "v1.0"

    INPUT_ERROR = "INPUT_ERROR"

    LOGGER_LEVELS = {
        "CRITICAL": "CRITICAL",
        "ERROR": "ERROR",
        "WARNING": "WARNING",
        "INFO": "INFO",
        "DEBUG": "DEBUG",
        "NOTSET": "NOTSET"
    }
   
    PROXY_SETTINGS = "Proxy settings - "

    PROXY_HOST = "Host: "

    PROXY_PORT = "Port: "

    PROXY_USER = "User: "

    PROXY_DOMAIN = "Domain: "

    GET_TOKEN_BY_ID_DB_ERROR = "Exception in getTokenById - DBStore : Given ID is invalid"

    GET_TOKEN_BY_ID_FILE_ERROR = "Exception in getTokenById - FileStore : Given ID is invalid"

    MYSQL_TABLE_NAME = "oauthtoken"

    SWITCH_USER_ERROR = "SWITCH USER ERROR"

    LOGGER_INITIALIZATION_ERROR = "Exception in Logger Initialization : "

    INVALID_ID_MSG = "The given id seems to be invalid."

    API_MAX_RECORDS_MSG = "Cannot process more than 100 records at a time."

    INVALID_DATA = "INVALID_DATA"

    CODE_SUCCESS = "SUCCESS"

    STATUS_SUCCESS = "success"

    STATUS_ERROR = "error"

    GRANT_TYPE = "grant_type"

    GRANT_TYPE_AUTH_CODE = "authorization_code"

    ACCESS_TOKEN = "access_token"

    EXPIRES_IN = "expires_in"

    EXPIRES_IN_SEC = "expires_in_sec"

    REFRESH_TOKEN = "refresh_token"

    CLIENT_ID = "client_id"

    CLIENT_SECRET = "client_secret"

    REDIRECT_URI = "redirect_uri"

    REDIRECT_URL = "redirect_url"

    OBJECT = "Object"

    DATA_TYPE = {
        "String": str,
        "List": list,
        "Integer": int,
        "HashMap": dict,
        "Map": dict,
        "Long": int,
        "Double": float,
        "Float": float,
        "DateTime": datetime.datetime,
        "Date": datetime.date,
        "Boolean": bool
    }

    OBJECT_KEY = "object"

    GIVEN_LENGTH = "given-length"

    ZOHO_SDK = "X-ZOHO-SDK"

    SDK_VERSION = "1.0.0"

    CONTENT_DISPOSITION = "Content-Disposition"

    TOKEN_ERROR = "TOKEN ERROR"

    SAVE_TOKEN_ERROR = "Exception in saving tokens"

    INVALID_CLIENT_ERROR = "INVALID CLIENT ERROR"

    ERROR_KEY = 'error'

    GET_TOKEN_ERROR = "Exception in getting access token"

    MYSQL_HOST = "localhost"

    MYSQL_DATABASE_NAME = "zohooauth"

    MYSQL_USER_NAME = "root"

    MYSQL_PORT_NUMBER = "3306"

    GET_TOKEN_DB_ERROR = "Exception in getToken - DBStore"

    TOKEN_STORE = "TOKEN_STORE"

    DELETE_TOKEN_DB_ERROR = "Exception in delete_token - DBStore"

    SAVE_TOKEN_DB_ERROR = "Exception in save_token - DBStore"

    USER_MAIL = "user_mail"

    GRANT_TOKEN = "grant_token"

    EXPIRY_TIME = "expiry_time"

    GET_TOKEN_FILE_ERROR = "Exception in get_token - FileStore"

    SAVE_TOKEN_FILE_ERROR = "Exception in save_token - FileStore"

    DELETE_TOKEN_FILE_ERROR = "Exception in delete_token - FileStore"

    TYPE = "type"

    STREAM_WRAPPER_CLASS_PATH = 'zohosdk.src.com.zoho.util.StreamWrapper'

    FIELD = "field"

    NAME = "name"

    INDEX = "index"

    CLASS = "class"

    ACCEPTED_TYPE = "accepted_type"

    GIVEN_TYPE = "given_type"

    TYPE_ERROR = "TYPE ERROR"

    VALUES = "values"

    ACCEPTED_VALUES = "accepted_values"

    UNACCEPTED_VALUES_ERROR = "UNACCEPTED VALUES ERROR"

    MIN_LENGTH = "min-length"

    MINIMUM_LENGTH = "minimum-length"

    MINIMUM_LENGTH_ERROR = "MINIMUM LENGTH ERROR"

    UNIQUE = "unique"

    FIRST_INDEX = "first-index"

    NEXT_INDEX = "next-index"

    UNIQUE_KEY_ERROR = "UNIQUE KEY ERROR"

    MAX_LENGTH = "max-length"

    MAXIMUM_LENGTH = "maximum-length"

    MAXIMUM_LENGTH_ERROR = "MAXIMUM LENGTH ERROR"

    REGEX = "regex"

    INSTANCE_NUMBER = "instance-number"

    REGEX_MISMATCH_ERROR = "REGEX MISMATCH ERROR"

    READ_ONLY = "read-only"

    WRITE_ONLY = "write-only"
	
    UPDATE_ONLY = "update-only"

    IS_KEY_MODIFIED = 'is_key_modified'

    REQUIRED = "required"

    REQUIRED_IN_UPDATE = "required-in-update"

    PRIMARY = "primary"

    MANDATORY_VALUE_ERROR = "MANDATORY VALUE ERROR"

    MANDATORY_VALUE_NULL_ERROR = "MANDATORY VALUE NULL ERROR"

    MANDATORY_KEY_ERROR = "Value missing or None for mandatory key(s): "

    MANDATORY_KEY_NULL_ERROR = "Null Value for mandatory key : "

    SET_KEY_MODIFIED = "set_key_modified"

    LIST_NAMESPACE = "List"

    MAP_NAMESPACE = "Map"

    HASH_MAP = "HashMap"

    STRUCTURE_NAME = "structure_name"

    KEYS = "keys"

    INTERFACE = "interface"

    PRODUCTS = "Products"

    TAX = "TAX"

    TERRITORY = "Territory"

    PACKAGE_NAMESPACE = "zohosdk.src.com.zoho."

    CHOICE_NAMESPACE = "zohosdk.src.com.zoho.util.Choice"

    KEY_VALUES = "key_values"

    KEY_MODIFIED = "key_modified"

    COMMENTS = "Comments"

    CLASSES = "classes"

    LOGFILE_NAME = "sdk_logs.log"

    USER = "user"

    EXPECTED_TYPE = "expected-type"

    USER_AGENT = "Mozilla/5.0"

    USER_AGENT_KEY = "user-agent"

    AT = '@'

    EXPECTED_TOKEN_TYPES = 'REFRESH, GRANT'

    INITIALIZATION_ERROR = "INITIALIZATION ERROR"

    ENVIRONMENT = "environment"

    STORE = "store"

    TOKEN = "token"

    SDK_CONFIG = "sdk_config"

    USER_PROXY = "proxy"

    JSON_DETAILS_FILE_PATH = 'json_details.json'

    EMAIL = "email"

    USER_SIGNATURE_ERROR = "USERSIGNATURE ERROR"

    USER_INITIALIZATION_ERROR = "Error during User Initialization"

    EMAIL_REGEX = '^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$'

    STRING = "String"

    TOKEN_TYPE = "token_type"

    GRANT = "GRANT"

    REFRESH = "REFRESH"

    CONTENT_TYPE = 'Content-Type'

    STRING_NAMESPACE = 'String'

    BOOLEAN_NAMESPACE = 'Boolean'

    INTEGER_NAMESPACE = 'Integer'

    LONG_NAMESPACE = 'Long'

    DOUBLE_NAMESPACE = 'Float'

    DATE_NAMESPACE = 'Date'

    DATETIME_NAMESPACE = 'DateTime'

    DISCOUNT = "DISCOUNT"

    FILE_NAMESPACE = "zohosdk.src.com.zoho.util.StreamWrapper"

    LAYOUT = "Layout"

    SUBFORM = "subform"

    LOOKUP = "lookup"

    MODULEDETAILS = 'moduleDetails'

    MODULEPACKAGENAME = "modulePackageName"

    UNDERSCORE = "_"

    FIELD_DETAILS_DIRECTORY = "resources"

    NO_CONTENT_STATUS_CODE = 204

    NOT_MODIFIED_STATUS_CODE = 304

    HREF = "href"

    API_EXCEPTION = "API_EXCEPTION"

    FIELDS_LAST_MODIFIED_TIME = "FIELDS-LAST-MODIFIED-TIME"

    LINE_TAX = "$line_tax"

    CANT_DISCLOSE = " ## can't disclose ## "

    URL = "URL"

    HEADERS = "HEADERS"

    PARAMS = "PARAMS"

    INITIALIZATION_SUCCESSFUL = "Initialization successful "

    INITIALIZATION_SWITCHED = "Initialization switched "

    IN_ENVIRONMENT = " in Environment : "

    FOR_EMAIL_ID = "for Email Id : "

    REFRESH_TOKEN_MESSAGE = "Access Token has expired. Hence refreshing."

    CONTENT_TYPE_HEADER = "Content-Type"

    LIST_KEY = "List"

    ATTACHMENT_ID = "attachment_id"

    FILE_ID = "file_id"

    PHOTO_UPLOAD_ERROR_MESSAGE = "The given module is not supported in API."

    INVALID_MODULE = "INVALID_MODULE"

    MULTI_SELECT_LOOKUP = "multiselectlookup"

    MULTI_USER_LOOKUP = "multiuserlookup"

    TERRITORIES = "territories"

    GENERATED_TYPE = "generated_type"

    GENERATED_TYPE_CUSTOM = "custom"

    UPLOAD_PHOTO_UNSUPPORTED_MESSAGE = "Photo Upload Operation is not supported by the module: "

    SDK_MODULE_METADATA = "SDK-MODULE-METADATA"

    INVALID_MODULE_API_NAME_ERROR = "INVALID MODULE API NAME ERROR"

    PROVIDE_VALID_MODULE_API_NAME = "PROVIDE VALID MODULE API NAME: "

    UPLOAD_PHOTO_UNSUPPORTED_ERROR = "UPLOAD PHOTO UNSUPPORTED MODULE"

    DELETE_FIELD_FILE_ERROR = "Exception in deleting Current User Fields file : "

    DELETE_FIELD_FILES_ERROR = "Exception in deleting all Fields files : "

    DELETE_MODULE_FROM_FIELDFILE_ERROR = "Exception in deleting module from Fields file : "

    FILE_BODY_WRAPPER = 'FileBodyWrapper'

    EXCEPTION_IS_KEY_MODIFIED = "Exception in calling is_key_modified : "

    EXCEPTION_SET_KEY_MODIFIED = "Exception in calling set_key_modified : "

    SET_API_URL_EXCEPTION = "Exception in setting API URL : "

    AUTHENTICATION_EXCEPTION = "Exception in authenticating current request : "

    FORM_REQUEST_EXCEPTION = "Exception in forming request body : "

    API_CALL_EXCEPTION = "Exception in current API call execution : "

    HTTP = "http"

    HTTPS = "https"

    CONTENT_API_URL = "content.zohoapis.com"

    EXCEPTION = "Exception"

    MODULE = "module"

    REQUEST_CATEGORY_READ = "READ"

    REQUEST_CATEGORY_CREATE = "CREATE"

    REQUEST_CATEGORY_UPDATE = "UPDATE"

    ID = "id"

    CODE = "code"

    STATUS = "status"

    MESSAGE = "message"

    INVALID_URL_ERROR = "Invalid URL Error"

    REQUEST_CATEGORY_ACTION = "ACTION"

    SKIP_MANDATORY = "skip-mandatory"

    FORMULA = "formula"

    PICKLIST = "picklist"

    ACCOUNTS = "accounts"

    PRIMARY_KEY_ERROR = "Value missing or None for required key(s) : "

    REFRESH_SINGLE_MODULE_FIELDS_ERROR = "Exception in refreshing fields of module : "

    REFRESH_ALL_MODULE_FIELDS_ERROR = "Exception in refreshing fields of all modules : "

    GET_TOKENS_DB_ERROR = "Exception in get_tokens - DBStore"

    DELETE_TOKENS_DB_ERROR = "Exception in delete_tokens - DBStore"

    GET_TOKENS_FILE_ERROR = "Exception in get_tokens - FileStore"

    DELETE_TOKENS_FILE_ERROR = "Exception in delete_tokens - FileStore"

    SDK_UNINITIALIZATION_ERROR = "SDK UNINITIALIZED ERROR"

    SDK_UNINITIALIZATION_MESSAGE = "SDK is UnInitialized"

    INITIALIZATION_EXCEPTION = "Exception in initialization"

    SWITCH_USER_EXCEPTION = "Exception in switching user"

    AUTO_REFRESH_FIELDS_ERROR_MESSAGE = "auto_refresh_fields MUST NOT be None."

    HEADER_NONE_ERROR = "NONE HEADER ERROR"

    PRODUCT_NAME = "Product_Name"

    HEADER_INSTANCE_NONE_ERROR = "Header Instance MUST NOT be None"

    PARAM_INSTANCE_NONE_ERROR = "Param Instance MUST NOT be None"

    HEADER_NAME_NONE_ERROR = "NONE HEADER NAME ERROR"

    HEADER_NAME_NULL_ERROR_MESSAGE = "Header Name MUST NOT be null"

    NONE_VALUE_ERROR_MESSAGE = " MUST NOT be None"

    PARAMETER_NONE_ERROR = "NONE PARAMETER ERROR"

    PARAM_NAME_NONE_ERROR = "NONE PARAM NAME ERROR"

    PARAM_NAME_NONE_ERROR_MESSAGE = "Param Name MUST NOT be None"

    USER_PROXY_ERROR = "USERPROXY ERROR"

    HOST_ERROR_MESSAGE = "Host MUST NOT be None"

    PORT_ERROR_MESSAGE = "Port MUST NOT be None"

    USER_ERROR_MESSAGE = "User MUST NOT be None/empty"

    UNSUPPORTED_IN_API = "API UNSUPPORTED OPERATION"

    UNSUPPORTED_IN_API_MESSAGE = " Operation is not supported by API"

    NULL_VALUE = "null"

    NOTES = "notes"

    ATTACHMENTS = "$attachments"

    JSON_FILE_EXTENSION = ".json"

    FILE_ERROR = "file_error"

    FILE_DOES_NOT_EXISTS = "file does not exists"

    CONSENT_LOOKUP = "consent_lookup"

    USER_MAIL_NULL_ERROR = "USER MAIL NONE ERROR"

    USER_MAIL_NULL_ERROR_MESSAGE = "User Mail MUST NOT be None. Set value to user_mail."

    JSON_DETAILS_ERROR = "ERROR IN READING JSONDETAILS FILE"

    INVALID_TOKEN_ERROR = "INVALID TOKEN ERROR"

    NO_ACCESS_TOKEN_ERROR = "ACCESS TOKEN IS NOT PRESENT IN RESPONSE"

    CLIENT_ID_NULL_ERROR_MESSAGE = "ClientID MUST NOT be null"

    CLIENT_SECRET_NULL_ERROR_MESSAGE = "ClientSecret MUST NOT be null"

    REQUEST_PROXY_ERROR_MESSAGE = "request_proxy must be instance of Request Proxy"

    USER_SIGNATURE_ERROR_MESSAGE = "user must be instance of userSignature."

    ENVIRONMENT_ERROR_MESSAGE = "environment must be instance of Environment."

    SDK_CONFIG_ERROR_MESSAGE = "sdk_config must be instance of sdkConfig."

    TOKEN_ERROR_MESSAGE = "token must be instance of Token."

    STORE_ERROR_MESSAGE = "store must be instance of Store."

    COUNT = "count"

    OWNER_LOOKUP = "ownerlookup"

    TOKEN_FILE = "sdk_tokens.txt"

    LOG_FILE_NAME = "sdk_logs.log"

    PYTHON = "python_"

    OAUTH_MANDATORY_KEYS = ["grant_token", "refresh_token", "id", "access_token"]
