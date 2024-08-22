#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import Int32, Float32

Wheel_Diameter_Default = 0.2

class RPMSubNode(Node):
    def __init__(self):
        super().__init__("rpm_sub_node")
        self.declare_parameter("Wheel_Diameter", Wheel_Diameter_Default)
        self.sub = self.create_subscription(Int32, "rpm", self.subscribe_callback, 10)
        self.pub_02 = self.create_publisher(Float32, "speed", 10)

    def subscribe_callback(self, msg):
        wheel_diameter_param = self.get_parameter("Wheel_Diameter").get_parameter_value().double_value
        print("Received, my curent rpm is: " + str(msg.data))
        speed_msg = Float32()
        speed_msg.data = 2*3.14*(wheel_diameter_param/2)*((msg.data)/60)
        speed_msg.data = round(speed_msg.data,2) 
        self.pub_02.publish(speed_msg)
        print(f"Publishing speed: {speed_msg.data} m/s")


def main(args=None):
    rclpy.init()      # Initializes the ROS DDS communication  
    my_sub = RPMSubNode()
    print(" Publisher-Subscriber node running")
    
    try:
       rclpy.spin(my_sub)
    except KeyboardInterrupt:
        print("Terminating the node ...")
        my_sub.destroy_node()
        

        
if __name__ == "__main__":
    main()