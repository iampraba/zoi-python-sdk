try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class Margin(object):
	def __init__(self):
		"""Creates an instance of Margin"""

		self.__left = None
		self.__right = None
		self.__top = None
		self.__bottom = None
		self.__key_modified = dict()

	def get_left(self):
		"""
		The method to get the left

		Returns:
			string: A string representing the left
		"""

		return self.__left

	def set_left(self, left):
		"""
		The method to set the value to left

		Parameters:
			left (string) : A string representing the left
		"""

		if left is not None and not isinstance(left, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: left EXPECTED TYPE: str', None, None)
		
		self.__left = left
		self.__key_modified['left'] = 1

	def get_right(self):
		"""
		The method to get the right

		Returns:
			string: A string representing the right
		"""

		return self.__right

	def set_right(self, right):
		"""
		The method to set the value to right

		Parameters:
			right (string) : A string representing the right
		"""

		if right is not None and not isinstance(right, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: right EXPECTED TYPE: str', None, None)
		
		self.__right = right
		self.__key_modified['right'] = 1

	def get_top(self):
		"""
		The method to get the top

		Returns:
			string: A string representing the top
		"""

		return self.__top

	def set_top(self, top):
		"""
		The method to set the value to top

		Parameters:
			top (string) : A string representing the top
		"""

		if top is not None and not isinstance(top, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: top EXPECTED TYPE: str', None, None)
		
		self.__top = top
		self.__key_modified['top'] = 1

	def get_bottom(self):
		"""
		The method to get the bottom

		Returns:
			string: A string representing the bottom
		"""

		return self.__bottom

	def set_bottom(self, bottom):
		"""
		The method to set the value to bottom

		Parameters:
			bottom (string) : A string representing the bottom
		"""

		if bottom is not None and not isinstance(bottom, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: bottom EXPECTED TYPE: str', None, None)
		
		self.__bottom = bottom
		self.__key_modified['bottom'] = 1

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
