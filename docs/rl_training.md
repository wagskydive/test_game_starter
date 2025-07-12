# RL Training Prototype

`rl_training.RLTrainer` implements a minimal Q-learning update used to prototype
reinforcement learning behaviors for NPCs.

```python
from rl_training import RLTrainer

trainer = RLTrainer()
state = (0,)
next_state = (1,)
trainer.update(state, action=0, reward=1.0, next_state=next_state)
```

The trainer stores a `q_table` dictionary mapping states to action values.
