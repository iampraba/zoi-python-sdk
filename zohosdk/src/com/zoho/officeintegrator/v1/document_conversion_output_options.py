try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class DocumentConversionOutputOptions(object):
	def __init__(self):
		"""Creates an instance of DocumentConversionOutputOptions"""

		self.__format = None
		self.__document_name = None
		self.__password = None
		self.__include_changes = None
		self.__include_comments = None
		self.__key_modified = dict()

	def get_format(self):
		"""
		The method to get the format

		Returns:
			string: A string representing the format
		"""

		return self.__format

	def set_format(self, format):
		"""
		The method to set the value to format

		Parameters:
			format (string) : A string representing the format
		"""

		if format is not None and not isinstance(format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: format EXPECTED TYPE: str', None, None)
		
		self.__format = format
		self.__key_modified['format'] = 1

	def get_document_name(self):
		"""
		The method to get the document_name

		Returns:
			string: A string representing the document_name
		"""

		return self.__document_name

	def set_document_name(self, document_name):
		"""
		The method to set the value to document_name

		Parameters:
			document_name (string) : A string representing the document_name
		"""

		if document_name is not None and not isinstance(document_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_name EXPECTED TYPE: str', None, None)
		
		self.__document_name = document_name
		self.__key_modified['document_name'] = 1

	def get_password(self):
		"""
		The method to get the password

		Returns:
			string: A string representing the password
		"""

		return self.__password

	def set_password(self, password):
		"""
		The method to set the value to password

		Parameters:
			password (string) : A string representing the password
		"""

		if password is not None and not isinstance(password, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: password EXPECTED TYPE: str', None, None)
		
		self.__password = password
		self.__key_modified['password'] = 1

	def get_include_changes(self):
		"""
		The method to get the include_changes

		Returns:
			string: A string representing the include_changes
		"""

		return self.__include_changes

	def set_include_changes(self, include_changes):
		"""
		The method to set the value to include_changes

		Parameters:
			include_changes (string) : A string representing the include_changes
		"""

		if include_changes is not None and not isinstance(include_changes, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: include_changes EXPECTED TYPE: str', None, None)
		
		self.__include_changes = include_changes
		self.__key_modified['include_changes'] = 1

	def get_include_comments(self):
		"""
		The method to get the include_comments

		Returns:
			string: A string representing the include_comments
		"""

		return self.__include_comments

	def set_include_comments(self, include_comments):
		"""
		The method to set the value to include_comments

		Parameters:
			include_comments (string) : A string representing the include_comments
		"""

		if include_comments is not None and not isinstance(include_comments, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: include_comments EXPECTED TYPE: str', None, None)
		
		self.__include_comments = include_comments
		self.__key_modified['include_comments'] = 1

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
