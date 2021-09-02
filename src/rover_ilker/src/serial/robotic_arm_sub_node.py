#! usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

class RoboticArm():
    def __init__(self):
        
        self.callbackF 
        self.subfunc
        
        self.sub_robotic = rospy.Subscriber("/serial/robotic_arm", String, self.callbackF)
        self.pub_robotic = rospy.Publisher("/position/robotic_arm", String, queue_size=10)

        self.mydata = None

        self.first =None
        self.second = None
        self.third = None
        self.fourth = None
        self.fifth = None
        self.sixth = None




    def callbackF(self,msg):
        rospy.loginfo("Data received")
        
        self.veri = msg.data
        self.newList=[]
    


        #VERİYİ İŞLEME ************************************
        for item in self.veri:

            self.newList.append(item)


                

        self.first = "".join(self.newList[1:5])
        self.second = "".join(self.newList[5:9])
        self.third = "".join(self.newList[9:13])
        self.fourth = "".join(self.newList[13:17])
        self.fifth = "".join(self.newList[17:21])
        self.sixth = "".join(self.newList[21:25]) 



        #first 4
        if list(self.first)[0] == "0" :
            self.first = "{}".format("".join(list(self.first)[1:]))
            if int(self.first) > 255:
                self.first = 255

        else:
            self.first = "-{}".format("".join(list(self.first)[1:]))
            if int(self.first) <-255:
                self.first = -255




        #second 4
        if list(self.second)[0] == "0" :
            self.second = "{}".format("".join(list(self.second)[1:]))
            if int(self.second) > 255:
                second = 255

        else:
            self.second = "-{}".format("".join(list(self.second)[1:]))
            if int(self.second) < -255:
                self.second = -255



        #third 4
        if list(self.third)[0] == "0" :
            self.third = "{}".format("".join(list(self.third)[1:]))
            if int(self.third) > 255:
                self.third = 255

        else:
            self.third = "-{}".format("".join(list(self.third)[1:]))
            if int(self.third) <-255:
                self.third = -255



        # fourth 4
        if list(self.fourth)[0] == "0" :
            self.fourth = "{}".format("".join(list(self.fourth)[1:]))
            if int(self.fourth) > 255:
                self.fourth = 255

        else:
            self.fourth = "-{}".format("".join(list(self.fourth)[1:]))
            if int(self.fourth) < -255:
                self.fourth = -255



        #fifth 4
        if list(self.fifth)[0] == "0" :
            self.fifth = "{}".format("".join(list(self.fifth)[1:]))
            if int(self.fifth) > 255:
                self.fifth = 255

        else:
            self.fifth = "-{}".format("".join(list(self.fifth)[1:]))
            if int(self.fifth) < -255:
                self.fifth = -255



        #sixth 4
        if list(self.sixth)[0] == "0" :
            self.sixth = "{}".format("".join(list(self.sixth)[1:]))
            if int(self.sixth) > 255:
                self.sixth = 255

        else:
            self.sixth = "-{}".format("".join(list(self.sixth)[1:]))
            if int(self.sixth) < -255:
                self.sixth = -255        
        #VERİ İŞLEM SONU **********************************


        self.wanted = "{} {} {} {} {} {}".format(self.first, self.second, self.third, self.fourth,self.fifth, self.sixth)

        rospy.loginfo(self.wanted)

        self.mydata = String()
        self.mydata.data = self.wanted
          
        self.pub_robotic.publish(self.mydata)

       
      

    
    

    def subfunc(self):
        rospy.init_node("robotic_arm_node")

        rospy.spin()




if __name__ == "__main__":
    obj = RoboticArm()
    obj.subfunc()
    