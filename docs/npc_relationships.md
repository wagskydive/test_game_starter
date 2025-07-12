# NPC Families and Relationships

NPCs can track family ties and friendships using new helper methods:

```python
from npc import NPC

alice = NPC(name="Alice")
charlie = NPC(name="Charlie")

alice.add_child(charlie)
```

`add_child()` and `add_parent()` automatically link both NPCs. Use `befriend()`
and `unfriend()` to manage social bonds. Relationship sets prevent duplicates
and hold direct references to other `NPC` objects.
