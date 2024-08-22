from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
    Node(
        package = "my_project_01",
        executable = "publisher.py",
        name = "rpm_pub_node",
        parameters = [{"RPM":40}]
        ),
    Node(
    package = "my_project_01",
    executable = "subscriber.py",
    name = "speed_sub_node",
    parameters = [{"Wheel_Diameter":0.5}],
    output = "screen"
        ),
    ExecuteProcess(
        cmd = ['ros2','topic','echo','/speed'],
        output = 'screen'
    ),

    ])