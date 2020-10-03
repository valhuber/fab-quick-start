import os
import sys
from datetime import datetime

import banking.db.models as models
from banking.logic import session  # opens db, activates logic listener <--
from logic_bank.exec_row_logic.logic_row import LogicRow

cwd = os.getcwd()   # eg, /Users/val/python/pycharm/logic-bank/nw/tests
required_path_python_rules = cwd  # seeking /Users/val/python/pycharm/Logic-Bank
required_path_python_rules = required_path_python_rules.replace("/banking/tests", "")
required_path_python_rules = required_path_python_rules.replace("\banking\tests", "")

sys_path = ""
required_path_present = False
for each_node in sys.path:
    sys_path += each_node + "\n"
    if each_node == required_path_python_rules:
        required_path_present = True

if not required_path_present:
    print("Fixing path (so can run from terminal)")
    sys.path.append(required_path_python_rules)
else:
    pass
    print("NOT Fixing path (default PyCharm, set in VSC Launch Config)")

path_info = "Run Environment info...\n\n"\
            + "Current Working Directory: " + cwd + "\n\n"\
            + "sys.path: (Python imports)\n" + sys_path + "\n"\
            + "From: " + sys.argv[0] + "\n\n"\
            + "Using Python: " + sys.version + "\n\n"\
            + "At: " + str(datetime.now()) + "\n\n"
print("\n" + path_info + "\n\n")

pre_cust = session.query(models.CUSTOMER).filter(models.CUSTOMER.CustNum == 1).one()
session.expunge(pre_cust)

"""
    ********* Customer Account Deposit Checking Setup - Deposit $100 to CHECKINGTRANS *********
"""

trans_date = datetime(2020, 10, 1)
deposit = models.CHECKINGTRANS(TransId=1, CustNum=1, AcctNum=1,
                               DepositAmt=100, WithdrawlAmt=0, TransDate=trans_date)
print("\n\nCustomer Account Deposit Checking Setup - Deposit $100 to CHECKINGTRANS: " + str(deposit))
session.add(deposit)
session.commit()

verify_cust = session.query(models.CUSTOMER).filter(models.CUSTOMER.CustNum == 1).one()
logic_row = LogicRow(row=verify_cust, old_row=pre_cust, ins_upd_dlt="*", nest_level=0, a_session=session, row_sets=None)
if verify_cust.TotalBalance == 100.0:
    logic_row.log("Customer Account Deposit Checking Setup OK - balance is 100")
    assert True
else:
    logic_row.log("Customer Account Deposit Checking Setup OK fails - balance not 100")
    assert False
session.expunge(verify_cust)

"""
    ********* Transfer 10 from checking to savings *********
"""
trasfer = models.TRANSFERFUND(TransId=2, FromCustNum=1, FromAcct=1, ToCustNum=1, ToAcct=1, TransferAmt=10, TransDate=trans_date)
session.add(trasfer)
session.commit()

print("\ncust should still have 100 in TotalBalance completed: " + str(verify_cust.TotalBalance) + "\n\n")
#print("\ncust should still have 10 in Savings completed: " + str(verify_cust.SavingAcctBal) + "\n\n")
verify_cust = session.query(models.CUSTOMER).filter(models.CUSTOMER.CustNum == 1).one()
logic_row = LogicRow(row=verify_cust, old_row=pre_cust, ins_upd_dlt="*", nest_level=0, a_session=session, row_sets=None)
if verify_cust.TotalBalance == 100.0:
    logic_row.log("Transfer 10 from checking to savings ok - balance is 100")
    assert True
else:
    logic_row.log("Transfer 10 from checking to savings fails - balance not 100")
    assert False
session.expunge(verify_cust)

"""
    ********* Overdraft Funds Test *********
"""

print("SHOULD FAIL")
trasfer2 = models.TRANSFERFUND(TransId=3, FromCustNum=1, FromAcct=1, ToCustNum=1, ToAcct=1, TransferAmt=1000, TransDate=trans_date)
session.add(trasfer2)
did_fail_as_expected = False
try:
    session.commit()
except:
    session.rollback()
    did_fail_as_expected = True

verify_cust = session.query(models.CUSTOMER).filter(models.CUSTOMER.CustNum == 1).one()
logic_row = LogicRow(row=verify_cust, old_row=pre_cust, ins_upd_dlt="*", nest_level=0, a_session=session, row_sets=None)

if not did_fail_as_expected:
    logic_row.log("ERROR -overdraft checking expected to fail, but succeeded")
    assert False
else:
    logic_row.log("Overdraft Funds Test rolled back transfer")
