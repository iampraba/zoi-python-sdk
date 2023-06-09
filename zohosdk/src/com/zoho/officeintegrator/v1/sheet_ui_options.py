try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class SheetUiOptions(object):
	def __init__(self):
		"""Creates an instance of SheetUiOptions"""

		self.__save_button = None
		self.__key_modified = dict()

	def get_save_button(self):
		"""
		The method to get the save_button

		Returns:
			string: A string representing the save_button
		"""

		return self.__save_button

	def set_save_button(self, save_button):
		"""
		The method to set the value to save_button

		Parameters:
			save_button (string) : A string representing the save_button
		"""

		if save_button is not None and not isinstance(save_button, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: save_button EXPECTED TYPE: str', None, None)
		
		self.__save_button = save_button
		self.__key_modified['save_button'] = 1

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
