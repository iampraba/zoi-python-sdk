from contextlib import nullcontext
import logging
from zohosdk.src.com.zoho.exception.sdk_exception import SDKException

from zohosdk.src.com.zoho.util.constants import Constants
from .token import Token


class APIKey(Token):
    logger = logging.getLogger('SDKLogger')

    def __init__(self, apikey=None, type=None):

        if apikey != nullcontext or apikey != "":
            self.__apikey = apikey
        else:
            raise SDKException("APIKey is not empty/null", "Configure proper apikey value")

        if type is Constants.PARAMS or type is Constants.HEADERS:
            self.__type = type
        else:
            raise SDKException("APIKey Type not configured properly", "Configure apikey type as params/header")

    def authenticate(self, url_connection):
        if self.__type is Constants.PARAMS:
            url_connection.add_param("apikey", self.__apikey)
        elif self.__type is Constants.HEADERS:
            url_connection.add_header("X-API-Key", self.__apikey)
        else:
            raise SDKException("APIKey Type not configured properly", "Configure apikey type as params/header")

    def remove(self):
        return True
