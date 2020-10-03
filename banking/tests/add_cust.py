import banking.db.models as models
from banking.logic import session  # opens db, activates logic listener <--

# first delete, so can add
delete_cust = session.query(models.CUSTOMER).filter(models.CUSTOMER.CustNum == 2).delete()
print("\nadd_cust, deleting: " + str(delete_cust) + "\n\n")
session.commit()

# Add a Customer - works
new_cust = models.CUSTOMER(CustNum=2, Name='Tyler', City='Ormond', Street='123 main', State='FL', CheckingAcctBal=0, SavingsAcctBal=0)
session.add(new_cust)
session.commit()

verify_cust = session.query(models.CUSTOMER).filter(models.CUSTOMER.CustNum == 2).one()

print("\nadd_cust, completed: " + str(verify_cust) + "\n\n")

assert True
