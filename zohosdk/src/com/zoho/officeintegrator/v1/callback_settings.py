try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class CallbackSettings(object):
	def __init__(self):
		"""Creates an instance of CallbackSettings"""

		self.__save_format = None
		self.__save_url = None
		self.__http_method_type = None
		self.__retries = None
		self.__timeout = None
		self.__save_url_params = None
		self.__key_modified = dict()

	def get_save_format(self):
		"""
		The method to get the save_format

		Returns:
			string: A string representing the save_format
		"""

		return self.__save_format

	def set_save_format(self, save_format):
		"""
		The method to set the value to save_format

		Parameters:
			save_format (string) : A string representing the save_format
		"""

		if save_format is not None and not isinstance(save_format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: save_format EXPECTED TYPE: str', None, None)
		
		self.__save_format = save_format
		self.__key_modified['save_format'] = 1

	def get_save_url(self):
		"""
		The method to get the save_url

		Returns:
			string: A string representing the save_url
		"""

		return self.__save_url

	def set_save_url(self, save_url):
		"""
		The method to set the value to save_url

		Parameters:
			save_url (string) : A string representing the save_url
		"""

		if save_url is not None and not isinstance(save_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: save_url EXPECTED TYPE: str', None, None)
		
		self.__save_url = save_url
		self.__key_modified['save_url'] = 1

	def get_http_method_type(self):
		"""
		The method to get the http_method_type

		Returns:
			string: A string representing the http_method_type
		"""

		return self.__http_method_type

	def set_http_method_type(self, http_method_type):
		"""
		The method to set the value to http_method_type

		Parameters:
			http_method_type (string) : A string representing the http_method_type
		"""

		if http_method_type is not None and not isinstance(http_method_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: http_method_type EXPECTED TYPE: str', None, None)
		
		self.__http_method_type = http_method_type
		self.__key_modified['http_method_type'] = 1

	def get_retries(self):
		"""
		The method to get the retries

		Returns:
			int: An int representing the retries
		"""

		return self.__retries

	def set_retries(self, retries):
		"""
		The method to set the value to retries

		Parameters:
			retries (int) : An int representing the retries
		"""

		if retries is not None and not isinstance(retries, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: retries EXPECTED TYPE: int', None, None)
		
		self.__retries = retries
		self.__key_modified['retries'] = 1

	def get_timeout(self):
		"""
		The method to get the timeout

		Returns:
			int: An int representing the timeout
		"""

		return self.__timeout

	def set_timeout(self, timeout):
		"""
		The method to set the value to timeout

		Parameters:
			timeout (int) : An int representing the timeout
		"""

		if timeout is not None and not isinstance(timeout, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: timeout EXPECTED TYPE: int', None, None)
		
		self.__timeout = timeout
		self.__key_modified['timeout'] = 1

	def get_save_url_params(self):
		"""
		The method to get the save_url_params

		Returns:
			dict: An instance of dict
		"""

		return self.__save_url_params

	def set_save_url_params(self, save_url_params):
		"""
		The method to set the value to save_url_params

		Parameters:
			save_url_params (dict) : An instance of dict
		"""

		if save_url_params is not None and not isinstance(save_url_params, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: save_url_params EXPECTED TYPE: dict', None, None)
		
		self.__save_url_params = save_url_params
		self.__key_modified['save_url_params'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
