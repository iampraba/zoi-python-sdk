try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .writer_response_handler import WriterResponseHandler


class DocumentDeleteSuccessResponse(WriterResponseHandler):
	def __init__(self):
		"""Creates an instance of DocumentDeleteSuccessResponse"""
		super().__init__()

		self.__document_deleted = None
		self.__key_modified = dict()

	def get_document_deleted(self):
		"""
		The method to get the document_deleted

		Returns:
			bool: A bool representing the document_deleted
		"""

		return self.__document_deleted

	def set_document_deleted(self, document_deleted):
		"""
		The method to set the value to document_deleted

		Parameters:
			document_deleted (bool) : A bool representing the document_deleted
		"""

		if document_deleted is not None and not isinstance(document_deleted, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_deleted EXPECTED TYPE: bool', None, None)
		
		self.__document_deleted = document_deleted
		self.__key_modified['document_deleted'] = 1

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
