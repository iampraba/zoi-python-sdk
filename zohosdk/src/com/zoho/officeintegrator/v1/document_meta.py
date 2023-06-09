try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .writer_response_handler import WriterResponseHandler


class DocumentMeta(WriterResponseHandler):
	def __init__(self):
		"""Creates an instance of DocumentMeta"""
		super().__init__()

		self.__document_id = None
		self.__collaborators_count = None
		self.__active_sessions_count = None
		self.__document_name = None
		self.__document_type = None
		self.__created_time = None
		self.__created_time_ms = None
		self.__expires_on = None
		self.__expires_on_ms = None
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

	def get_collaborators_count(self):
		"""
		The method to get the collaborators_count

		Returns:
			int: An int representing the collaborators_count
		"""

		return self.__collaborators_count

	def set_collaborators_count(self, collaborators_count):
		"""
		The method to set the value to collaborators_count

		Parameters:
			collaborators_count (int) : An int representing the collaborators_count
		"""

		if collaborators_count is not None and not isinstance(collaborators_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: collaborators_count EXPECTED TYPE: int', None, None)
		
		self.__collaborators_count = collaborators_count
		self.__key_modified['collaborators_count'] = 1

	def get_active_sessions_count(self):
		"""
		The method to get the active_sessions_count

		Returns:
			int: An int representing the active_sessions_count
		"""

		return self.__active_sessions_count

	def set_active_sessions_count(self, active_sessions_count):
		"""
		The method to set the value to active_sessions_count

		Parameters:
			active_sessions_count (int) : An int representing the active_sessions_count
		"""

		if active_sessions_count is not None and not isinstance(active_sessions_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: active_sessions_count EXPECTED TYPE: int', None, None)
		
		self.__active_sessions_count = active_sessions_count
		self.__key_modified['active_sessions_count'] = 1

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

	def get_document_type(self):
		"""
		The method to get the document_type

		Returns:
			string: A string representing the document_type
		"""

		return self.__document_type

	def set_document_type(self, document_type):
		"""
		The method to set the value to document_type

		Parameters:
			document_type (string) : A string representing the document_type
		"""

		if document_type is not None and not isinstance(document_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_type EXPECTED TYPE: str', None, None)
		
		self.__document_type = document_type
		self.__key_modified['document_type'] = 1

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
