'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal, getcontext

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_AMOUNT = 1000000
MIN_ORDER_QUANTITY = 0
MAX_ORDER_QUANTITY = 100

def validorder(order: Order):
    costs = Decimal(0)
    paid = Decimal(0)

    for item in order.items:
        if item.type == 'payment':
            paid += Decimal(str(item.amount))
        elif item.type == 'product':
            if type(item.quantity) is int and MIN_ORDER_QUANTITY < item.quantity <= MAX_ORDER_QUANTITY:
                costs += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if paid >= MAX_AMOUNT or costs >= MAX_AMOUNT:
        return "Total amount payable for an order exceeded"

    if costs != paid:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, float(paid - costs))
    else:
        return "Order ID: %s - Full payment received!" % order.id