# NPC Needs System

`NPC` objects now track rest, safety, social and status. The `tick` method
reduces these values over time and `satisfy()` can replenish them.
