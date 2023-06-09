try:
    from zohosdk.src.com.zoho.dc.data_center import DataCenter

except Exception as e:
    from .data_center import DataCenter


class USDataCenter(DataCenter):

    """
    This class represents the properties of Zoho in US Domain.
    """

    @classmethod
    def PRODUCTION(cls):

        """
        This method represents the Zoho Production environment in US domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://www.zohoapis.com", cls().get_iam_url(), cls().get_file_upload_url(), "us_prd")

    @classmethod
    def SANDBOX(cls):

        """
        This method represents the Zoho Sandbox environment in US domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://sandbox.zohoapis.com", cls().get_iam_url(), cls().get_file_upload_url(), "us_sdb")

    @classmethod
    def DEVELOPER(cls):

        """
        This method represents the Zoho Developer environment in US domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://developer.zohoapis.com", cls().get_iam_url(), cls().get_file_upload_url(), "us_dev")

    def get_iam_url(self):
        return "https://accounts.zoho.com/oauth/v2/token"

    def get_file_upload_url(self):
        return "https://content.zohoapis.com"
