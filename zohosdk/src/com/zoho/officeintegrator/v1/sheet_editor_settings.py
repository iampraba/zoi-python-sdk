try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class SheetEditorSettings(object):
	def __init__(self):
		"""Creates an instance of SheetEditorSettings"""

		self.__country = None
		self.__language = None
		self.__key_modified = dict()

	def get_country(self):
		"""
		The method to get the country

		Returns:
			string: A string representing the country
		"""

		return self.__country

	def set_country(self, country):
		"""
		The method to set the value to country

		Parameters:
			country (string) : A string representing the country
		"""

		if country is not None and not isinstance(country, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: country EXPECTED TYPE: str', None, None)
		
		self.__country = country
		self.__key_modified['country'] = 1

	def get_language(self):
		"""
		The method to get the language

		Returns:
			string: A string representing the language
		"""

		return self.__language

	def set_language(self, language):
		"""
		The method to set the value to language

		Parameters:
			language (string) : A string representing the language
		"""

		if language is not None and not isinstance(language, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: language EXPECTED TYPE: str', None, None)
		
		self.__language = language
		self.__key_modified['language'] = 1

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
