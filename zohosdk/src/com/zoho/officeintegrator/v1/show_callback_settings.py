try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class ShowCallbackSettings(object):
	def __init__(self):
		"""Creates an instance of ShowCallbackSettings"""

		self.__save_format = None
		self.__save_url = None
		self.__context_info = None
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

	def get_context_info(self):
		"""
		The method to get the context_info

		Returns:
			string: A string representing the context_info
		"""

		return self.__context_info

	def set_context_info(self, context_info):
		"""
		The method to set the value to context_info

		Parameters:
			context_info (string) : A string representing the context_info
		"""

		if context_info is not None and not isinstance(context_info, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: context_info EXPECTED TYPE: str', None, None)
		
		self.__context_info = context_info
		self.__key_modified['context_info'] = 1

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
