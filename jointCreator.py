import maya.cmds as cmds
from utils import midpoint

#--------------------------------------------------------------------------------------------------
def orient_joints(selected_joints=cmds.ls(sl=1, type="joint")):
    # orients joints with y-up and x down the chain.
    for selected_joint in selected_joints:
        if cmds.listRelatives(selected_joint, children=True):
            # if selected joint has a child run this
            if len(cmds.listRelatives(selected_joint, ad=True)) >= 2:
                # if the joint has multiple children then use a locator at the midpoint for up-vector
                children_joints = cmds.listRelatives(selected_joint, ad=1)[:2]
                children_joints = [selected_joint] + children_joints
                temp_locator = cmds.spaceLocator(name="tmp_locator_01")
                mid_point = midpoint(children_joints, 0.1)
                cmds.xform(temp_locator[0], ws=1, t=(mid_point[0], mid_point[1], mid_point[2]))
                child_joint = cmds.listRelatives(selected_joint, children=True)
                cmds.parent(child_joint, world=True)
                aim_constraint = cmds.aimConstraint(child_joint, selected_joint, aimVector=(1, 0, 0), upVector=(0, 1, 0), worldUpObject=temp_locator[0])
                cmds.delete(aim_constraint)
                cmds.makeIdentity(selected_joint, r=True, apply=True)
                cmds.parent(child_joint, selected_joint)
            elif len(cmds.listRelatives(selected_joint, ad=1)) == 1:
                # if the joint has one child then run this
                    try:
                        if temp_locator:
                            child_joint = cmds.listRelatives(selected_joint, children=True)
                            cmds.parent(child_joint, world=True)
                            aim_constraint = cmds.aimConstraint(child_joint, selected_joint, aimVector=(1, 0, 0), upVector=(0, 1, 0), worldUpObject=temp_locator[0])
                            cmds.delete(aim_constraint)
                            cmds.makeIdentity(selected_joint, r=True, apply=True)
                            cmds.parent(child_joint, selected_joint)
                            cmds.delete(temp_locator[0])
                    except:
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
            # if the joint does not have any children zero the joint orients. 
            cmds.makeIdentity(selected_joint, jointOrient=True, apply=True)

#--------------------------------------------------------------------------------------------------
def createJoints(selection=cmds.ls(sl=1)):
    # creates joint at the location of the order of selection. Uses orient_joint to orient the joints properly.
    cmds.select(clear=True)
    created_joints = []
    for item in selection:
        new_joint = cmds.joint()
        cmds.matchTransform(new_joint, item)
        created_joints.append(new_joint)
    orient_joints(created_joints)

createJoints()