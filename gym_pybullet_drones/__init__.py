from gymnasium.envs.registration import register

register(
    id='gym_pybullet_drones/ctrl-aviary-v0',
    entry_point='gym_pybullet_drones.envs:CtrlAviary',
)

register(
    id='gym_pybullet_drones/velocity-aviary-v0',
    entry_point='gym_pybullet_drones.envs:VelocityAviary',
)

register(
    id='gym_pybullet_drones/hover-aviary-v0',
    entry_point='gym_pybullet_drones.envs:HoverAviary',
)

register(
    id='gym_pybullet_drones/multihover-aviary-v0',
    entry_point='gym_pybullet_drones.envs:MultiHoverAviary',
)
