try:
    from zohosdk.src.com.zoho.dc.data_center import DataCenter

except Exception as e:
    from .data_center import DataCenter


class INDataCenter(DataCenter):

    """
    This class represents the properties of Zoho in IN Domain.
    """

    @classmethod
    def PRODUCTION(cls):

        """
        This method represents the Zoho Production environment in IN domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://www.zohoapis.in", cls().get_iam_url(), cls().get_file_upload_url(), "in_prd")

    @classmethod
    def SANDBOX(cls):

        """
        This method represents the Zoho Sandbox environment in IN domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://sandbox.zohoapis.in", cls().get_iam_url(), cls().get_file_upload_url(), "in_sdb")

    @classmethod
    def DEVELOPER(cls):

        """
        This method represents the Zoho Developer environment in IN domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://developer.zohoapis.in", cls().get_iam_url(), cls().get_file_upload_url(), "in_dev")

    def get_iam_url(self):
        return "https://accounts.zoho.in/oauth/v2/token"

    def get_file_upload_url(self):
        return "https://content.zohoapis.in"
