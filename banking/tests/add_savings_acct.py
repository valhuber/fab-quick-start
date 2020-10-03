import banking.db.models as models
from banking.logic import session  # opens db, activates logic listener <--

# first delete, so can add
delete_savings = session.query(models.SAVING).filter(models.SAVING.CustNum == 2).delete()
print("\ndelete savings, deleting: " + str(delete_savings) + "\n\n")
session.commit()

new_savings = models.SAVING(CustNum=2, AcctNum=3, Deposits=0, Withdrawls=0, AvailableBalance=0, ItemCount=0, AcctType='S')
session.add(new_savings)
session.commit()

verify_savings = session.query(models.SAVING).filter(models.CHECKING.AcctNum == 3).one()

print("\nverify_savings, completed: " + str(verify_savings) + "\n\n")

