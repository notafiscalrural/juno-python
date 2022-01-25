import juno
from config import Config

Config()


"""
Gerar o hash do cartão com o juno.html
Pegar o hash no console.log

"""


result_charge = juno.charge.create(
    {
        "charge": {
            "description": "Cobrança Cartão de Crédito",
            "amount": "1.02",
            "references": [""],
            "payment_types": ["CREDIT_CARD"],
        },
        "billing": {
            "name": "Teste",
            "document": "99999999909",
        },
    }
)

if result_charge.is_success:
    print(f"Success charge created: {result_charge.charge.id}")

    result_payment = juno.payment.create(
        {
            "charge_id": result_charge.charge.id,
            "billing": {
                "email": "teste@gmail.com",
                "address": {
                    "street": "Rua 1",
                    "number": "1",
                    "city": "Cuiabá",
                    "state": "MT",
                    "postCode": "78100000"
                },
                "delayed": False,  # for capture delayed, use: "delayed": True
            },
            "credit_card_details": {"credit_card_hash": "4ff60a3a-23b0-4104-b8c6-801d430e820a"},
        }
    )

    if result_payment.is_success:
        print(f"Success payment: {result_payment.payment.id}")
    else:
        print(result_payment.errors)
else:
    print(result_charge.errors)
