try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.show_response_handler import ShowResponseHandler
	from zohosdk.src.com.zoho.officeintegrator.v1.sheet_response_handler import SheetResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .show_response_handler import ShowResponseHandler
	from .sheet_response_handler import SheetResponseHandler


class FileDeleteSuccessResponse(SheetResponseHandler, ShowResponseHandler):
	def __init__(self):
		"""Creates an instance of FileDeleteSuccessResponse"""
		super().__init__()

		self.__doc_delete = None
		self.__key_modified = dict()

	def get_doc_delete(self):
		"""
		The method to get the doc_delete

		Returns:
			string: A string representing the doc_delete
		"""

		return self.__doc_delete

	def set_doc_delete(self, doc_delete):
		"""
		The method to set the value to doc_delete

		Parameters:
			doc_delete (string) : A string representing the doc_delete
		"""

		if doc_delete is not None and not isinstance(doc_delete, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: doc_delete EXPECTED TYPE: str', None, None)
		
		self.__doc_delete = doc_delete
		self.__key_modified['doc_delete'] = 1

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
