try:
	from zohosdk.src.com.zoho.exception import SDKException
	from zohosdk.src.com.zoho.util import Constants
except Exception:
	from ...exception import SDKException
	from ...util import Constants


class FillableFormOptions(object):
	def __init__(self):
		"""Creates an instance of FillableFormOptions"""

		self.__download = None
		self.__print = None
		self.__submit = None
		self.__key_modified = dict()

	def get_download(self):
		"""
		The method to get the download

		Returns:
			bool: A bool representing the download
		"""

		return self.__download

	def set_download(self, download):
		"""
		The method to set the value to download

		Parameters:
			download (bool) : A bool representing the download
		"""

		if download is not None and not isinstance(download, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: download EXPECTED TYPE: bool', None, None)
		
		self.__download = download
		self.__key_modified['download'] = 1

	def get_print(self):
		"""
		The method to get the print

		Returns:
			bool: A bool representing the print
		"""

		return self.__print

	def set_print(self, print):
		"""
		The method to set the value to print

		Parameters:
			print (bool) : A bool representing the print
		"""

		if print is not None and not isinstance(print, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: print EXPECTED TYPE: bool', None, None)
		
		self.__print = print
		self.__key_modified['print'] = 1

	def get_submit(self):
		"""
		The method to get the submit

		Returns:
			bool: A bool representing the submit
		"""

		return self.__submit

	def set_submit(self, submit):
		"""
		The method to set the value to submit

		Parameters:
			submit (bool) : A bool representing the submit
		"""

		if submit is not None and not isinstance(submit, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: submit EXPECTED TYPE: bool', None, None)
		
		self.__submit = submit
		self.__key_modified['submit'] = 1

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
