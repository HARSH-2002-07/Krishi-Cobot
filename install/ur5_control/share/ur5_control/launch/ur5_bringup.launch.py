from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='ur5_control', executable='ur5_node', output='screen')
    ])
