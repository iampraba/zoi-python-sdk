try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .writer_response_handler import WriterResponseHandler


class DocumentSessionDeleteSuccessResponse(WriterResponseHandler):
	def __init__(self):
		"""Creates an instance of DocumentSessionDeleteSuccessResponse"""
		super().__init__()

		self.__session_deleted = None
		self.__key_modified = dict()

	def get_session_deleted(self):
		"""
		The method to get the session_deleted

		Returns:
			bool: A bool representing the session_deleted
		"""

		return self.__session_deleted

	def set_session_deleted(self, session_deleted):
		"""
		The method to set the value to session_deleted

		Parameters:
			session_deleted (bool) : A bool representing the session_deleted
		"""

		if session_deleted is not None and not isinstance(session_deleted, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: session_deleted EXPECTED TYPE: bool', None, None)
		
		self.__session_deleted = session_deleted
		self.__key_modified['session_deleted'] = 1

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
