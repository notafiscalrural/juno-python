import juno
from config import Config

Config()


token_id = juno.card.tokenization(
    {"creditCardHash": "a78a6abb-aea9-493b-a955-8f221d234320"}
)

print(f"token_id={token_id}")
print(f"credit_card_id={token_id.credit_card_id}")
print(f"last4_card_number={token_id.last4_card_number}")
print(f"expiration_month={token_id.expiration_month}")
print(f"expiration_year={token_id.expiration_year}")

"""
credit_card_id=d2e6e202-4def-458a-98a8-38adf6098e7f
last4_card_number=4502
expiration_month=1
expiration_year=2030
"""
