import juno
from config import Config

Config()


result_pix = juno.pix.create_keys(
    {
        "type": "RANDOM_KEY"
    }
)

if result_pix.is_success:
    print("Pix key created")
    print(result_pix)
else:
    print(result_pix.errors)


"""
Response:
{
    "key": "77c1f1ce-683b-4f77-a03b-271dea91cdfb",
    "creationDateTime": "2022-01-25T10:38:02.287-03:00",
    "ownershipDateTime": "2022-01-25T10:38:02.287-03:00"
}
"""
