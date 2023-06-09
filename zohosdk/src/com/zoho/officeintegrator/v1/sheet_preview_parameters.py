try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import StreamWrapper, Constants
except Exception:
	from ...exception import SDKException
	from ...util import StreamWrapper, Constants


class SheetPreviewParameters(object):
	def __init__(self):
		"""Creates an instance of SheetPreviewParameters"""

		self.__url = None
		self.__document = None
		self.__language = None
		self.__permissions = None
		self.__key_modified = dict()

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

	def get_document(self):
		"""
		The method to get the document

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__document

	def set_document(self, document):
		"""
		The method to set the value to document

		Parameters:
			document (StreamWrapper) : An instance of StreamWrapper
		"""

		if document is not None and not isinstance(document, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__document = document
		self.__key_modified['document'] = 1

	def get_language(self):
		"""
		The method to get the language

		Returns:
			string: A string representing the language
		"""

		return self.__language

	def set_language(self, language):
		"""
		The method to set the value to language

		Parameters:
			language (string) : A string representing the language
		"""

		if language is not None and not isinstance(language, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: language EXPECTED TYPE: str', None, None)
		
		self.__language = language
		self.__key_modified['language'] = 1

	def get_permissions(self):
		"""
		The method to get the permissions

		Returns:
			dict: An instance of dict
		"""

		return self.__permissions

	def set_permissions(self, permissions):
		"""
		The method to set the value to permissions

		Parameters:
			permissions (dict) : An instance of dict
		"""

		if permissions is not None and not isinstance(permissions, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: permissions EXPECTED TYPE: dict', None, None)
		
		self.__permissions = permissions
		self.__key_modified['permissions'] = 1

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
