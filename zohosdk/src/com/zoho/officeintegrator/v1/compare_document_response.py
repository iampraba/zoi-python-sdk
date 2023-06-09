try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .writer_response_handler import WriterResponseHandler


class CompareDocumentResponse(WriterResponseHandler):
	def __init__(self):
		"""Creates an instance of CompareDocumentResponse"""
		super().__init__()

		self.__compare_url = None
		self.__session_delete_url = None
		self.__key_modified = dict()

	def get_compare_url(self):
		"""
		The method to get the compare_url

		Returns:
			string: A string representing the compare_url
		"""

		return self.__compare_url

	def set_compare_url(self, compare_url):
		"""
		The method to set the value to compare_url

		Parameters:
			compare_url (string) : A string representing the compare_url
		"""

		if compare_url is not None and not isinstance(compare_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: compare_url EXPECTED TYPE: str', None, None)
		
		self.__compare_url = compare_url
		self.__key_modified['compare_url'] = 1

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
