# Copyright (c) 2025 Intelligent Robotics Lab (URJC)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

  bringup_dir = get_package_share_directory('easynav_indoor_testcase')

  namespace = LaunchConfiguration('namespace')
  params_file = LaunchConfiguration('params_file')

  declare_namespace_cmd = DeclareLaunchArgument(
        'namespace',
        default_value='',
  )
  declare_params_file_cmd = DeclareLaunchArgument(
        'params_file',
        default_value=os.path.join(bringup_dir, 'robots_params', 'costmap_multirobot.params.yaml'),
    )

  easynav_system_cmd = Node(
    package='easynav_system',
    executable='system_main',
    namespace=namespace,
    parameters=[
      params_file
    ],
    remappings=[
            ('/tf', 'tf'),
            ('/tf_static', 'tf_static'),
        ],
  )

  ld = LaunchDescription()
  ld.add_action(declare_namespace_cmd)
  ld.add_action(declare_params_file_cmd)
  ld.add_action(easynav_system_cmd)

  return ld

