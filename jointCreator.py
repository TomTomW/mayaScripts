import maya.cmds as cmds


# Takes in a list of selected objs in the order the joints will be created.

def createJoints(selection=cmds.ls(sl=1)):
    # There is probably a better way to do this.
    cmds.select(clear=True)
    for item in selection:
        print
        item
        cmds.matchTransform(cmds.joint(), item)
    # cmds.select((cmds.ls(sl=1))[0].root())
    alignJoints()


# recursive function that properly orinets all joints created using createJoints


def alignJoints():
    # Giving unicode error. FIX
    cmds.ls(sl=1)[0].orientJoint('xyz', sao='yup')
    try:
        cmds.select(cmds.listRelatives(children=True)[0])
        print
        "I am in the if statement"
        alignJoints()
    except:
        cmds.joint(edit=True, orientation=(0, 0, 0))


createJoints()