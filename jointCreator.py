import pymel.core as pm 

# Takes in a list of selected objs in the order the joints will be created. 

def createJoints(selection=pm.selected()):
    pm.select(clear=True)
    for item in selection:
        pm.matchTransform(pm.joint(), item)
    pm.select(pm.selected()[0].root())
    alignJoints()
	
def alignJoints():
    pm.selected()[0].orientJoint('xyz', sao='yup')
    try:
        pm.select(pm.listRelatives(children=True)[0])
        print "I am in the if statement"
        alignJoints()
    except:
        pm.matchTransform(pm.selected()[0], pm.selected()[0].getParent(), rot=True)


createJoints()