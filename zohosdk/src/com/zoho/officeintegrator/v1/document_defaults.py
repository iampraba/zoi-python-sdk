try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class DocumentDefaults(object):
	def __init__(self):
		"""Creates an instance of DocumentDefaults"""

		self.__orientation = None
		self.__paper_size = None
		self.__font_name = None
		self.__font_size = None
		self.__track_changes = None
		self.__language = None
		self.__margin = None
		self.__key_modified = dict()

	def get_orientation(self):
		"""
		The method to get the orientation

		Returns:
			string: A string representing the orientation
		"""

		return self.__orientation

	def set_orientation(self, orientation):
		"""
		The method to set the value to orientation

		Parameters:
			orientation (string) : A string representing the orientation
		"""

		if orientation is not None and not isinstance(orientation, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: orientation EXPECTED TYPE: str', None, None)
		
		self.__orientation = orientation
		self.__key_modified['orientation'] = 1

	def get_paper_size(self):
		"""
		The method to get the paper_size

		Returns:
			string: A string representing the paper_size
		"""

		return self.__paper_size

	def set_paper_size(self, paper_size):
		"""
		The method to set the value to paper_size

		Parameters:
			paper_size (string) : A string representing the paper_size
		"""

		if paper_size is not None and not isinstance(paper_size, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: paper_size EXPECTED TYPE: str', None, None)
		
		self.__paper_size = paper_size
		self.__key_modified['paper_size'] = 1

	def get_font_name(self):
		"""
		The method to get the font_name

		Returns:
			string: A string representing the font_name
		"""

		return self.__font_name

	def set_font_name(self, font_name):
		"""
		The method to set the value to font_name

		Parameters:
			font_name (string) : A string representing the font_name
		"""

		if font_name is not None and not isinstance(font_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: font_name EXPECTED TYPE: str', None, None)
		
		self.__font_name = font_name
		self.__key_modified['font_name'] = 1

	def get_font_size(self):
		"""
		The method to get the font_size

		Returns:
			int: An int representing the font_size
		"""

		return self.__font_size

	def set_font_size(self, font_size):
		"""
		The method to set the value to font_size

		Parameters:
			font_size (int) : An int representing the font_size
		"""

		if font_size is not None and not isinstance(font_size, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: font_size EXPECTED TYPE: int', None, None)
		
		self.__font_size = font_size
		self.__key_modified['font_size'] = 1

	def get_track_changes(self):
		"""
		The method to get the track_changes

		Returns:
			string: A string representing the track_changes
		"""

		return self.__track_changes

	def set_track_changes(self, track_changes):
		"""
		The method to set the value to track_changes

		Parameters:
			track_changes (string) : A string representing the track_changes
		"""

		if track_changes is not None and not isinstance(track_changes, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: track_changes EXPECTED TYPE: str', None, None)
		
		self.__track_changes = track_changes
		self.__key_modified['track_changes'] = 1

	def get_language(self):
		"""
		The method to get the language

		Returns:
			string: A string representing the language
		"""

		return self.__language

	def set_language(self, language):
		"""
		The method to set the value to language

		Parameters:
			language (string) : A string representing the language
		"""

		if language is not None and not isinstance(language, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: language EXPECTED TYPE: str', None, None)
		
		self.__language = language
		self.__key_modified['language'] = 1

	def get_margin(self):
		"""
		The method to get the margin

		Returns:
			Margin: An instance of Margin
		"""

		return self.__margin

	def set_margin(self, margin):
		"""
		The method to set the value to margin

		Parameters:
			margin (Margin) : An instance of Margin
		"""

		try:
			from zohosdk.src.com.zoho.officeintegrator.v1.margin import Margin
		except Exception:
			from .margin import Margin

		if margin is not None and not isinstance(margin, Margin):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: margin EXPECTED TYPE: Margin', None, None)
		
		self.__margin = margin
		self.__key_modified['margin'] = 1

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
