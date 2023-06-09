try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import StreamWrapper, Constants
except Exception:
	from ...exception import SDKException
	from ...util import StreamWrapper, Constants


class MergeAndDeliverViaWebhookParameters(object):
	def __init__(self):
		"""Creates an instance of MergeAndDeliverViaWebhookParameters"""

		self.__file_content = None
		self.__file_url = None
		self.__output_format = None
		self.__webhook = None
		self.__merge_to = None
		self.__merge_data = None
		self.__merge_data_csv_content = None
		self.__merge_data_json_content = None
		self.__merge_data_csv_url = None
		self.__merge_data_json_url = None
		self.__password = None
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

	def get_output_format(self):
		"""
		The method to get the output_format

		Returns:
			string: A string representing the output_format
		"""

		return self.__output_format

	def set_output_format(self, output_format):
		"""
		The method to set the value to output_format

		Parameters:
			output_format (string) : A string representing the output_format
		"""

		if output_format is not None and not isinstance(output_format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: output_format EXPECTED TYPE: str', None, None)
		
		self.__output_format = output_format
		self.__key_modified['output_format'] = 1

	def get_webhook(self):
		"""
		The method to get the webhook

		Returns:
			MailMergeWebhookSettings: An instance of MailMergeWebhookSettings
		"""

		return self.__webhook

	def set_webhook(self, webhook):
		"""
		The method to set the value to webhook

		Parameters:
			webhook (MailMergeWebhookSettings) : An instance of MailMergeWebhookSettings
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.mail_merge_webhook_settings import MailMergeWebhookSettings
		except Exception:
			from .mail_merge_webhook_settings import MailMergeWebhookSettings

		if webhook is not None and not isinstance(webhook, MailMergeWebhookSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: webhook EXPECTED TYPE: MailMergeWebhookSettings', None, None)
		
		self.__webhook = webhook
		self.__key_modified['webhook'] = 1

	def get_merge_to(self):
		"""
		The method to get the merge_to

		Returns:
			string: A string representing the merge_to
		"""

		return self.__merge_to

	def set_merge_to(self, merge_to):
		"""
		The method to set the value to merge_to

		Parameters:
			merge_to (string) : A string representing the merge_to
		"""

		if merge_to is not None and not isinstance(merge_to, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: merge_to EXPECTED TYPE: str', None, None)
		
		self.__merge_to = merge_to
		self.__key_modified['merge_to'] = 1

	def get_merge_data(self):
		"""
		The method to get the merge_data

		Returns:
			dict: An instance of dict
		"""

		return self.__merge_data

	def set_merge_data(self, merge_data):
		"""
		The method to set the value to merge_data

		Parameters:
			merge_data (dict) : An instance of dict
		"""

		if merge_data is not None and not isinstance(merge_data, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: merge_data EXPECTED TYPE: dict', None, None)
		
		self.__merge_data = merge_data
		self.__key_modified['merge_data'] = 1

	def get_merge_data_csv_content(self):
		"""
		The method to get the merge_data_csv_content

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__merge_data_csv_content

	def set_merge_data_csv_content(self, merge_data_csv_content):
		"""
		The method to set the value to merge_data_csv_content

		Parameters:
			merge_data_csv_content (StreamWrapper) : An instance of StreamWrapper
		"""

		if merge_data_csv_content is not None and not isinstance(merge_data_csv_content, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: merge_data_csv_content EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__merge_data_csv_content = merge_data_csv_content
		self.__key_modified['merge_data_csv_content'] = 1

	def get_merge_data_json_content(self):
		"""
		The method to get the merge_data_json_content

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__merge_data_json_content

	def set_merge_data_json_content(self, merge_data_json_content):
		"""
		The method to set the value to merge_data_json_content

		Parameters:
			merge_data_json_content (StreamWrapper) : An instance of StreamWrapper
		"""

		if merge_data_json_content is not None and not isinstance(merge_data_json_content, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: merge_data_json_content EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__merge_data_json_content = merge_data_json_content
		self.__key_modified['merge_data_json_content'] = 1

	def get_merge_data_csv_url(self):
		"""
		The method to get the merge_data_csv_url

		Returns:
			string: A string representing the merge_data_csv_url
		"""

		return self.__merge_data_csv_url

	def set_merge_data_csv_url(self, merge_data_csv_url):
		"""
		The method to set the value to merge_data_csv_url

		Parameters:
			merge_data_csv_url (string) : A string representing the merge_data_csv_url
		"""

		if merge_data_csv_url is not None and not isinstance(merge_data_csv_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: merge_data_csv_url EXPECTED TYPE: str', None, None)
		
		self.__merge_data_csv_url = merge_data_csv_url
		self.__key_modified['merge_data_csv_url'] = 1

	def get_merge_data_json_url(self):
		"""
		The method to get the merge_data_json_url

		Returns:
			string: A string representing the merge_data_json_url
		"""

		return self.__merge_data_json_url

	def set_merge_data_json_url(self, merge_data_json_url):
		"""
		The method to set the value to merge_data_json_url

		Parameters:
			merge_data_json_url (string) : A string representing the merge_data_json_url
		"""

		if merge_data_json_url is not None and not isinstance(merge_data_json_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: merge_data_json_url EXPECTED TYPE: str', None, None)
		
		self.__merge_data_json_url = merge_data_json_url
		self.__key_modified['merge_data_json_url'] = 1

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
