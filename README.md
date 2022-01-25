## Juno Python Library

The Juno Python library provides integration access to the Juno Gateway.

## Installing

To install, use:

```sh
$ pip install https://github.com/notafiscalrural/juno-python/archive/main.zip
```


## Documentation

* [API Guide](https://dev.juno.com.br/api/)

## Quick Start Example

```python
import juno

juno.init(
    client_id="CLIENT_ID_JUNO",
    client_secret="CLIENT_SECRET_JUNO",
    resource_token="RESOURCE_TOKEN_JUNO",
    idempotency_key="IDEMPOTENCY_KEY",  # only for create pix routes
    sandbox=False,
)

result_charge = juno.charge.create(
    {
        "charge": {
            "description": "Description",
            "amount": "100.00",
            "references": [""],
            "payment_types": ["CREDIT_CARD"],
        },
        "billing": {
            "name": "Name Test",
            "document": "00000000000",  # Add a valid CPF
        },
    }
)

if result_charge.is_success:
    result_payment = juno.payment.create(
        {
            "charge_id": result_charge.charge.id,
            "billing": {
                "email": "name@test.com",  # Add a valid email
                "address": {  # Add a valid address
                    "street": "",
                    "number": "",
                    "complement": "",
                    "neighborhood": "",
                    "city": "",
                    "state": "",
                    "post_code": "",
                },
                "delayed": False,  # for capture delayed, use: "delayed": True
            },
            # if card is attached: "credit_card_details": {"credit_card_id": "id"}
            "credit_card_details": {"credit_card_hash": "hash"},
        }
    )

    if result_payment.is_success:
        print(f"Success payment: {result_payment.payment.id}")
    else:
        print(result_payment.errors)
else:
    print(result_charge.errors)
```

### Capture Delayed
```python
# ...
juno.payment.capture(result_payment.payment.id, {"charge_id": result_charge.charge.id, "amount": "100.00"})
```

## Support
If you have any problem or suggestion please open an issue [here](https://github.com/notafiscalrural/juno-python/issues).

## License

Check [here](LICENSE).
