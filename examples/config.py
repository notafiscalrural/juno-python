import juno


class Config:

    def __init__(self):
        juno.init(
            client_id="my client_id",
            client_secret="my client_secret",
            resource_token="my resource_token",
            idempotency_key="my idempotency_key",
            sandbox=True,
        )
