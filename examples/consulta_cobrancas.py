import juno
from config import Config

Config()


# todos
find_all_charges = juno.charge.find_all()
print(find_all_charges)

# todos somente pagos
find_all_charges = juno.charge.find_all(
    dictionary={
        "showPaid": True,
    }
)
print(find_all_charges)

# cobrança sem pagamento
find_charge_by_id = juno.charge.find_by_id('chr_4B37A1D1A9EA696B714CF015019BF33E')
print(f"id={find_charge_by_id.charge.id} status={find_charge_by_id.charge.status}")
if find_charge_by_id.charge.status == 'PAID':
    print(f"status={find_charge_by_id.charge.payments[0].status}")
    print(f"pagamento={find_charge_by_id.charge.payments[0].release_date}")
    print(f"valor pago={find_charge_by_id.charge.payments[0].amount}")

# pagamento feito
find_charge_by_id = juno.charge.find_by_id('chr_A2D459BF1AD077204838B949FC6B5EFA')
print(f"id={find_charge_by_id.charge.id} status={find_charge_by_id.charge.status}")
if find_charge_by_id.charge.status == 'PAID':
    print(f"status={find_charge_by_id.charge.payments[0].status}")
    print(f"pagamento={find_charge_by_id.charge.payments[0].release_date}")
    print(f"valor pago={find_charge_by_id.charge.payments[0].amount}")

# pagamento não autorizado por cartão de crédito
find_charge_by_id = juno.charge.find_by_id('chr_DD789E5BF904DB172D49AC9A8458B194')
print(f"id={find_charge_by_id.charge.id} status={find_charge_by_id.charge.status}")
if find_charge_by_id.charge.status == 'PAID':
    print(f"status={find_charge_by_id.charge.payments[0].status}")
    print(f"pagamento={find_charge_by_id.charge.payments[0].release_date}")
    print(f"valor pago={find_charge_by_id.charge.payments[0].amount}")
