try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class SheetCallbackSettings(object):
	def __init__(self):
		"""Creates an instance of SheetCallbackSettings"""

		self.__save_format = None
		self.__save_url = None
		self.__savetype = None
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

	def get_savetype(self):
		"""
		The method to get the savetype

		Returns:
			string: A string representing the savetype
		"""

		return self.__savetype

	def set_savetype(self, savetype):
		"""
		The method to set the value to savetype

		Parameters:
			savetype (string) : A string representing the savetype
		"""

		if savetype is not None and not isinstance(savetype, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: savetype EXPECTED TYPE: str', None, None)
		
		self.__savetype = savetype
		self.__key_modified['savetype'] = 1

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
