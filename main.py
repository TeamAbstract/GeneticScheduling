from vessels import Vessels
from gui.mainWindow import startGUI


def init():
	vessels = Vessels()
	vessels.addVessel(20)
	vessels.addVessel(30)
	vessels.addVessel(50)



init()
startGUI()
