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
        fix_base=False,
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
        pos=(0.0, 0.0, 0.4),
        joint_pos={".*" : 0.000},
        joint_vel={".*": 0.000},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "planar": ActuatorCfg(
            joint_names_expr=["dummy_x_joint", "dummy_y_joint"],
            effort_limit=10.0,
            velocity_limit=100.0,
            stiffness={"dummy_.*": 20.0},
            damping={"dummy_.*": 1.0},
            friction={"dummy_.*": 0.0},
        ),
         "yaw": ActuatorCfg(
            joint_names_expr=["dummy_yaw_joint"],
            effort_limit=10.0,
            velocity_limit=100.0,
            stiffness={"dummy_.*": 20.0},
            damping={"dummy_.*": 1.0},
            friction={"dummy_.*": 0.0},
         ),
    }
)
"""
Ordered Joints:
0:  'l_hip_ie',
1:  'l_shoulder_fe',
2:  'neck_pitch',
3:  'r_hip_ie',
4:  'r_shoulder_fe',
5:  'l_hip_aa',
6:  'l_shoulder_aa',
7:  'r_hip_aa',
8:  'r_shoulder_aa',
9:  'l_hip_fe',
10: 'l_shoulder_ie',
11: 'r_hip_fe',
12: 'r_shoulder_ie',
13: 'l_knee_fe_jp',
14: 'l_elbow_fe',
15: 'r_knee_fe_jp',
16: 'r_elbow_fe',
17: 'l_knee_fe_jd',
18: 'l_wrist_ps',
19: 'r_knee_fe_jd',
20: 'r_wrist_ps',
21: 'l_ankle_fe',
22: 'l_wrist_pitch',
23: 'r_ankle_fe',
24: 'r_wrist_pitch',
25: 'l_ankle_ie',
26: 'r_ankle_ie']
"""