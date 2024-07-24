import rospy  
from geometry_msgs.msg import Twist  
from sensor_msgs.msg import LaserScan  
from math import *  
from time import *  
#선언
class LimoEstop:  
    def __init__(self):  
        rospy.init_node("laser_scan_node")  
        rospy.Subscriber("/scan", LaserScan, self.laser_callback)  
        self.rate=rospy.Rate(30)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=3)  
        self.lidar_flag = False  
        self.deg = 10  
        self.cmd_vel_msg = Twist()  
        

    def laser_callback(self, msg):
        num = 0 
        
        if self.lidar_flag == False:
            self.degrees = [
                (msg.angle_min + (i * msg.angle_increment)) * 180 / pi
                for i, data in enumerate(msg.ranges)
            ]
            self.lidar_flag = True
        
        for i, data in enumerate(msg.ranges):
            if -self.deg < self.degrees[i] < self.deg and 0 < msg.ranges[i] < 0.5:
                num += 1
        
        if num < 10:
            self.cmd_vel_msg.linear.x = 0.15
            
            print({})
        
        else:
            self.cmd_vel_msg.linear.x = 0
        self.pub.publish(self.cmd_vel_msg)
        self.rate.sleep()
#정의
if __name__ == "__main__":
    limo_estop = Limo_estop()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
#실행