#! usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String 

class DriveClass():
    
    def __init__(self):

        self.pub_drive = rospy.Publisher("/position/drive", String, queue_size=10)
        
        self.callbackF
        self.sub_func

        self.sub_drive = rospy.Subscriber("/serial/drive", String, self.callbackF)
        
        self.mydata = None

        self.first =None
        self.second = None
        self.third = None
        self.fourth = None




    def callbackF(self,msg):
        rospy.loginfo("Data received")
        
        self.veri = msg.data # /serial/drive verisi
        self.newList=[]
    


        #VERİYİ İŞLEME ************************************
        for item in self.veri:

            self.newList.append(item)


                

        self.first = "".join(self.newList[1:5])
        self.second = "".join(self.newList[5:9])
        self.third = "".join(self.newList[9:13])
        self.fourth = "".join(self.newList[13:17]) 



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
        #VERİ İŞLEM SONU **********************************


        self.wanted = "{} {} {} {}".format(self.first, self.second, self.third, self.fourth)

        rospy.loginfo(self.wanted)

        self.mydata = String()
        self.mydata.data = self.wanted
          
        self.pub_drive.publish(self.mydata)

       
      

    
    

    def sub_func(self):
        rospy.init_node("drive_node")

        rospy.spin()



if __name__ == "__main__":
    
    drive = DriveClass()
    drive.sub_func()
  
        
    