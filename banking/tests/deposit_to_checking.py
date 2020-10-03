import datetime
import banking.db.models as models
from banking.logic import session  # opens db, activates logic listener <--

delete_deposit = session.query(models.CHECKINGTRANS).filter(models.CHECKINGTRANS.TransId == 100).one()
print("\ndelete checking trans, deleting row: " + str(delete_deposit) )

delete_deposit = session.query(models.CHECKINGTRANS).filter(models.CHECKINGTRANS.TransId == 100).delete()
print("\ndelete checking trans, affected: " + str(delete_deposit) + " rows")
session.commit()

trans_date = datetime.datetime(2020, 10, 1)
deposit = models.CHECKINGTRANS(TransId=100, CustNum=2, AcctNum=2, DepositAmt=1000, WithdrawlAmt=0, TransDate=trans_date)
print("\n\n - deposit checking trans: " + str(deposit))
session.add(deposit)
session.commit()

verify_deposit = session.query(models.CHECKINGTRANS).filter(models.CHECKINGTRANS.TransId == 100).one()

print("\nverify_deposit, completed: " + str(verify_deposit) + "\n\n")