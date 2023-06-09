try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import StreamWrapper, Constants
except Exception:
	from ...exception import SDKException
	from ...util import StreamWrapper, Constants


class CreatePresentationParameters(object):
	def __init__(self):
		"""Creates an instance of CreatePresentationParameters"""

		self.__url = None
		self.__document = None
		self.__callback_settings = None
		self.__editor_settings = None
		self.__permissions = None
		self.__document_info = None
		self.__user_info = None
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
			ShowCallbackSettings: An instance of ShowCallbackSettings
		"""

		return self.__callback_settings

	def set_callback_settings(self, callback_settings):
		"""
		The method to set the value to callback_settings

		Parameters:
			callback_settings (ShowCallbackSettings) : An instance of ShowCallbackSettings
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.show_callback_settings import ShowCallbackSettings
		except Exception:
			from .show_callback_settings import ShowCallbackSettings

		if callback_settings is not None and not isinstance(callback_settings, ShowCallbackSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: callback_settings EXPECTED TYPE: ShowCallbackSettings', None, None)
		
		self.__callback_settings = callback_settings
		self.__key_modified['callback_settings'] = 1

	def get_editor_settings(self):
		"""
		The method to get the editor_settings

		Returns:
			ZohoShowEditorSettings: An instance of ZohoShowEditorSettings
		"""

		return self.__editor_settings

	def set_editor_settings(self, editor_settings):
		"""
		The method to set the value to editor_settings

		Parameters:
			editor_settings (ZohoShowEditorSettings) : An instance of ZohoShowEditorSettings
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.zoho_show_editor_settings import ZohoShowEditorSettings
		except Exception:
			from .zoho_show_editor_settings import ZohoShowEditorSettings

		if editor_settings is not None and not isinstance(editor_settings, ZohoShowEditorSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editor_settings EXPECTED TYPE: ZohoShowEditorSettings', None, None)
		
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
			UserInfo: An instance of UserInfo
		"""

		return self.__user_info

	def set_user_info(self, user_info):
		"""
		The method to set the value to user_info

		Parameters:
			user_info (UserInfo) : An instance of UserInfo
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.user_info import UserInfo
		except Exception:
			from .user_info import UserInfo

		if user_info is not None and not isinstance(user_info, UserInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_info EXPECTED TYPE: UserInfo', None, None)
		
		self.__user_info = user_info
		self.__key_modified['user_info'] = 1

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
