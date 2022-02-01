from juno.resources import handler_request
from juno.resources.routes import pix_routes


def create_keys(dictionary):
    return handler_request.post(pix_routes.create_keys(), dictionary)


def qrcodes_static(dictionary):
    return handler_request.get(f"{pix_routes.get_base_url()}/qrcodes/static", dictionary)
