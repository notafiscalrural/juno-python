import juno
from config import Config

Config()


result_charge = juno.charge.create(
    {
        "charge": {
            "description": "Validar Cartão",
            "amount": "1.00",
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
                    "postCode": "78000000"
                },
                "delayed": False,  # for capture delayed, use: "delayed": True
            },
            "credit_card_details": {"credit_card_hash": "c588062c-7be0-42d9-9459-fbb7101e2ba5"},
        }
    )

    if result_payment.is_success:
        refund_payment = juno.payment.refund(
            result_payment.payment.id, {"amount": "1.00"}
        )
        if refund_payment.is_success:
            print(f"Success payment refund: {refund_payment.refunds}")
            print(f"Success payment refund id: {refund_payment.refunds[0]['id']}")
            print(f"Success payment refund status: {refund_payment.refunds[0]['status']}")
            print(f"Success payment refund paybackDate: {refund_payment.refunds[0]['payback_date']}")
        else:
            print(f"refund_payment errors={refund_payment.errors}")
    else:
        print(f"result_payment errors={result_payment.errors}")
else:
    print(f"result_charge errors={result_charge.errors}")
