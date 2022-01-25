import juno
from config import Config

Config()


result_plan = juno.plan.create(
    {
        "name": "Plano Mensal",
        "amount": 50.01,
    }
)

if result_plan.is_success:
    print("Success plan created")
    print(result_plan)
else:
    print(result_plan.errors)

print(juno.plan.find_all())
print(juno.plan.find_by_id('pln_77449A963CFDB13F'))
print(juno.plan.deactivation('pln_77449A963CFDB13F'))
print(juno.plan.activation('pln_77449A963CFDB13F'))
