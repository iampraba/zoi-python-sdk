try:
    from zohosdk.src.com.zoho.dc.data_center import DataCenter

except Exception as e:
    from .data_center import DataCenter


class EUDataCenter(DataCenter):

    """
    This class represents the properties of Zoho in EU Domain.
    """

    @classmethod
    def PRODUCTION(cls):

        """
        This method represents the Zoho Production environment in EU domain
        :return: An instance of Environments
        """

        return DataCenter.Environment("https://www.zohoapis.eu", cls().get_iam_url(), cls().get_file_upload_url(), "eu_prd")

    @classmethod
    def SANDBOX(cls):

        """
        This method represents the Zoho Sandbox environment in EU domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://sandbox.zohoapis.eu", cls().get_iam_url(), cls().get_file_upload_url(), "eu_sdb")

    @classmethod
    def DEVELOPER(cls):

        """
        This method represents the Zoho Developer environment in EU domain
        :return:  An instance of Environment
        """

        return DataCenter.Environment("https://developer.zohoapis.eu", cls().get_iam_url(), cls().get_file_upload_url(), "eu_dev")

    def get_iam_url(self):
        return "https://accounts.zoho.eu/oauth/v2/token"

    def get_file_upload_url(self):
        return "https://content.zohoapis.eu"
