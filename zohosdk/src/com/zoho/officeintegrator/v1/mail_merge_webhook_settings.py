try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class MailMergeWebhookSettings(object):
	def __init__(self):
		"""Creates an instance of MailMergeWebhookSettings"""

		self.__invoke_url = None
		self.__invoke_period = None
		self.__key_modified = dict()

	def get_invoke_url(self):
		"""
		The method to get the invoke_url

		Returns:
			string: A string representing the invoke_url
		"""

		return self.__invoke_url

	def set_invoke_url(self, invoke_url):
		"""
		The method to set the value to invoke_url

		Parameters:
			invoke_url (string) : A string representing the invoke_url
		"""

		if invoke_url is not None and not isinstance(invoke_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: invoke_url EXPECTED TYPE: str', None, None)
		
		self.__invoke_url = invoke_url
		self.__key_modified['invoke_url'] = 1

	def get_invoke_period(self):
		"""
		The method to get the invoke_period

		Returns:
			string: A string representing the invoke_period
		"""

		return self.__invoke_period

	def set_invoke_period(self, invoke_period):
		"""
		The method to set the value to invoke_period

		Parameters:
			invoke_period (string) : A string representing the invoke_period
		"""

		if invoke_period is not None and not isinstance(invoke_period, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: invoke_period EXPECTED TYPE: str', None, None)
		
		self.__invoke_period = invoke_period
		self.__key_modified['invoke_period'] = 1

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
