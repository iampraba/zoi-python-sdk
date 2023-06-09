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


class SessionDeleteSuccessResponse(SheetResponseHandler, ShowResponseHandler):
	def __init__(self):
		"""Creates an instance of SessionDeleteSuccessResponse"""
		super().__init__()

		self.__session_delete = None
		self.__key_modified = dict()

	def get_session_delete(self):
		"""
		The method to get the session_delete

		Returns:
			string: A string representing the session_delete
		"""

		return self.__session_delete

	def set_session_delete(self, session_delete):
		"""
		The method to set the value to session_delete

		Parameters:
			session_delete (string) : A string representing the session_delete
		"""

		if session_delete is not None and not isinstance(session_delete, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: session_delete EXPECTED TYPE: str', None, None)
		
		self.__session_delete = session_delete
		self.__key_modified['session_delete'] = 1

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
