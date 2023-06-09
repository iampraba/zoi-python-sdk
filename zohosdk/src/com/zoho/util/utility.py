try:
    import logging
    import threading
    import datetime
    import time
    import os
    import json
    import zlib
    import base64
    import re
    from zohosdk.src.com.zoho.initializer import Initializer
    from zohosdk.src.com.zoho.exception import SDKException
    from zohosdk.src.com.zoho.header_map import HeaderMap

except Exception:
    import logging
    import threading
    import os
    import json
    import time
    import datetime
    import zlib
    import base64
    import re
    from ..initializer import Initializer
    from ..exception import SDKException
    from ..header_map import HeaderMap


class Utility(object):
    """
    This class handles module field details.
    """
    
    @staticmethod
    def search_json_details(key):
        try:
            from zohosdk.src.com.zoho.util import Constants
        except Exception:
            from .constants import Constants

        package_name = Constants.PACKAGE_NAMESPACE + 'record.' + key

        from zohosdk.src.com.zoho.initializer import Initializer

        for class_key in Initializer.json_details.keys():
            if class_key == package_name:
                return_json = {
                    Constants.MODULEPACKAGENAME: class_key,
                    Constants.MODULEDETAILS: Initializer.json_details[class_key]
                }

                return return_json

        return None

    @staticmethod
    def get_json_object(json, key):
        for key_in_json in json.keys():
            if key_in_json.lower() == key.lower():
                return json[key_in_json]

        return None
    
    @staticmethod
    def check_data_type(value, type):
        try:
            from zohosdk.src.com.zoho.util import Constants
        except Exception:
            from .constants import Constants
        if value is None:
            return False
        if type.lower() == Constants.OBJECT.lower():
            return True
        type = Constants.DATA_TYPE.get(type)
        class_name = value.__class__
        if class_name == type:
            return True
        else:
            return False
