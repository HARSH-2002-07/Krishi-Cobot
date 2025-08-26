from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='ebot_navigation', executable='ebot_node', output='screen')
    ])
