from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

'''def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('gui', default_value='true',
                              description='Set to "false" to run headless.'),

        DeclareLaunchArgument('server', default_value='true',
                              description='Set to "false" not to run gzserver.'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/gzserver.launch.py']),
            condition=IfCondition(LaunchConfiguration('server'))
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/gzclient.launch.py']),
            condition=IfCondition(LaunchConfiguration('gui'))
        ),
    ])'''

'''def generate_launch_description():
    ld = LaunchDescription()

    gzb_pkg = get_package_share_directory("gazebo_ros")

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            
    )

    talker_node = Node(
        package="demo_nodes_cpp",
        executable="talker",
    )

    listener_node = Node(
        package="demo_nodes_py",
        executable="listener"
    )

    ld.add_action(talker_node)
    ld.add_action(listener_node)

    return ld'''

def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
            )
        )
    ])