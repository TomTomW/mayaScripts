import maya.cmds as cmds

# Takes in a list of selected objs in the order the joints will be created.

def orient_joints(selected_joints=cmds.ls(sl=1, type="joint")):
    # orients joints using aimConstraint and Locator
    for selected_joint in selected_joints:
        if cmds.listRelatives(selected_joint, children=True):
            temp_locator = cmds.spaceLocator(name="tmp_locator_01")
            cmds.matchTransform(temp_locator[0], selected_joint)
            cmds.move(0, 2, 0, temp_locator[0], relative=True)
            child_joint = cmds.listRelatives(selected_joint, children=True)
            cmds.parent(child_joint, world=True)
            aim_constraint = cmds.aimConstraint(child_joint, selected_joint, aimVector=(1, 0, 0), upVector=(0, 1, 0), worldUpObject=temp_locator[0])
            cmds.delete(aim_constraint)
            cmds.makeIdentity(selected_joint, r=True, apply=True)
            cmds.parent(child_joint, selected_joint)
            cmds.delete(temp_locator[0])
        else:
            cmds.makeIdentity(selected_joint, jointOrient=True, apply=True)

def createJoints(selection=cmds.ls(sl=1)):
    # creates joints using a selection of objects and using orient_joint() orients the newly created joints. 
    cmds.select(clear=True)
    created_joints = []
    for item in selection:
        new_joint = cmds.joint()
        cmds.matchTransform(new_joint, item)
        created_joints.append(new_joint)
    orient_joints(created_joints)

createJoints()