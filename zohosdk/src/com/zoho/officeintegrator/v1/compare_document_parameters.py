try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import StreamWrapper, Constants
except Exception:
	from ...exception import SDKException
	from ...util import StreamWrapper, Constants


class CompareDocumentParameters(object):
	def __init__(self):
		"""Creates an instance of CompareDocumentParameters"""

		self.__document1 = None
		self.__url1 = None
		self.__document2 = None
		self.__url2 = None
		self.__title = None
		self.__lang = None
		self.__key_modified = dict()

	def get_document1(self):
		"""
		The method to get the document1

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__document1

	def set_document1(self, document1):
		"""
		The method to set the value to document1

		Parameters:
			document1 (StreamWrapper) : An instance of StreamWrapper
		"""

		if document1 is not None and not isinstance(document1, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document1 EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__document1 = document1
		self.__key_modified['document1'] = 1

	def get_url1(self):
		"""
		The method to get the url1

		Returns:
			string: A string representing the url1
		"""

		return self.__url1

	def set_url1(self, url1):
		"""
		The method to set the value to url1

		Parameters:
			url1 (string) : A string representing the url1
		"""

		if url1 is not None and not isinstance(url1, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: url1 EXPECTED TYPE: str', None, None)
		
		self.__url1 = url1
		self.__key_modified['url1'] = 1

	def get_document2(self):
		"""
		The method to get the document2

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__document2

	def set_document2(self, document2):
		"""
		The method to set the value to document2

		Parameters:
			document2 (StreamWrapper) : An instance of StreamWrapper
		"""

		if document2 is not None and not isinstance(document2, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document2 EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__document2 = document2
		self.__key_modified['document2'] = 1

	def get_url2(self):
		"""
		The method to get the url2

		Returns:
			string: A string representing the url2
		"""

		return self.__url2

	def set_url2(self, url2):
		"""
		The method to set the value to url2

		Parameters:
			url2 (string) : A string representing the url2
		"""

		if url2 is not None and not isinstance(url2, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: url2 EXPECTED TYPE: str', None, None)
		
		self.__url2 = url2
		self.__key_modified['url2'] = 1

	def get_title(self):
		"""
		The method to get the title

		Returns:
			string: A string representing the title
		"""

		return self.__title

	def set_title(self, title):
		"""
		The method to set the value to title

		Parameters:
			title (string) : A string representing the title
		"""

		if title is not None and not isinstance(title, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: title EXPECTED TYPE: str', None, None)
		
		self.__title = title
		self.__key_modified['title'] = 1

	def get_lang(self):
		"""
		The method to get the lang

		Returns:
			string: A string representing the lang
		"""

		return self.__lang

	def set_lang(self, lang):
		"""
		The method to set the value to lang

		Parameters:
			lang (string) : A string representing the lang
		"""

		if lang is not None and not isinstance(lang, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lang EXPECTED TYPE: str', None, None)
		
		self.__lang = lang
		self.__key_modified['lang'] = 1

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
