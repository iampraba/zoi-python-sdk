try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class FillableLinkOutputSettings(object):
	def __init__(self):
		"""Creates an instance of FillableLinkOutputSettings"""

		self.__format = None
		self.__key_modified = dict()

	def get_format(self):
		"""
		The method to get the format

		Returns:
			string: A string representing the format
		"""

		return self.__format

	def set_format(self, format):
		"""
		The method to set the value to format

		Parameters:
			format (string) : A string representing the format
		"""

		if format is not None and not isinstance(format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: format EXPECTED TYPE: str', None, None)
		
		self.__format = format
		self.__key_modified['format'] = 1

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
