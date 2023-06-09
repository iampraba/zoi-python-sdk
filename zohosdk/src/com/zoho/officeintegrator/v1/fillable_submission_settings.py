try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class FillableSubmissionSettings(object):
	def __init__(self):
		"""Creates an instance of FillableSubmissionSettings"""

		self.__callback_options = None
		self.__redirect_url = None
		self.__onsubmit_message = None
		self.__key_modified = dict()

	def get_callback_options(self):
		"""
		The method to get the callback_options

		Returns:
			FillableCallbackSettings: An instance of FillableCallbackSettings
		"""

		return self.__callback_options

	def set_callback_options(self, callback_options):
		"""
		The method to set the value to callback_options

		Parameters:
			callback_options (FillableCallbackSettings) : An instance of FillableCallbackSettings
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.fillable_callback_settings import FillableCallbackSettings
		except Exception:
			from .fillable_callback_settings import FillableCallbackSettings

		if callback_options is not None and not isinstance(callback_options, FillableCallbackSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: callback_options EXPECTED TYPE: FillableCallbackSettings', None, None)
		
		self.__callback_options = callback_options
		self.__key_modified['callback_options'] = 1

	def get_redirect_url(self):
		"""
		The method to get the redirect_url

		Returns:
			string: A string representing the redirect_url
		"""

		return self.__redirect_url

	def set_redirect_url(self, redirect_url):
		"""
		The method to set the value to redirect_url

		Parameters:
			redirect_url (string) : A string representing the redirect_url
		"""

		if redirect_url is not None and not isinstance(redirect_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: redirect_url EXPECTED TYPE: str', None, None)
		
		self.__redirect_url = redirect_url
		self.__key_modified['redirect_url'] = 1

	def get_onsubmit_message(self):
		"""
		The method to get the onsubmit_message

		Returns:
			string: A string representing the onsubmit_message
		"""

		return self.__onsubmit_message

	def set_onsubmit_message(self, onsubmit_message):
		"""
		The method to set the value to onsubmit_message

		Parameters:
			onsubmit_message (string) : A string representing the onsubmit_message
		"""

		if onsubmit_message is not None and not isinstance(onsubmit_message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: onsubmit_message EXPECTED TYPE: str', None, None)
		
		self.__onsubmit_message = onsubmit_message
		self.__key_modified['onsubmit_message'] = 1

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
