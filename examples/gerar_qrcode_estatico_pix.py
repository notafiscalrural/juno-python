import juno
from config import Config

Config()


result_pix = juno.pix.qrcodes_static(
    {
        "includeImage": True,
        "key": "pix_key",
        "amount": 5.05,
        "reference": "",
        "additionalData": ""
    }
)

if result_pix.is_success:
    print("Pix qrcode static image created")
    print(result_pix)
else:
    print(result_pix.errors)
