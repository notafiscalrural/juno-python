import juno
from config import Config

Config()


result_subscription = juno.subscription.create(
    {}
)

if result_subscription.is_success:
    print("Success subscription created")
    print(result_subscription)
else:
    print(result_subscription.errors)

print(juno.subscription.find_all())
print(juno.subscription.find_by_id('pln_77449A963CFDB13F'))
print(juno.subscription.deactivation('pln_77449A963CFDB13F'))
print(juno.subscription.activation('pln_77449A963CFDB13F'))
print(juno.subscription.cancelation('pln_77449A963CFDB13F'))
