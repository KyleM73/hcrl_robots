"""Configuration for Draco robots.

The following configurations are available:

* :obj:`BUMPYBOT_CFG`: HCRL Bumpybot robot with Nonholonomic controller

Reference: TODO add link to urdf etc.
"""

from __future__ import annotations
import os

import omni.isaac.orbit.sim as sim_utils
from omni.isaac.orbit.actuators import IdealPDActuatorCfg, ImplicitActuatorCfg
from omni.isaac.orbit.assets.articulation import ArticulationCfg

##
# Configuration
##

ActuatorCfg = IdealPDActuatorCfg #ImplicitActuatorCfg

BUMPYBOT_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        fix_base=True,
        merge_fixed_joints=True,
        make_instanceable=True,
        asset_path=os.path.abspath(os.path.join(os.path.dirname(__file__), "bumpybot.urdf")),
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35),
        joint_pos={".*" : 0.000},
        joint_vel={".*": 0.000},
    ),
    #soft_joint_pos_limit_factor=1.0,
    actuators={
        "prismatic": ActuatorCfg(
            joint_names_expr=["dummy_prismatic.*"],
            effort_limit=1000.0,
            velocity_limit=2.0,
            stiffness={"dummy_prismatic.*": 0}, #2e-3
            damping={"dummy_prismatic.*": 100}, #1e-5
            friction={"dummy_prismatic.*": 0.0},
        ),
         "revolute": ActuatorCfg(
            joint_names_expr=["dummy_revolute.*"],
            effort_limit=1000.0,
            velocity_limit=6.0,
            stiffness={"dummy_revolute.*": 0},
            damping={"dummy_revolute.*": 100},
            friction={"dummy_revolute.*": 0.0},
         ),
    }
)