import banking.db.models as models
from banking.logic import session  # opens db, activates logic listener <--

# first delete, so can add
delete_checking = session.query(models.CHECKING).filter(models.CHECKING.CustNum == 2).delete()
print("\ndelete checking, deleting: " + str(delete_checking) + "\n\n")
session.commit()

new_checking = models.CHECKING(CustNum=2, AcctNum=2, Deposits=0, Withdrawls=0, AvailableBalance=0, ItemCount=0, CreditCode=1, AcctType='C')
session.add(new_checking)
session.commit()

verify_checking = session.query(models.CHECKING).filter(models.CHECKING.AcctNum == 2).one()

print("\nverify_checking, completed: " + str(verify_checking) + "\n\n")

