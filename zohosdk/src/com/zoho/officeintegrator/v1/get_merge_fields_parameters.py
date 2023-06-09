try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import StreamWrapper, Constants
except Exception:
	from ...exception import SDKException
	from ...util import StreamWrapper, Constants


class GetMergeFieldsParameters(object):
	def __init__(self):
		"""Creates an instance of GetMergeFieldsParameters"""

		self.__file_content = None
		self.__file_url = None
		self.__key_modified = dict()

	def get_file_content(self):
		"""
		The method to get the file_content

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__file_content

	def set_file_content(self, file_content):
		"""
		The method to set the value to file_content

		Parameters:
			file_content (StreamWrapper) : An instance of StreamWrapper
		"""

		if file_content is not None and not isinstance(file_content, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_content EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__file_content = file_content
		self.__key_modified['file_content'] = 1

	def get_file_url(self):
		"""
		The method to get the file_url

		Returns:
			string: A string representing the file_url
		"""

		return self.__file_url

	def set_file_url(self, file_url):
		"""
		The method to set the value to file_url

		Parameters:
			file_url (string) : A string representing the file_url
		"""

		if file_url is not None and not isinstance(file_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_url EXPECTED TYPE: str', None, None)
		
		self.__file_url = file_url
		self.__key_modified['file_url'] = 1

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
