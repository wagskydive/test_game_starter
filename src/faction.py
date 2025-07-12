from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List

from .npc import NPC
from .ai_behavior import Behavior, perform_behavior


class FactionGoal(Enum):
    DEFEND = "defend"
    WORK = "work"
    PARTY = "party"
    EXPLORE = "explore"


@dataclass
class Faction:
    """A simple group of NPCs with a shared goal."""

    name: str
    members: List[NPC] = field(default_factory=list)
    goal: FactionGoal = FactionGoal.DEFEND

    def add_member(self, npc: NPC) -> None:
        if npc not in self.members:
            self.members.append(npc)
            npc.join_faction(self.name)

    def remove_member(self, npc: NPC) -> None:
        if npc in self.members:
            self.members.remove(npc)
            npc.leave_faction()

    def set_goal(self, goal: FactionGoal) -> None:
        self.goal = goal

    def tick(self) -> None:
        behavior_map = {
            FactionGoal.DEFEND: Behavior.IDLE,
            FactionGoal.WORK: Behavior.WORK,
            FactionGoal.PARTY: Behavior.SOCIALIZE,
            FactionGoal.EXPLORE: Behavior.WANDER,
        }
        behavior = behavior_map[self.goal]
        for npc in self.members:
            perform_behavior(npc, behavior)
