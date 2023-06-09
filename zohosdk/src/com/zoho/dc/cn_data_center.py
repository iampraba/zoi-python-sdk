try:
    from zohosdk.src.com.zoho.dc.data_center import DataCenter

except Exception as e:
    from .data_center import DataCenter


class CNDataCenter(DataCenter):

    """
    This class represents the properties of Zoho in CN Domain.
    """

    @classmethod
    def PRODUCTION(cls):

        """
        This method represents the Zoho Production environment in CN domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://www.zohoapis.com.cn", cls().get_iam_url(), cls().get_file_upload_url(), "cn_prd")

    @classmethod
    def SANDBOX(cls):

        """
        This method represents the Zoho Sandbox environment in CN domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://sandbox.zohoapis.com.cn", cls().get_iam_url(), cls().get_file_upload_url(), "cn_sdb")

    @classmethod
    def DEVELOPER(cls):

        """
        This method represents the Zoho Developer environment in CN domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://developer.zohoapis.com.cn", cls().get_iam_url(), cls().get_file_upload_url(), "cn_dev")

    def get_iam_url(self):
        return "https://accounts.zoho.com.cn/oauth/v2/token"

    def get_file_upload_url(self):
        return "https://content.zohoapis.com.cn"
