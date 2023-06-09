try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.response_handler import ResponseHandler
	from zohosdk.src.com.zoho.officeintegrator.v1.show_response_handler import ShowResponseHandler
	from zohosdk.src.com.zoho.officeintegrator.v1.sheet_response_handler import SheetResponseHandler
	from zohosdk.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .response_handler import ResponseHandler
	from .show_response_handler import ShowResponseHandler
	from .sheet_response_handler import SheetResponseHandler
	from .writer_response_handler import WriterResponseHandler


class InvalidConfigurationException(WriterResponseHandler, SheetResponseHandler, ShowResponseHandler, ResponseHandler):
	def __init__(self):
		"""Creates an instance of InvalidConfigurationException"""
		super().__init__()

		self.__key_name = None
		self.__code = None
		self.__parameter_name = None
		self.__message = None
		self.__key_modified = dict()

	def get_key_name(self):
		"""
		The method to get the key_name

		Returns:
			string: A string representing the key_name
		"""

		return self.__key_name

	def set_key_name(self, key_name):
		"""
		The method to set the value to key_name

		Parameters:
			key_name (string) : A string representing the key_name
		"""

		if key_name is not None and not isinstance(key_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key_name EXPECTED TYPE: str', None, None)
		
		self.__key_name = key_name
		self.__key_modified['key_name'] = 1

	def get_code(self):
		"""
		The method to get the code

		Returns:
			int: An int representing the code
		"""

		return self.__code

	def set_code(self, code):
		"""
		The method to set the value to code

		Parameters:
			code (int) : An int representing the code
		"""

		if code is not None and not isinstance(code, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: code EXPECTED TYPE: int', None, None)
		
		self.__code = code
		self.__key_modified['code'] = 1

	def get_parameter_name(self):
		"""
		The method to get the parameter_name

		Returns:
			string: A string representing the parameter_name
		"""

		return self.__parameter_name

	def set_parameter_name(self, parameter_name):
		"""
		The method to set the value to parameter_name

		Parameters:
			parameter_name (string) : A string representing the parameter_name
		"""

		if parameter_name is not None and not isinstance(parameter_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parameter_name EXPECTED TYPE: str', None, None)
		
		self.__parameter_name = parameter_name
		self.__key_modified['parameter_name'] = 1

	def get_message(self):
		"""
		The method to get the message

		Returns:
			string: A string representing the message
		"""

		return self.__message

	def set_message(self, message):
		"""
		The method to set the value to message

		Parameters:
			message (string) : A string representing the message
		"""

		if message is not None and not isinstance(message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: message EXPECTED TYPE: str', None, None)
		
		self.__message = message
		self.__key_modified['message'] = 1

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
