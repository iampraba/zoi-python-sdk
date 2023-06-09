try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class SessionInfo(object):
	def __init__(self):
		"""Creates an instance of SessionInfo"""

		self.__document_id = None
		self.__created_time_ms = None
		self.__created_time = None
		self.__expires_on_ms = None
		self.__expires_on = None
		self.__session_url = None
		self.__session_delete_url = None
		self.__key_modified = dict()

	def get_document_id(self):
		"""
		The method to get the document_id

		Returns:
			string: A string representing the document_id
		"""

		return self.__document_id

	def set_document_id(self, document_id):
		"""
		The method to set the value to document_id

		Parameters:
			document_id (string) : A string representing the document_id
		"""

		if document_id is not None and not isinstance(document_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_id EXPECTED TYPE: str', None, None)
		
		self.__document_id = document_id
		self.__key_modified['document_id'] = 1

	def get_created_time_ms(self):
		"""
		The method to get the created_time_ms

		Returns:
			int: An int representing the created_time_ms
		"""

		return self.__created_time_ms

	def set_created_time_ms(self, created_time_ms):
		"""
		The method to set the value to created_time_ms

		Parameters:
			created_time_ms (int) : An int representing the created_time_ms
		"""

		if created_time_ms is not None and not isinstance(created_time_ms, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time_ms EXPECTED TYPE: int', None, None)
		
		self.__created_time_ms = created_time_ms
		self.__key_modified['created_time_ms'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			string: A string representing the created_time
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (string) : A string representing the created_time
		"""

		if created_time is not None and not isinstance(created_time, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: str', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_expires_on_ms(self):
		"""
		The method to get the expires_on_ms

		Returns:
			int: An int representing the expires_on_ms
		"""

		return self.__expires_on_ms

	def set_expires_on_ms(self, expires_on_ms):
		"""
		The method to set the value to expires_on_ms

		Parameters:
			expires_on_ms (int) : An int representing the expires_on_ms
		"""

		if expires_on_ms is not None and not isinstance(expires_on_ms, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: expires_on_ms EXPECTED TYPE: int', None, None)
		
		self.__expires_on_ms = expires_on_ms
		self.__key_modified['expires_on_ms'] = 1

	def get_expires_on(self):
		"""
		The method to get the expires_on

		Returns:
			string: A string representing the expires_on
		"""

		return self.__expires_on

	def set_expires_on(self, expires_on):
		"""
		The method to set the value to expires_on

		Parameters:
			expires_on (string) : A string representing the expires_on
		"""

		if expires_on is not None and not isinstance(expires_on, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: expires_on EXPECTED TYPE: str', None, None)
		
		self.__expires_on = expires_on
		self.__key_modified['expires_on'] = 1

	def get_session_url(self):
		"""
		The method to get the session_url

		Returns:
			string: A string representing the session_url
		"""

		return self.__session_url

	def set_session_url(self, session_url):
		"""
		The method to set the value to session_url

		Parameters:
			session_url (string) : A string representing the session_url
		"""

		if session_url is not None and not isinstance(session_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: session_url EXPECTED TYPE: str', None, None)
		
		self.__session_url = session_url
		self.__key_modified['session_url'] = 1

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
