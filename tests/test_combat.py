import os, sys
sys.path.insert(0, os.path.abspath('src'))

from item import Item
from npc import NPC
import combat


def test_melee_attack_hits(monkeypatch):
    attacker = NPC(name='Attacker')
    defender = NPC(name='Defender')
    weapon = Item(name='sword', weight=5.0, durability=10)

    monkeypatch.setattr(combat.random, 'random', lambda: 0.0)
    hit = combat.melee_attack(attacker, defender, weapon)

    assert hit
    assert defender.health == 95  # damage 5
    assert weapon.durability == 9


def test_melee_attack_misses(monkeypatch):
    attacker = NPC(name='Attacker')
    defender = NPC(name='Defender')
    weapon = Item(name='sword', weight=5.0, durability=10)

    monkeypatch.setattr(combat.random, 'random', lambda: 0.99)
    hit = combat.melee_attack(attacker, defender, weapon, hit_chance=0.5)

    assert not hit
    assert defender.health == 100
    assert weapon.durability == 10


def test_ranged_attack(monkeypatch):
    attacker = NPC(name='Attacker')
    defender = NPC(name='Defender')
    bow = Item(name='bow', weight=2.0, durability=5)

    monkeypatch.setattr(combat.random, 'random', lambda: 0.1)
    hit = combat.ranged_attack(attacker, defender, bow)

    assert hit
    assert defender.health == 98  # damage 2
    assert bow.durability == 4
