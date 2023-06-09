try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class WatermarkSettings(object):
	def __init__(self):
		"""Creates an instance of WatermarkSettings"""

		self.__text = None
		self.__type = None
		self.__orientation = None
		self.__font_name = None
		self.__font_size = None
		self.__font_color = None
		self.__opacity = None
		self.__key_modified = dict()

	def get_text(self):
		"""
		The method to get the text

		Returns:
			string: A string representing the text
		"""

		return self.__text

	def set_text(self, text):
		"""
		The method to set the value to text

		Parameters:
			text (string) : A string representing the text
		"""

		if text is not None and not isinstance(text, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: text EXPECTED TYPE: str', None, None)
		
		self.__text = text
		self.__key_modified['text'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

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

	def get_font_color(self):
		"""
		The method to get the font_color

		Returns:
			string: A string representing the font_color
		"""

		return self.__font_color

	def set_font_color(self, font_color):
		"""
		The method to set the value to font_color

		Parameters:
			font_color (string) : A string representing the font_color
		"""

		if font_color is not None and not isinstance(font_color, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: font_color EXPECTED TYPE: str', None, None)
		
		self.__font_color = font_color
		self.__key_modified['font_color'] = 1

	def get_opacity(self):
		"""
		The method to get the opacity

		Returns:
			float: A float representing the opacity
		"""

		return self.__opacity

	def set_opacity(self, opacity):
		"""
		The method to set the value to opacity

		Parameters:
			opacity (float) : A float representing the opacity
		"""

		if opacity is not None and not isinstance(opacity, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: opacity EXPECTED TYPE: float', None, None)
		
		self.__opacity = opacity
		self.__key_modified['opacity'] = 1

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
