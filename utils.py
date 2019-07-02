import maya.cmds as cmds
import maya.OpenMaya as om

#--------------------------------------------------------------------------------------------------
def ctrlSpace(targets, name='Space'):
    # Parents target under a group created at the same location.

    try:
        if type(targets) == list and len(targets) > 1:
            for target in targets:
                ctrlGrp = cmds.group(em=True, name=target + name)
                matchXfos(target, ctrlGrp)
                cmds.parent(target, ctrlGrp)
                return ctrlGrp

        elif type(targets) == list:
            ctrlGrp = cmds.group(em=True, name=targets[0] + name)
            matchXfos(targets[0], ctrlGrp)
            cmds.parent(targets[0], ctrlGrp)
            return ctrlGrp

        else:
            ctrlGrp = cmds.group(em=True, name=targets + name)
            matchXfos(targets, ctrlGrp)
            cmds.parent(targets, ctrlGrp)
            return ctrlGrp

    except IndexError:
        print '//Error//: Something needs to be selected for ctrlSpace() to run!!!'


#--------------------------------------------------------------------------------------------------
def matchXfos(srcObj, target):
    # match transforms of srcObj to the target

    srcXfo = cmds.xform(srcObj, query=True, worldSpace=True, matrix=True)
    cmds.xform(target, worldSpace=True, matrix=srcXfo)


#--------------------------------------------------------------------------------------------------
def midpoint(points, pvDist=2):
    # creates control positioned for a midpoint. Returns control
    # using Marco Giordano method for finding the midpoint

    start = cmds.xform(points[0], q=1, ws=1, t=1)
    mid = cmds.xform(points[1], q=1, ws=1, t=1)
    end = cmds.xform(points[2], q=1, ws=1, t=1)

    startV = om.MVector(start[0], start[1], start[2])
    midV = om.MVector(mid[0], mid[1], mid[2])
    endV = om.MVector(end[0], end[1], end[2])

    startEnd = endV - startV
    startMid = midV - startV

    dotP = startMid * startEnd
    proj = float(dotP) / float(startEnd.length())
    startEndN = startEnd.normal()
    projV = startEndN * proj

    arrowV = startMid - projV
    arrowV *= pvDist
    finalV = arrowV + midV

    return [finalV.x, finalV.y, finalV.z]

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