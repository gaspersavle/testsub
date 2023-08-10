from colorama import Fore
import rospy
import std_msgs.msg
from std_msgs.msg import String

class SubTest():
    def __init__(self) -> None:
        self.textTopic = '/rostest/text'
        self.rosNodeText = 'rostest'

        self.initRosPy()

        rospy.spin()

    def initRosPy(self):
        rospy.init_node(self.rosNodeText, anonymous=True)
        rospy.Subscriber(self.textTopic, String, self.subCB)

    def subCB(self, data):
        rospy.loginfo('Eo cujem: ' + data.data)
        print(f"{Fore.BLUE} Eo cujem: {data.data}")

if __name__ == "__main__":
    print(f"{Fore.GREEN} Starting subscriber")
    SubTest()    



        
        