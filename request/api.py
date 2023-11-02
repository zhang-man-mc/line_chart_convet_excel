from request.dust_url import UrlConfig
from request.request import request_post


def fetch_site_data(data):
    """获取监测站点数据

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    return request_post(UrlConfig.url_site_data, data)
