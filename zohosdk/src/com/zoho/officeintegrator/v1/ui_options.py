try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class UiOptions(object):
	def __init__(self):
		"""Creates an instance of UiOptions"""

		self.__save_button = None
		self.__chat_panel = None
		self.__file_menu = None
		self.__dark_mode = None
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

	def get_chat_panel(self):
		"""
		The method to get the chat_panel

		Returns:
			string: A string representing the chat_panel
		"""

		return self.__chat_panel

	def set_chat_panel(self, chat_panel):
		"""
		The method to set the value to chat_panel

		Parameters:
			chat_panel (string) : A string representing the chat_panel
		"""

		if chat_panel is not None and not isinstance(chat_panel, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: chat_panel EXPECTED TYPE: str', None, None)
		
		self.__chat_panel = chat_panel
		self.__key_modified['chat_panel'] = 1

	def get_file_menu(self):
		"""
		The method to get the file_menu

		Returns:
			string: A string representing the file_menu
		"""

		return self.__file_menu

	def set_file_menu(self, file_menu):
		"""
		The method to set the value to file_menu

		Parameters:
			file_menu (string) : A string representing the file_menu
		"""

		if file_menu is not None and not isinstance(file_menu, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_menu EXPECTED TYPE: str', None, None)
		
		self.__file_menu = file_menu
		self.__key_modified['file_menu'] = 1

	def get_dark_mode(self):
		"""
		The method to get the dark_mode

		Returns:
			string: A string representing the dark_mode
		"""

		return self.__dark_mode

	def set_dark_mode(self, dark_mode):
		"""
		The method to set the value to dark_mode

		Parameters:
			dark_mode (string) : A string representing the dark_mode
		"""

		if dark_mode is not None and not isinstance(dark_mode, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: dark_mode EXPECTED TYPE: str', None, None)
		
		self.__dark_mode = dark_mode
		self.__key_modified['dark_mode'] = 1

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
