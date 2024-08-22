#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import Int32, Float32

RPM_DEFAULT = 20

class RPMPubNode(Node):
    def __init__(self):
        super().__init__("rpm_pub_node")
        self.declare_parameter("RPM", RPM_DEFAULT)
        self.pub = self.create_publisher(Int32, "rpm", 10)
        self.timer = self.create_timer(0.5, self.publish_rpm) 

    
    def publish_rpm(self):
        rpm_param = self.get_parameter("RPM").get_parameter_value().integer_value
        msg = Int32()
        msg.data = rpm_param
        self.pub.publish(msg)


def main(args=None):
    rclpy.init()      # Initializes the ROS DDS communication  
    my_pub = RPMPubNode()
    print("Publisher Node running ...")
    
    try:
        rclpy.spin(my_pub) # Keeps the node running until a keyborad key is pressed
    except KeyboardInterrupt:
        print("Terminating the node ...")
        my_pub.destroy_node()
        

        
if __name__ == "__main__":
    main()