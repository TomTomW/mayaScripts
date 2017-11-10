from Qt import QtWidgets, QtCore, QtGui
from maya import cmds 
import sys
class HandRig(QtWidgets.QWidget):

	def __init__(self, parent=None):

		try:
			cmds.deleteUI('Hand Rig')

		except:
			print 'No other UI exsits'

		super(HandRig, self).__init__(parent)
		self.setWindowTitle("Hand Rig")

		self.buildUI()

	def buildUI(self):

		# Builds the user interface for the rig

		layout = QtWidgets.QGridLayout(self)

		# Thumb finger Contorl Buttons

		thumb01_button = QtWidgets.QPushButton('thumb01_ctrl')
		thumb01_button.setFixedWidth(75)
		thumb01_button.setFixedHeight(100)
		thumb01_button.clicked.connect(self.button)
		layout.addWidget(thumb01_button, 4, 1)

		thumb02_button = QtWidgets.QPushButton('thumb02_ctrl')
		thumb02_button.setFixedWidth(75)
		thumb02_button.setFixedHeight(75)
		thumb02_button.clicked.connect(self.button)
		layout.addWidget(thumb02_button, 3, 1)

		# Index finger Control Buttons

		index01_button = QtWidgets.QPushButton('index01_ctrl')
		index01_button.setFixedWidth(75)
		index01_button.setFixedHeight(100)
		index01_button.clicked.connect(self.button)
		layout.addWidget(index01_button, 3, 2)
		
		index02_button = QtWidgets.QPushButton('index02_ctrl')
		index02_button.setFixedWidth(75)
		index02_button.setFixedHeight(75)
		index02_button.clicked.connect(self.button)
		layout.addWidget(index02_button, 2, 2)

		index03_button = QtWidgets.QPushButton('index03_ctrl')
		index03_button.setFixedWidth(75)
		index03_button.setFixedHeight(50)
		index03_button.clicked.connect(self.button)
		layout.addWidget(index03_button, 1, 2)

		# Middle Finger Control Buttons

		middle01_button = QtWidgets.QPushButton('middle01_ctrl')
		middle01_button.setFixedWidth(75)
		middle01_button.setFixedHeight(100)
		middle01_button.clicked.connect(self.button)
		layout.addWidget(middle01_button, 3, 3)
		
		middle02_button = QtWidgets.QPushButton('middle02_ctrl')
		middle02_button.setFixedWidth(75)
		middle02_button.setFixedHeight(75)
		middle02_button.clicked.connect(self.button)
		layout.addWidget(middle02_button, 2, 3)

		middle03_button = QtWidgets.QPushButton('middle03_ctrl')
		middle03_button.setFixedWidth(75)
		middle03_button.setFixedHeight(50)
		middle03_button.clicked.connect(self.button)
		layout.addWidget(middle03_button, 1, 3)

		# Ring Finger Control Buttons

		ring01_button = QtWidgets.QPushButton('ring01_ctrl')
		ring01_button.setFixedWidth(75)
		ring01_button.setFixedHeight(100)
		ring01_button.clicked.connect(self.button)
		layout.addWidget(ring01_button, 3, 4)
		
		ring02_button = QtWidgets.QPushButton('ring02_ctrl')
		ring02_button.setFixedWidth(75)
		ring02_button.setFixedHeight(75)
		ring02_button.clicked.connect(self.button)
		layout.addWidget(ring02_button, 2, 4)

		ring03_button = QtWidgets.QPushButton('ring03_ctrl')
		ring03_button.setFixedWidth(75)
		ring03_button.setFixedHeight(50)
		ring03_button.clicked.connect(self.button)
		layout.addWidget(ring03_button, 1, 4)

		# Pinkie Finger Control Buttons

		pinkie01_button = QtWidgets.QPushButton('pinkie01_ctrl')
		pinkie01_button.setFixedWidth(75)
		pinkie01_button.setFixedHeight(100)
		pinkie01_button.clicked.connect(self.button)
		layout.addWidget(pinkie01_button, 3, 5)
		
		pinkie02_button = QtWidgets.QPushButton('pinkie02_ctrl')
		pinkie02_button.setFixedWidth(75)
		pinkie02_button.setFixedHeight(75)
		pinkie02_button.clicked.connect(self.button)
		layout.addWidget(pinkie02_button, 2, 5)

		pinkie03_button = QtWidgets.QPushButton('pinkie03_ctrl')
		pinkie03_button.setFixedWidth(75)
		pinkie03_button.setFixedHeight(50)
		pinkie03_button.clicked.connect(self.button)
		layout.addWidget(pinkie03_button, 1, 5)

		# Hand Control Button

		hand_button = QtWidgets.QPushButton('wrist_ctrl')
		hand_button.setFixedWidth(75)
		hand_button.setFixedHeight(100)
		hand_button.clicked.connect(self.button)
		layout.addWidget(hand_button, 5, 3)

		# arm Control Button

		arm_button = QtWidgets.QPushButton('arm_ctrl')
		arm_button.clicked.connect(self.button)
		layout.addWidget(arm_button, 6, 3)

		oImage =  QtGui.QImage("test.png")
		sImage = oImage.scaled(QtCore.QSize(300,200))
		palette = QtGui.QPalette()
		palette.setBrush(10, QtGui.QBrush(sImage))
		self.setPalette(palette)

		print "I am in the buildUI()"

	def reset(self):
		pass

	def close(self, *args):

		cmds.deletUI(windowName)

	def button(self):

		print 'The BUTTON has been clicked'

	def selectCtrl(self, selectedButton):
		print'I am in' + ' ' + selectedButton
		'''cmds.select('hand_M_' + selectedButton)

		print ('I have selected' + selectedButton)'''

