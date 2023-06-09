try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .writer_response_handler import WriterResponseHandler


class MergeAndDeliverViaWebhookSuccessResponse(WriterResponseHandler):
	def __init__(self):
		"""Creates an instance of MergeAndDeliverViaWebhookSuccessResponse"""
		super().__init__()

		self.__merge_report_data_url = None
		self.__records = None
		self.__key_modified = dict()

	def get_merge_report_data_url(self):
		"""
		The method to get the merge_report_data_url

		Returns:
			string: A string representing the merge_report_data_url
		"""

		return self.__merge_report_data_url

	def set_merge_report_data_url(self, merge_report_data_url):
		"""
		The method to set the value to merge_report_data_url

		Parameters:
			merge_report_data_url (string) : A string representing the merge_report_data_url
		"""

		if merge_report_data_url is not None and not isinstance(merge_report_data_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: merge_report_data_url EXPECTED TYPE: str', None, None)
		
		self.__merge_report_data_url = merge_report_data_url
		self.__key_modified['merge_report_data_url'] = 1

	def get_records(self):
		"""
		The method to get the records

		Returns:
			list: An instance of list
		"""

		return self.__records

	def set_records(self, records):
		"""
		The method to set the value to records

		Parameters:
			records (list) : An instance of list
		"""

		if records is not None and not isinstance(records, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: records EXPECTED TYPE: list', None, None)
		
		self.__records = records
		self.__key_modified['records'] = 1

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
