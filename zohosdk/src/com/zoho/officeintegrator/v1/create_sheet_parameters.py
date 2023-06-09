try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import StreamWrapper, Constants
except Exception:
	from ...exception import SDKException
	from ...util import StreamWrapper, Constants


class CreateSheetParameters(object):
	def __init__(self):
		"""Creates an instance of CreateSheetParameters"""

		self.__url = None
		self.__document = None
		self.__callback_settings = None
		self.__editor_settings = None
		self.__permissions = None
		self.__document_info = None
		self.__user_info = None
		self.__ui_options = None
		self.__key_modified = dict()

	def get_url(self):
		"""
		The method to get the url

		Returns:
			string: A string representing the url
		"""

		return self.__url

	def set_url(self, url):
		"""
		The method to set the value to url

		Parameters:
			url (string) : A string representing the url
		"""

		if url is not None and not isinstance(url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: url EXPECTED TYPE: str', None, None)
		
		self.__url = url
		self.__key_modified['url'] = 1

	def get_document(self):
		"""
		The method to get the document

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__document

	def set_document(self, document):
		"""
		The method to set the value to document

		Parameters:
			document (StreamWrapper) : An instance of StreamWrapper
		"""

		if document is not None and not isinstance(document, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__document = document
		self.__key_modified['document'] = 1

	def get_callback_settings(self):
		"""
		The method to get the callback_settings

		Returns:
			SheetCallbackSettings: An instance of SheetCallbackSettings
		"""

		return self.__callback_settings

	def set_callback_settings(self, callback_settings):
		"""
		The method to set the value to callback_settings

		Parameters:
			callback_settings (SheetCallbackSettings) : An instance of SheetCallbackSettings
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.sheet_callback_settings import SheetCallbackSettings
		except Exception:
			from .sheet_callback_settings import SheetCallbackSettings

		if callback_settings is not None and not isinstance(callback_settings, SheetCallbackSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: callback_settings EXPECTED TYPE: SheetCallbackSettings', None, None)
		
		self.__callback_settings = callback_settings
		self.__key_modified['callback_settings'] = 1

	def get_editor_settings(self):
		"""
		The method to get the editor_settings

		Returns:
			SheetEditorSettings: An instance of SheetEditorSettings
		"""

		return self.__editor_settings

	def set_editor_settings(self, editor_settings):
		"""
		The method to set the value to editor_settings

		Parameters:
			editor_settings (SheetEditorSettings) : An instance of SheetEditorSettings
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.sheet_editor_settings import SheetEditorSettings
		except Exception:
			from .sheet_editor_settings import SheetEditorSettings

		if editor_settings is not None and not isinstance(editor_settings, SheetEditorSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editor_settings EXPECTED TYPE: SheetEditorSettings', None, None)
		
		self.__editor_settings = editor_settings
		self.__key_modified['editor_settings'] = 1

	def get_permissions(self):
		"""
		The method to get the permissions

		Returns:
			dict: An instance of dict
		"""

		return self.__permissions

	def set_permissions(self, permissions):
		"""
		The method to set the value to permissions

		Parameters:
			permissions (dict) : An instance of dict
		"""

		if permissions is not None and not isinstance(permissions, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: permissions EXPECTED TYPE: dict', None, None)
		
		self.__permissions = permissions
		self.__key_modified['permissions'] = 1

	def get_document_info(self):
		"""
		The method to get the document_info

		Returns:
			DocumentInfo: An instance of DocumentInfo
		"""

		return self.__document_info

	def set_document_info(self, document_info):
		"""
		The method to set the value to document_info

		Parameters:
			document_info (DocumentInfo) : An instance of DocumentInfo
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.document_info import DocumentInfo
		except Exception:
			from .document_info import DocumentInfo

		if document_info is not None and not isinstance(document_info, DocumentInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_info EXPECTED TYPE: DocumentInfo', None, None)
		
		self.__document_info = document_info
		self.__key_modified['document_info'] = 1

	def get_user_info(self):
		"""
		The method to get the user_info

		Returns:
			SheetUserSettings: An instance of SheetUserSettings
		"""

		return self.__user_info

	def set_user_info(self, user_info):
		"""
		The method to set the value to user_info

		Parameters:
			user_info (SheetUserSettings) : An instance of SheetUserSettings
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.sheet_user_settings import SheetUserSettings
		except Exception:
			from .sheet_user_settings import SheetUserSettings

		if user_info is not None and not isinstance(user_info, SheetUserSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_info EXPECTED TYPE: SheetUserSettings', None, None)
		
		self.__user_info = user_info
		self.__key_modified['user_info'] = 1

	def get_ui_options(self):
		"""
		The method to get the ui_options

		Returns:
			SheetUiOptions: An instance of SheetUiOptions
		"""

		return self.__ui_options

	def set_ui_options(self, ui_options):
		"""
		The method to set the value to ui_options

		Parameters:
			ui_options (SheetUiOptions) : An instance of SheetUiOptions
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.sheet_ui_options import SheetUiOptions
		except Exception:
			from .sheet_ui_options import SheetUiOptions

		if ui_options is not None and not isinstance(ui_options, SheetUiOptions):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ui_options EXPECTED TYPE: SheetUiOptions', None, None)
		
		self.__ui_options = ui_options
		self.__key_modified['ui_options'] = 1

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
