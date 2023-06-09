try:
    import re
    from zohosdk.src.com.zoho.exception.sdk_exception import SDKException
    from zohosdk.src.com.zoho.util.constants import Constants

except Exception:
    import re
    from zohosdk.src.com.zoho.exception.sdk_exception import SDKException
    from .util.constants import Constants


class UserSignature(object):

    """
    This class represents the Zoho User.
    """

    def __init__(self, email):

        """
        Creates an UserSignature class instance with the specified user email.

        Parameters:
            email (str) : A string containing the user email
        """

        error = {}

        if re.fullmatch(Constants.EMAIL_REGEX, email) is None:
            error[Constants.FIELD] = Constants.EMAIL
            error[Constants.EXPECTED_TYPE] = Constants.EMAIL

            raise SDKException(Constants.USER_SIGNATURE_ERROR, details=error)

        self.__email = email

    def get_email(self):
        """
        This is a getter method to get __email.

        Returns:
            string: A string representing __email
        """

        return self.__email
