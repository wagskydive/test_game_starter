from collections import defaultdict
from typing import Tuple, Dict, List

class RLTrainer:
    """Simple Q-learning trainer for NPC behaviors."""

    def __init__(self) -> None:
        # q_table[state][action] -> value
        self.q_table: Dict[Tuple, List[float]] = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])

    def update(
        self,
        state: Tuple,
        action: int,
        reward: float,
        next_state: Tuple,
        alpha: float = 0.1,
        gamma: float = 0.9,
    ) -> None:
        """Update Q-value for a state-action pair."""
        best_next = max(self.q_table[next_state])
        current = self.q_table[state][action]
        self.q_table[state][action] = current + alpha * (
            reward + gamma * best_next - current
        )
