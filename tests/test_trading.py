import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.npc import NPC
from src.item import Item
from src.trading import trade


def test_trade_success():
    buyer = NPC(name='Alice', money=10)
    seller = NPC(name='Bob', money=0)
    item = Item(name='apple', weight=1.0)
    seller.inventory.add(item)

    assert trade(buyer, seller, item, 5)
    assert item in buyer.inventory.items
    assert buyer.money == 5
    assert seller.money == 5


def test_trade_insufficient_funds():
    buyer = NPC(name='Alice', money=3)
    seller = NPC(name='Bob', money=0)
    item = Item(name='apple', weight=1.0)
    seller.inventory.add(item)

    assert not trade(buyer, seller, item, 5)
    assert item in seller.inventory.items
    assert buyer.money == 3
    assert seller.money == 0
