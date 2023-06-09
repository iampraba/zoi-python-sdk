try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
	from zohosdk.src.com.zoho.officeintegrator.v1.response_handler import ResponseHandler
except Exception:
	from ...exception import SDKException
	from ...util import Constants
	from .response_handler import ResponseHandler


class PlanDetails(ResponseHandler):
	def __init__(self):
		"""Creates an instance of PlanDetails"""
		super().__init__()

		self.__usage_limit = None
		self.__apikey_generated_time = None
		self.__remaining_usage_limit = None
		self.__last_payment_date_ms = None
		self.__next_payment_date_ms = None
		self.__last_payment_date = None
		self.__apikey_id = None
		self.__plan_name = None
		self.__apikey_generated_time_ms = None
		self.__payment_link = None
		self.__next_payment_date = None
		self.__subscription_interval = None
		self.__total_usage = None
		self.__subscription_period = None
		self.__key_modified = dict()

	def get_usage_limit(self):
		"""
		The method to get the usage_limit

		Returns:
			int: An int representing the usage_limit
		"""

		return self.__usage_limit

	def set_usage_limit(self, usage_limit):
		"""
		The method to set the value to usage_limit

		Parameters:
			usage_limit (int) : An int representing the usage_limit
		"""

		if usage_limit is not None and not isinstance(usage_limit, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: usage_limit EXPECTED TYPE: int', None, None)
		
		self.__usage_limit = usage_limit
		self.__key_modified['usage_limit'] = 1

	def get_apikey_generated_time(self):
		"""
		The method to get the apikey_generated_time

		Returns:
			string: A string representing the apikey_generated_time
		"""

		return self.__apikey_generated_time

	def set_apikey_generated_time(self, apikey_generated_time):
		"""
		The method to set the value to apikey_generated_time

		Parameters:
			apikey_generated_time (string) : A string representing the apikey_generated_time
		"""

		if apikey_generated_time is not None and not isinstance(apikey_generated_time, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: apikey_generated_time EXPECTED TYPE: str', None, None)
		
		self.__apikey_generated_time = apikey_generated_time
		self.__key_modified['apikey_generated_time'] = 1

	def get_remaining_usage_limit(self):
		"""
		The method to get the remaining_usage_limit

		Returns:
			int: An int representing the remaining_usage_limit
		"""

		return self.__remaining_usage_limit

	def set_remaining_usage_limit(self, remaining_usage_limit):
		"""
		The method to set the value to remaining_usage_limit

		Parameters:
			remaining_usage_limit (int) : An int representing the remaining_usage_limit
		"""

		if remaining_usage_limit is not None and not isinstance(remaining_usage_limit, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: remaining_usage_limit EXPECTED TYPE: int', None, None)
		
		self.__remaining_usage_limit = remaining_usage_limit
		self.__key_modified['remaining_usage_limit'] = 1

	def get_last_payment_date_ms(self):
		"""
		The method to get the last_payment_date_ms

		Returns:
			int: An int representing the last_payment_date_ms
		"""

		return self.__last_payment_date_ms

	def set_last_payment_date_ms(self, last_payment_date_ms):
		"""
		The method to set the value to last_payment_date_ms

		Parameters:
			last_payment_date_ms (int) : An int representing the last_payment_date_ms
		"""

		if last_payment_date_ms is not None and not isinstance(last_payment_date_ms, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_payment_date_ms EXPECTED TYPE: int', None, None)
		
		self.__last_payment_date_ms = last_payment_date_ms
		self.__key_modified['last_payment_date_ms'] = 1

	def get_next_payment_date_ms(self):
		"""
		The method to get the next_payment_date_ms

		Returns:
			int: An int representing the next_payment_date_ms
		"""

		return self.__next_payment_date_ms

	def set_next_payment_date_ms(self, next_payment_date_ms):
		"""
		The method to set the value to next_payment_date_ms

		Parameters:
			next_payment_date_ms (int) : An int representing the next_payment_date_ms
		"""

		if next_payment_date_ms is not None and not isinstance(next_payment_date_ms, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: next_payment_date_ms EXPECTED TYPE: int', None, None)
		
		self.__next_payment_date_ms = next_payment_date_ms
		self.__key_modified['next_payment_date_ms'] = 1

	def get_last_payment_date(self):
		"""
		The method to get the last_payment_date

		Returns:
			string: A string representing the last_payment_date
		"""

		return self.__last_payment_date

	def set_last_payment_date(self, last_payment_date):
		"""
		The method to set the value to last_payment_date

		Parameters:
			last_payment_date (string) : A string representing the last_payment_date
		"""

		if last_payment_date is not None and not isinstance(last_payment_date, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_payment_date EXPECTED TYPE: str', None, None)
		
		self.__last_payment_date = last_payment_date
		self.__key_modified['last_payment_date'] = 1

	def get_apikey_id(self):
		"""
		The method to get the apikey_id

		Returns:
			int: An int representing the apikey_id
		"""

		return self.__apikey_id

	def set_apikey_id(self, apikey_id):
		"""
		The method to set the value to apikey_id

		Parameters:
			apikey_id (int) : An int representing the apikey_id
		"""

		if apikey_id is not None and not isinstance(apikey_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: apikey_id EXPECTED TYPE: int', None, None)
		
		self.__apikey_id = apikey_id
		self.__key_modified['apikey_id'] = 1

	def get_plan_name(self):
		"""
		The method to get the plan_name

		Returns:
			string: A string representing the plan_name
		"""

		return self.__plan_name

	def set_plan_name(self, plan_name):
		"""
		The method to set the value to plan_name

		Parameters:
			plan_name (string) : A string representing the plan_name
		"""

		if plan_name is not None and not isinstance(plan_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: plan_name EXPECTED TYPE: str', None, None)
		
		self.__plan_name = plan_name
		self.__key_modified['plan_name'] = 1

	def get_apikey_generated_time_ms(self):
		"""
		The method to get the apikey_generated_time_ms

		Returns:
			int: An int representing the apikey_generated_time_ms
		"""

		return self.__apikey_generated_time_ms

	def set_apikey_generated_time_ms(self, apikey_generated_time_ms):
		"""
		The method to set the value to apikey_generated_time_ms

		Parameters:
			apikey_generated_time_ms (int) : An int representing the apikey_generated_time_ms
		"""

		if apikey_generated_time_ms is not None and not isinstance(apikey_generated_time_ms, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: apikey_generated_time_ms EXPECTED TYPE: int', None, None)
		
		self.__apikey_generated_time_ms = apikey_generated_time_ms
		self.__key_modified['apikey_generated_time_ms'] = 1

	def get_payment_link(self):
		"""
		The method to get the payment_link

		Returns:
			string: A string representing the payment_link
		"""

		return self.__payment_link

	def set_payment_link(self, payment_link):
		"""
		The method to set the value to payment_link

		Parameters:
			payment_link (string) : A string representing the payment_link
		"""

		if payment_link is not None and not isinstance(payment_link, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: payment_link EXPECTED TYPE: str', None, None)
		
		self.__payment_link = payment_link
		self.__key_modified['payment_link'] = 1

	def get_next_payment_date(self):
		"""
		The method to get the next_payment_date

		Returns:
			string: A string representing the next_payment_date
		"""

		return self.__next_payment_date

	def set_next_payment_date(self, next_payment_date):
		"""
		The method to set the value to next_payment_date

		Parameters:
			next_payment_date (string) : A string representing the next_payment_date
		"""

		if next_payment_date is not None and not isinstance(next_payment_date, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: next_payment_date EXPECTED TYPE: str', None, None)
		
		self.__next_payment_date = next_payment_date
		self.__key_modified['next_payment_date'] = 1

	def get_subscription_interval(self):
		"""
		The method to get the subscription_interval

		Returns:
			string: A string representing the subscription_interval
		"""

		return self.__subscription_interval

	def set_subscription_interval(self, subscription_interval):
		"""
		The method to set the value to subscription_interval

		Parameters:
			subscription_interval (string) : A string representing the subscription_interval
		"""

		if subscription_interval is not None and not isinstance(subscription_interval, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subscription_interval EXPECTED TYPE: str', None, None)
		
		self.__subscription_interval = subscription_interval
		self.__key_modified['subscription_interval'] = 1

	def get_total_usage(self):
		"""
		The method to get the total_usage

		Returns:
			int: An int representing the total_usage
		"""

		return self.__total_usage

	def set_total_usage(self, total_usage):
		"""
		The method to set the value to total_usage

		Parameters:
			total_usage (int) : An int representing the total_usage
		"""

		if total_usage is not None and not isinstance(total_usage, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: total_usage EXPECTED TYPE: int', None, None)
		
		self.__total_usage = total_usage
		self.__key_modified['total_usage'] = 1

	def get_subscription_period(self):
		"""
		The method to get the subscription_period

		Returns:
			string: A string representing the subscription_period
		"""

		return self.__subscription_period

	def set_subscription_period(self, subscription_period):
		"""
		The method to set the value to subscription_period

		Parameters:
			subscription_period (string) : A string representing the subscription_period
		"""

		if subscription_period is not None and not isinstance(subscription_period, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subscription_period EXPECTED TYPE: str', None, None)
		
		self.__subscription_period = subscription_period
		self.__key_modified['subscription_period'] = 1

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
