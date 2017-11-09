"""
from Qt import QtWidgets

class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("My Window Title")
        
a = MyWindow()
a.show()
"""    

from Qt import QtWidgets, QtCore, QtGui
from maya import cmds 

class HandRig(QtWidgets.QWidget):

	def __init__(self, parent=None):

		try:
			cmds.deleteUI('Hand Rig')

		except:
			print 'Not other UI exsits'

		super(HandRig, self).__init__(parent)
		self.setWindowTitle("Hand Rig")

		self.buildUI()

	def buildUI(self):

		# Builds the user interface for the rig

		layout = QtWidgets.QGridLayout(self)

		# Thumb finger Contorl Buttons

		thumb01_button = QtWidgets.QPushButton('thumb01_ctrl')
		thumb01_button.clicked.connect(self.button)
		layout.addWidget(thumb01_button, 3, 1)

		thumb02_button = QtWidgets.QPushButton('thumb02_ctrl')
		thumb02_button.clicked.connect(self.button)
		layout.addWidget(thumb02_button, 2, 1)

		# Index finger Control Buttons

		index01_button = QtWidgets.QPushButton('index01_ctrl')
		#tempButton1.setMinimumWidth(10)
		#tempButton1.setMinimumHeight(10)
		index01_button.clicked.connect(self.button)
		layout.addWidget(index01_button, 3, 2)
		
		index02_button = QtWidgets.QPushButton('index02_ctrl')
		index02_button.clicked.connect(self.button)
		layout.addWidget(index02_button, 2, 2)

		index03_button = QtWidgets.QPushButton('index03_ctrl')
		index03_button.clicked.connect(self.button)
		layout.addWidget(index03_button, 1, 2)

		# Middle Finger Control Buttons

		middle01_button = QtWidgets.QPushButton('middle01_ctrl')
		middle01_button.clicked.connect(self.button)
		layout.addWidget(middle01_button, 3, 3)
		
		middle02_button = QtWidgets.QPushButton('middle02_ctrl')
		middle02_button.clicked.connect(self.button)
		layout.addWidget(middle02_button, 2, 3)

		middle03_button = QtWidgets.QPushButton('middle03_ctrl')
		middle03_button.clicked.connect(self.button)
		layout.addWidget(middle03_button, 1, 3)

		# Ring Finger Control Buttons

		ring01_button = QtWidgets.QPushButton('ring01_ctrl')
		ring01_button.clicked.connect(self.button)
		layout.addWidget(ring01_button, 3, 4)
		
		ring02_button = QtWidgets.QPushButton('ring02_ctrl')
		ring02_button.clicked.connect(self.button)
		layout.addWidget(ring02_button, 2, 4)

		ring03_button = QtWidgets.QPushButton('ring03_ctrl')
		ring03_button.clicked.connect(self.button)
		layout.addWidget(ring03_button, 1, 4)

		# Pinkie Finger Control Buttons

		pinkie01_button = QtWidgets.QPushButton('pinkie01_ctrl')
		pinkie01_button.clicked.connect(self.button)
		layout.addWidget(pinkie01_button, 3, 5)
		
		pinkie02_button = QtWidgets.QPushButton('pinkie02_ctrl')
		pinkie02_button.clicked.connect(self.button)
		layout.addWidget(pinkie02_button, 2, 5)

		pinkie03_button = QtWidgets.QPushButton('pinkie03_ctrl')
		pinkie03_button.clicked.connect(self.button)
		layout.addWidget(pinkie03_button, 1, 5)

		# Hand Control Button

		hand_button = QtWidgets.QPushButton('wrist_ctrl')
		hand_button.clicked.connect(self.button)
		layout.addWidget(hand_button)

		# arm Control Button

		arm_button = QtWidgets.QPushButton('arm_ctrl')
		arm_button.clicked.connect(self.button)
		layout.addWidget(arm_button)


		print "I am in the buildUI()"

	def reset(self):
		pass

	def close(self, *args):

		cmds.deletUI(windowName)

	def button(self):

		print 'The BUTTON has been clicked'

