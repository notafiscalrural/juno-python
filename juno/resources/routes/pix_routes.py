from ..handler_request import get_resource_url


def get_base_url():
    return f"{get_resource_url()}/pix"


def create_keys():
    return f"{get_base_url()}/keys"


def qrcodes_static():
    return f"{get_base_url()}/qrcodes/static"
