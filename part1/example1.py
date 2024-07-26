# 선언
import rospy  
from geometry_msgs.msg import Twist  
from sensor_msgs.msg import LaserScan  
from math import *  
from time import *  

# 정의
class LimoEstop:  # LimoEstop 클래스 정의했
    def __init__(self):  # 클래스를 생성했
        rospy.init_node("laser_scan_node")  # "laser_scan_node" 노드를 생성했
        rospy.Subscriber("/scan", LaserScan, self.laser_callback)  # rospy 모듈 속, Subscriber 클래스 self.laser_callback 함수가 LaserScan 형태의 "/scan" 값의 Subscriber하도록 정의했
        self.rate=rospy.Rate(30) # self.rate 변수 값의 rospy 모듈 속, Rate 클래스 30 값으로 정의했
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=3)  # self.pub 변수 값의 rospy 모듈 속, Publisher 클래스가 Twist 형태의 "/cmd_vel" 값의 큐 사이즈 3으로 Publisher하도록 정의했
        self.lidar_flag = False  # self.lidar_flag 변수 값의 False 값으로 정의했
        self.deg = 10  # self.deg 변수 값의 10 값으로 정의했
        self.cmd_vel_msg = Twist()  # self.cmd_vel_msg 인스턴슨 Twist 클래스를 실행하도록 정의했 
        

    def laser_callback(self, msg): # laser_callback 함순 mag 값을 인자값으로 받도록 정의했
        num = 0 # num 변수 값의 0 값으로 정의했
        if self.lidar_flag == False: # 만약 self.lider_flag 변수 값이 False이면 아래의 구문을 이행!
            self.degrees = [
                (msg.angle_min + (i * msg.angle_increment)) * 180 / pi
                for i, data in enumerate(msg.ranges)
            ] # self.degrees 변수 값의 msg.angle_min + (i * msg.angle_increment)) * 180 / pi for i, data in enumerate(msg.ranges)로 정의했
              # for i, data in enumerate(msg.ranges) : msg 길이 만큼 i를 반복하도록 정의했
            self.lidar_flag = True # self.lidar_flag 변수 값의 True 값으로 정의했
        
        for i, data in enumerate(msg.ranges): # msg 길이 만큼 i를 반복하도록 정의했
            if -self.deg < self.degrees[i] < self.deg and 0 < msg.ranges[i] < 0.5: # 만약 -self.deg < self.degrees[i] < self.deg and 0 < msg.ranges[i] < 0.5이면 아래의 구문을 이행!
                num += 1 # num 변수 값의 1 증가하도록 정의했
        
        if num < 10: # num < 10이면 아래의 구문을 이행!
            self.cmd_vel_msg.linear.x = 0.15 # self.cmd_vel_msg 인스턴스 값의 0.15 값으로 linear.x 방향으로 정의했
         
        else: # num < 10 아니면 아래의 구문을 이행!
            self.cmd_vel_msg.linear.x = 0 # 정지!
            
        self.pub.publish(self.cmd_vel_msg) # 정의된 self.cmd_vel_msg 값의 publish 실행했
        self.rate.sleep() # 30! Delay

# 실행
if __name__ == "__main__": # __name__ == "__main__"이면 아래의 구문을 이행!
    limo_estop = LimoEstop() # limo_estop 인스턴슨 LimoEstop 클래스를 실행했
    try:
        rospy.spin() # 반복!
    except rospy.ROSInterruptException: # 예외 발생 무시!
        pass
