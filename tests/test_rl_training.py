import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rl_training import RLTrainer


def test_rl_update():
    trainer = RLTrainer()
    state = (0,)
    next_state = (1,)
    trainer.update(state, action=0, reward=1.0, next_state=next_state)
    assert trainer.q_table[state][0] > 0
