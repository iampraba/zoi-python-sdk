try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.show_response_handler import ShowResponseHandler
	from zohosdk.src.com.zoho.officeintegrator.v1.sheet_response_handler import SheetResponseHandler
	from zohosdk.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .show_response_handler import ShowResponseHandler
	from .sheet_response_handler import SheetResponseHandler
	from .writer_response_handler import WriterResponseHandler


class SessionMeta(WriterResponseHandler, SheetResponseHandler, ShowResponseHandler):
	def __init__(self):
		"""Creates an instance of SessionMeta"""
		super().__init__()

		self.__status = None
		self.__info = None
		self.__user_info = None
		self.__key_modified = dict()

	def get_status(self):
		"""
		The method to get the status

		Returns:
			string: A string representing the status
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (string) : A string representing the status
		"""

		if status is not None and not isinstance(status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: str', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

	def get_info(self):
		"""
		The method to get the info

		Returns:
			SessionInfo: An instance of SessionInfo
		"""

		return self.__info

	def set_info(self, info):
		"""
		The method to set the value to info

		Parameters:
			info (SessionInfo) : An instance of SessionInfo
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.session_info import SessionInfo
		except Exception:
			from .session_info import SessionInfo

		if info is not None and not isinstance(info, SessionInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: info EXPECTED TYPE: SessionInfo', None, None)
		
		self.__info = info
		self.__key_modified['info'] = 1

	def get_user_info(self):
		"""
		The method to get the user_info

		Returns:
			SessionUserInfo: An instance of SessionUserInfo
		"""

		return self.__user_info

	def set_user_info(self, user_info):
		"""
		The method to set the value to user_info

		Parameters:
			user_info (SessionUserInfo) : An instance of SessionUserInfo
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.session_user_info import SessionUserInfo
		except Exception:
			from .session_user_info import SessionUserInfo

		if user_info is not None and not isinstance(user_info, SessionUserInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_info EXPECTED TYPE: SessionUserInfo', None, None)
		
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
