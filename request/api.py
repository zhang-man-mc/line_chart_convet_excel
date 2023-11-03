from request.dust_url import UrlConfig
from request.request import request_post


def fetch_data(params: dict):
    """获取目标数据

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    return request_post(UrlConfig.url_site_data, params)
