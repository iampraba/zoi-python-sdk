try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class EditorSettings(object):
	def __init__(self):
		"""Creates an instance of EditorSettings"""

		self.__unit = None
		self.__language = None
		self.__view = None
		self.__key_modified = dict()

	def get_unit(self):
		"""
		The method to get the unit

		Returns:
			string: A string representing the unit
		"""

		return self.__unit

	def set_unit(self, unit):
		"""
		The method to set the value to unit

		Parameters:
			unit (string) : A string representing the unit
		"""

		if unit is not None and not isinstance(unit, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: unit EXPECTED TYPE: str', None, None)
		
		self.__unit = unit
		self.__key_modified['unit'] = 1

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

	def get_view(self):
		"""
		The method to get the view

		Returns:
			string: A string representing the view
		"""

		return self.__view

	def set_view(self, view):
		"""
		The method to set the value to view

		Parameters:
			view (string) : A string representing the view
		"""

		if view is not None and not isinstance(view, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: view EXPECTED TYPE: str', None, None)
		
		self.__view = view
		self.__key_modified['view'] = 1

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
