try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class FillableCallbackSettings(object):
	def __init__(self):
		"""Creates an instance of FillableCallbackSettings"""

		self.__output = None
		self.__url = None
		self.__http_method_type = None
		self.__retries = None
		self.__timeout = None
		self.__key_modified = dict()

	def get_output(self):
		"""
		The method to get the output

		Returns:
			FillableLinkOutputSettings: An instance of FillableLinkOutputSettings
		"""

		return self.__output

	def set_output(self, output):
		"""
		The method to set the value to output

		Parameters:
			output (FillableLinkOutputSettings) : An instance of FillableLinkOutputSettings
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.fillable_link_output_settings import FillableLinkOutputSettings
		except Exception:
			from .fillable_link_output_settings import FillableLinkOutputSettings

		if output is not None and not isinstance(output, FillableLinkOutputSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: output EXPECTED TYPE: FillableLinkOutputSettings', None, None)
		
		self.__output = output
		self.__key_modified['output'] = 1

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

	def get_http_method_type(self):
		"""
		The method to get the http_method_type

		Returns:
			string: A string representing the http_method_type
		"""

		return self.__http_method_type

	def set_http_method_type(self, http_method_type):
		"""
		The method to set the value to http_method_type

		Parameters:
			http_method_type (string) : A string representing the http_method_type
		"""

		if http_method_type is not None and not isinstance(http_method_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: http_method_type EXPECTED TYPE: str', None, None)
		
		self.__http_method_type = http_method_type
		self.__key_modified['http_method_type'] = 1

	def get_retries(self):
		"""
		The method to get the retries

		Returns:
			int: An int representing the retries
		"""

		return self.__retries

	def set_retries(self, retries):
		"""
		The method to set the value to retries

		Parameters:
			retries (int) : An int representing the retries
		"""

		if retries is not None and not isinstance(retries, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: retries EXPECTED TYPE: int', None, None)
		
		self.__retries = retries
		self.__key_modified['retries'] = 1

	def get_timeout(self):
		"""
		The method to get the timeout

		Returns:
			int: An int representing the timeout
		"""

		return self.__timeout

	def set_timeout(self, timeout):
		"""
		The method to set the value to timeout

		Parameters:
			timeout (int) : An int representing the timeout
		"""

		if timeout is not None and not isinstance(timeout, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: timeout EXPECTED TYPE: int', None, None)
		
		self.__timeout = timeout
		self.__key_modified['timeout'] = 1

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
