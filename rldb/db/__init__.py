from .paper__deep_recurrent_q_learning_for_partially_observable_mdps import entries as drqn_entries
from .paper__deep_reinforcement_learning_with_double_q_learning import entries as ddqn_entries
from .paper__dueling_network_architectures_for_deep_reinforcement_learning import entries as dueling_entries
from .paper__exploration_by_random_network_distillation import entries as rnd_entries
from .paper__playing_atari_with_deep_reinforcement_learning import entries as dqn2013_entries
from .paper__prioritized_experience_replay import entries as per_entries
from .paper__proximal_policy_optimization_algorithms import entries as ppo_entries
from .paper__trust_region_policy_optimization import entries as trpo_entries

entries = (
    []
    + drqn_entries
    + ddqn_entries
    + dueling_entries
    + rnd_entries
    + dqn2013_entries
    + per_entries
    + ppo_entries
    + trpo_entries
)

assert len(entries) == (
    0
    + 18   # DRQN
    + 375  # DDQN
    + 456  # Dueling DQN
    + 18   # RND
    + 56   # DQN2013
    + 334  # PER
    + 147  # PPO
    + 35   # TRPO
)
