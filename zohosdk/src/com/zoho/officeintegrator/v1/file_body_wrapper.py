try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import StreamWrapper, Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.show_response_handler import ShowResponseHandler
	from zohosdk.src.com.zoho.officeintegrator.v1.sheet_response_handler import SheetResponseHandler
	from zohosdk.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import StreamWrapper, Constants
	from .show_response_handler import ShowResponseHandler
	from .sheet_response_handler import SheetResponseHandler
	from .writer_response_handler import WriterResponseHandler


class FileBodyWrapper(WriterResponseHandler, SheetResponseHandler, ShowResponseHandler):
	def __init__(self):
		"""Creates an instance of FileBodyWrapper"""
		super().__init__()

		self.__file = None
		self.__key_modified = dict()

	def get_file(self):
		"""
		The method to get the file

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__file

	def set_file(self, file):
		"""
		The method to set the value to file

		Parameters:
			file (StreamWrapper) : An instance of StreamWrapper
		"""

		if file is not None and not isinstance(file, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__file = file
		self.__key_modified['file'] = 1

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
