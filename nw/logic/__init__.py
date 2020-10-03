import os
from shutil import copyfile

import sqlalchemy
from sqlalchemy import event
from sqlalchemy.orm import session

from logic_bank.rule_bank import rule_bank_withdraw  # FIXME design why required to avoid circular imports??
from logic_bank.rule_bank import rule_bank_setup
from nw.logic.rules_bank import activate_basic_check_credit_rules

from nw.logic.legacy.order_code import order_commit_dirty, order_flush_dirty, order_flush_new, order_flush_delete
from nw.logic.legacy.order_detail_code import order_detail_flush_new, order_detail_flush_delete

from logic_bank.util import prt

# from nw.logic.models import Order

'''
These listeners are part of the legacy, hand-coded logic alternative
(Not required in a rules-based approach)
'''


def nw_before_commit(a_session: session):
    print("logic: before commit!")
    # for obj in versioned_objects(a_session.dirty):
    for obj in a_session.dirty:
        print("logic: before commit! --> " + str(obj))
        obj_class = obj.__tablename__
        if obj_class == "Order":
            order_commit_dirty(obj, a_session)
        elif obj_class == "OrderDetail":
            print("Stub")
    print("logic called: before commit!  EXIT")


def nw_before_flush(a_session: session, a_flush_context, an_instances):
    print("nw_before_flush")
    for each_instance in a_session.dirty:
        print("nw_before_flush flushing Dirty! --> " + str(each_instance))
        obj_class = each_instance.__tablename__
        if obj_class == "Order":
            order_flush_dirty(each_instance, a_session)
        elif obj_class == "OrderDetail":
            print("Stub")

    for each_instance in a_session.new:
        print("nw_before_flush flushing New! --> " + str(each_instance))
        obj_class = each_instance.__tablename__
        if obj_class == "OrderDetail":
            order_detail_flush_new(each_instance, a_session)
        elif obj_class == "Order":
            order_flush_new(each_instance, a_session)

    for each_instance in a_session.deleted:
        print("nw_before_flush flushing New! --> " + str(each_instance))
        obj_class = each_instance.__tablename__
        if obj_class == "OrderDetail":
            order_detail_flush_delete(each_instance, a_session)
        elif obj_class == "Order":
            order_flush_delete(each_instance, a_session)

    print("nw_before_flush  EXIT")


""" Initialization
1 - Connect
2 - Register listeners (either hand-coded ones above, or the logic-engine listeners).
"""

print("\n" + prt("nw/logic/__init__.py BEGIN - setup logging, connect to db, register listeners\n"))

# Initialize Logging
import logging
import sys

logic_logger = logging.getLogger('logic_logger')  # for debugging user logic
logic_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s - %(asctime)s - %(name)s - %(levelname)s')
handler.setFormatter(formatter)
logic_logger.addHandler(handler)

do_engine_logging = False
engine_logger = logging.getLogger('engine_logger')  # for internals
if do_engine_logging:
    engine_logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s - %(asctime)s - %(name)s - %(levelname)s')
    handler.setFormatter(formatter)
    engine_logger.addHandler(handler)

basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.dirname(basedir)

print("\n****************\n"
      "  IMPORTANT - create database.db from database-gold.db in " + basedir + "/nw/db/" +
      "\n****************")

nw_loc = os.path.join(basedir, "db/database.db")
nw_source = os.path.join(basedir, "db/database-gold.db")
copyfile(src=nw_source, dst=nw_loc)

conn_string = "sqlite:///" + nw_loc
engine = sqlalchemy.create_engine(conn_string, echo=False)  # sqlalchemy sqls...

session_maker = sqlalchemy.orm.sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

by_rules = True  # True => use rules, False => use hand code (for comparison)
rule_list = None
db = None
if by_rules:
    rule_bank_setup.setup(session, engine)
    activate_basic_check_credit_rules()
    rule_bank_setup.validate(session, engine)  # checks for cycles, etc
else:
    # setup to illustrate hand-coding alternative - target, modifier, function
    event.listen(session, "before_commit", nw_before_commit)
    event.listen(session, "before_flush", nw_before_flush)

print("\n" + prt("nw/logic/__init__.py END - connected, session created, listeners registered\n"))
