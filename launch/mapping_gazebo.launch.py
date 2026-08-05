import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package_share = get_package_share_directory('fast_livo')
    use_rviz = LaunchConfiguration('rviz')
    return LaunchDescription([
        DeclareLaunchArgument('rviz', default_value='False'),
        Node(
            package='fast_livo',
            executable='fastlivo_mapping',
            name='laserMapping',
            output='screen',
            parameters=[
                os.path.join(package_share, 'config', 'fast_livo_gazebo.yaml'),
                os.path.join(package_share, 'config', 'camera_gazebo.yaml'),
                {'use_sim_time': True},
            ],
        ),
        Node(
            condition=IfCondition(use_rviz),
            package='rviz2',
            executable='rviz2',
            name='fast_livo_rviz',
            output='screen',
            arguments=[
                '-d', os.path.join(package_share, 'rviz_cfg', 'fast_livo2.rviz')
            ],
            parameters=[{'use_sim_time': True}],
        ),
    ])
