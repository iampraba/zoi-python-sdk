try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.show_response_handler import ShowResponseHandler
	from zohosdk.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .show_response_handler import ShowResponseHandler
	from .writer_response_handler import WriterResponseHandler


class CreateDocumentResponse(WriterResponseHandler, ShowResponseHandler):
	def __init__(self):
		"""Creates an instance of CreateDocumentResponse"""
		super().__init__()

		self.__document_url = None
		self.__document_id = None
		self.__save_url = None
		self.__session_id = None
		self.__session_delete_url = None
		self.__document_delete_url = None
		self.__key_modified = dict()

	def get_document_url(self):
		"""
		The method to get the document_url

		Returns:
			string: A string representing the document_url
		"""

		return self.__document_url

	def set_document_url(self, document_url):
		"""
		The method to set the value to document_url

		Parameters:
			document_url (string) : A string representing the document_url
		"""

		if document_url is not None and not isinstance(document_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_url EXPECTED TYPE: str', None, None)
		
		self.__document_url = document_url
		self.__key_modified['document_url'] = 1

	def get_document_id(self):
		"""
		The method to get the document_id

		Returns:
			string: A string representing the document_id
		"""

		return self.__document_id

	def set_document_id(self, document_id):
		"""
		The method to set the value to document_id

		Parameters:
			document_id (string) : A string representing the document_id
		"""

		if document_id is not None and not isinstance(document_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_id EXPECTED TYPE: str', None, None)
		
		self.__document_id = document_id
		self.__key_modified['document_id'] = 1

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

	def get_session_id(self):
		"""
		The method to get the session_id

		Returns:
			string: A string representing the session_id
		"""

		return self.__session_id

	def set_session_id(self, session_id):
		"""
		The method to set the value to session_id

		Parameters:
			session_id (string) : A string representing the session_id
		"""

		if session_id is not None and not isinstance(session_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: session_id EXPECTED TYPE: str', None, None)
		
		self.__session_id = session_id
		self.__key_modified['session_id'] = 1

	def get_session_delete_url(self):
		"""
		The method to get the session_delete_url

		Returns:
			string: A string representing the session_delete_url
		"""

		return self.__session_delete_url

	def set_session_delete_url(self, session_delete_url):
		"""
		The method to set the value to session_delete_url

		Parameters:
			session_delete_url (string) : A string representing the session_delete_url
		"""

		if session_delete_url is not None and not isinstance(session_delete_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: session_delete_url EXPECTED TYPE: str', None, None)
		
		self.__session_delete_url = session_delete_url
		self.__key_modified['session_delete_url'] = 1

	def get_document_delete_url(self):
		"""
		The method to get the document_delete_url

		Returns:
			string: A string representing the document_delete_url
		"""

		return self.__document_delete_url

	def set_document_delete_url(self, document_delete_url):
		"""
		The method to set the value to document_delete_url

		Parameters:
			document_delete_url (string) : A string representing the document_delete_url
		"""

		if document_delete_url is not None and not isinstance(document_delete_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_delete_url EXPECTED TYPE: str', None, None)
		
		self.__document_delete_url = document_delete_url
		self.__key_modified['document_delete_url'] = 1

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
