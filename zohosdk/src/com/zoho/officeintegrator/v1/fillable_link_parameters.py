try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import StreamWrapper, Constants
except Exception:
	from ...exception import SDKException
	from ...util import StreamWrapper, Constants


class FillableLinkParameters(object):
	def __init__(self):
		"""Creates an instance of FillableLinkParameters"""

		self.__document = None
		self.__url = None
		self.__document_info = None
		self.__user_info = None
		self.__prefill_data = None
		self.__form_language = None
		self.__submit_settings = None
		self.__form_options = None
		self.__key_modified = dict()

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

	def get_document_info(self):
		"""
		The method to get the document_info

		Returns:
			DocumentInfo: An instance of DocumentInfo
		"""

		return self.__document_info

	def set_document_info(self, document_info):
		"""
		The method to set the value to document_info

		Parameters:
			document_info (DocumentInfo) : An instance of DocumentInfo
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.document_info import DocumentInfo
		except Exception:
			from .document_info import DocumentInfo

		if document_info is not None and not isinstance(document_info, DocumentInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_info EXPECTED TYPE: DocumentInfo', None, None)
		
		self.__document_info = document_info
		self.__key_modified['document_info'] = 1

	def get_user_info(self):
		"""
		The method to get the user_info

		Returns:
			UserInfo: An instance of UserInfo
		"""

		return self.__user_info

	def set_user_info(self, user_info):
		"""
		The method to set the value to user_info

		Parameters:
			user_info (UserInfo) : An instance of UserInfo
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.user_info import UserInfo
		except Exception:
			from .user_info import UserInfo

		if user_info is not None and not isinstance(user_info, UserInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_info EXPECTED TYPE: UserInfo', None, None)
		
		self.__user_info = user_info
		self.__key_modified['user_info'] = 1

	def get_prefill_data(self):
		"""
		The method to get the prefill_data

		Returns:
			dict: An instance of dict
		"""

		return self.__prefill_data

	def set_prefill_data(self, prefill_data):
		"""
		The method to set the value to prefill_data

		Parameters:
			prefill_data (dict) : An instance of dict
		"""

		if prefill_data is not None and not isinstance(prefill_data, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: prefill_data EXPECTED TYPE: dict', None, None)
		
		self.__prefill_data = prefill_data
		self.__key_modified['prefill_data'] = 1

	def get_form_language(self):
		"""
		The method to get the form_language

		Returns:
			string: A string representing the form_language
		"""

		return self.__form_language

	def set_form_language(self, form_language):
		"""
		The method to set the value to form_language

		Parameters:
			form_language (string) : A string representing the form_language
		"""

		if form_language is not None and not isinstance(form_language, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: form_language EXPECTED TYPE: str', None, None)
		
		self.__form_language = form_language
		self.__key_modified['form_language'] = 1

	def get_submit_settings(self):
		"""
		The method to get the submit_settings

		Returns:
			FillableSubmissionSettings: An instance of FillableSubmissionSettings
		"""

		return self.__submit_settings

	def set_submit_settings(self, submit_settings):
		"""
		The method to set the value to submit_settings

		Parameters:
			submit_settings (FillableSubmissionSettings) : An instance of FillableSubmissionSettings
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.fillable_submission_settings import FillableSubmissionSettings
		except Exception:
			from .fillable_submission_settings import FillableSubmissionSettings

		if submit_settings is not None and not isinstance(submit_settings, FillableSubmissionSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: submit_settings EXPECTED TYPE: FillableSubmissionSettings', None, None)
		
		self.__submit_settings = submit_settings
		self.__key_modified['submit_settings'] = 1

	def get_form_options(self):
		"""
		The method to get the form_options

		Returns:
			FillableFormOptions: An instance of FillableFormOptions
		"""

		return self.__form_options

	def set_form_options(self, form_options):
		"""
		The method to set the value to form_options

		Parameters:
			form_options (FillableFormOptions) : An instance of FillableFormOptions
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.fillable_form_options import FillableFormOptions
		except Exception:
			from .fillable_form_options import FillableFormOptions

		if form_options is not None and not isinstance(form_options, FillableFormOptions):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: form_options EXPECTED TYPE: FillableFormOptions', None, None)
		
		self.__form_options = form_options
		self.__key_modified['form_options'] = 1

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
