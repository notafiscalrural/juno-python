import juno
from config import Config

Config()


result_charge = juno.charge.create(
    {
        "charge": {
            "pixKey": "74e32fdc-e201-4f99-9e32-6b42095c1f29",
            "pixIncludeImage": False,
            "description": "Cobrança Teste por PIX",
            "amount": 5.01,
            "dueDate": "2022-01-06",
            "installments": 1,
            "maxOverdueDays": 0,
            "fine": 0,
            "interest": "0.00",
            "discountAmount": "0.00",
            "discountDays": 0,
            "paymentTypes": ["BOLETO_PIX"],
            "paymentAdvance": False
        },
        "billing": {
            "name": "Teste",
            "document": "99999999909",
            "email": "teste@gmail.com",
            "address": {
                "street": "Rua 1",
                "number": "1",
                "city": "Cuiabá",
                "state": "MT",
                "postCode": "78100000"
            },
        },
    }
)

if result_charge.is_success:
    print(f"Success charge created: {result_charge.charge.id}")
    print(result_charge)
else:
    print(result_charge.errors)
