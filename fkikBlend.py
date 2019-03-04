import maya.cmds as cmds
import maya.OpenMaya as om
import curves


'''
Task List:
DONE--Duplicate joint chain and rename the joints to fk and ik
DONE--Create controls for the FK chain of joints 
DONE--create ik handle for ik joint chain with control
DONE--create the polevector for the ik handle
DONE--parent the blend joints to the fk and ik joints
DONE--parent bind joints to the blend joints
DONE--create one parent joint for the ik, fk, and blend joints to live under
DONE--create blend between ik and fk (use direct connects and plusMinusNode.)
'''


# -------------------------------------------------------------------------
def fkIkBlend(bones, ctrlColor=None):
    children = cmds.listRelatives(bones, ad=1)
    children.reverse()
    origJnts = [bones] + children
    fkJnts = []
    ikJnts = []
    blendJnts = []

    # Duplicates bones and replacing 'bind' with 'fk_jnt'
    for jnt in cmds.duplicate(bones, rc=1):
        newName = jnt.split('bind')
        cmds.rename(jnt, newName[0] + 'fk_jnt')
        fkJnts.append(newName[0] + 'fk_jnt')

    # Duplicates bones and replacing 'bind' with 'ik_jnt'
    for jnt in cmds.duplicate(bones, rc=1):
        newName = jnt.split('bind')
        cmds.rename(jnt, newName[0] + 'ik_jnt')
        ikJnts.append(newName[0] + 'ik_jnt')

    # Duplicates bones replacing 'bind' with 'blend_jnt'
    for jnt in cmds.duplicate(bones, rc=1):
        newName = jnt.split('bind')
        cmds.rename(jnt, newName[0] + 'blend_jnt')
        blendJnts.append(newName[0] + 'blend_jnt')

    # parents bones to the blend joints. parents the blend joints to fk_jnts and ik_jnts
    for i, jnt in enumerate(origJnts, 0):
        cmds.parentConstraint(blendJnts[i], jnt)
        cmds.parentConstraint(fkJnts[i], blendJnts[i])
        cmds.parentConstraint(ikJnts[i], blendJnts[i])

    # creates parent joint and parents fk, ik, and blend joints under
    parentJnt = cmds.duplicate(bones)
    parentName = parentJnt[0].split('bind')
    cmds.rename(parentJnt[0], parentName[0] + 'parent')
    cmds.parent(fkJnts[0], parentName[0] + 'parent')
    cmds.parent(ikJnts[0], parentName[0] + 'parent')
    cmds.parent(blendJnts[0], parentName[0] + 'parent')
    
    ikControl(ikJnts, ctrlColor=ctrlColor)
    fkControls(fkJnts, ctrlColor=ctrlColor)
    settingsCtrl(blendJnts, ctrlColor=ctrlColor)


# -------------------------------------------------------------------------
def ikControl(bones, ctrlColor=None):
    # creates ik handle for bones along with control and polevector
    ik = cmds.ikHandle(sj=bones[0], ee=bones[2])[0]
    cmds.setAttr('{}.visibility'.format(ik), 0)
    ctrl = curves.ctrlCurves(name='ik_ctrl', type='box', color=ctrlColor)
    matchXfos(bones[2], ctrl)
    ctrlSpace(ctrl, 'Space')
    cmds.parent(ik, ctrl)
    cmds.orientConstraint(ctrl, bones[2])

    poleVec = poleVector(bones, pvDist=2, ctrlColor=ctrlColor)
    cmds.poleVectorConstraint(poleVec, ik)

    ctrlSpace(poleVec, 'Space')


# -------------------------------------------------------------------------
def fkControls(bones, ctrlColor=None):
    # Creates control curves for each item in 'bones'

    ctrls = []
    for bone in bones:
        newName = bone.split('jnt')
        ctrl = curves.ctrlCurves(name=newName[0] + 'ctrl', type='circle', color=ctrlColor)
        matchXfos(bone, ctrl)
        ctrlSpace(ctrl, 'Space')
        ctrls.append(str(ctrl) + 'Space')

        cmds.orientConstraint(ctrl, bone)
    # iterating through newly created controlSpaces and creating a hierachy
    # similar to the 'bones' hierarchy
    for i, ctrl in enumerate(ctrls, 0):
        if ctrl != ctrls[0]:
            cmds.parent(ctrl, cmds.listRelatives(ctrls[i - 1])[0])


# -------------------------------------------------------------------------
def ctrlSpace(targets, name='Space'):
    # Parents target under a group created at the same location.

    try:
        if type(targets) == list and len(targets) > 1:
            for target in targets:
                ctrlGrp = cmds.group(em=True, name=target + name)
                matchXfos(target, ctrlGrp)
                cmds.parent(target, ctrlGrp)

        elif type(targets) == list:
            ctrlGrp = cmds.group(em=True, name=targets[0] + name)
            matchXfos(targets[0], ctrlGrp)
            cmds.parent(targets[0], ctrlGrp)

        else:
            ctrlGrp = cmds.group(em=True, name=targets + name)
            matchXfos(targets, ctrlGrp)
            cmds.parent(targets, ctrlGrp)

    except IndexError:
        print '//Error//: Something needs to be selected for ctrlSpace() to run!!!'


# -------------------------------------------------------------------------
def matchXfos(srcObj, target):
    # match transforms of srcObj to the target

    srcXfo = cmds.xform(srcObj, query=True, worldSpace=True, matrix=True)
    cmds.xform(target, worldSpace=True, matrix=srcXfo)


# -------------------------------------------------------------------------
def poleVector(bones, pvDist=2, ctrlColor=None):
    # creates control positioned for a polevector. Returns control

    start = cmds.xform(bones[0], q=1, ws=1, t=1)
    mid = cmds.xform(bones[1], q=1, ws=1, t=1)
    end = cmds.xform(bones[2], q=1, ws=1, t=1)

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

    ctrl = curves.ctrlCurves(name='pVec_ctrl', type='circle', color=ctrlColor)

    cmds.xform(ctrl, ws=1, t=(finalV.x, finalV.y, finalV.z))

    return ctrl

# -------------------------------------------------------------------------
def settingsCtrl(blendJnts, ctrlColor=None):
    # creates setting ctrl at end the last joint in blendJoints. Adds attribute to control 'fkikBlend' connects to blendJnt constraints. 
    
    ctrl = curves.ctrlCurves(name='settings_ctrl', type='pin', color=ctrlColor)
    ctrlSpace(ctrl)
    cmds.parentConstraint(blendJnts[2], ctrl)
    cmds.addAttr(longName='fkikBlend', niceName='FKIK Blend', defaultValue=0.0, minValue=0.0, maxValue=1.0,
                 hidden=False, keyable=True)
    plusMinus = cmds.createNode('plusMinusAverage')
    cmds.setAttr('{}.operation'.format(plusMinus), 2)
    cmds.setAttr('{}.input1D[0]'.format(plusMinus), 1)
    cmds.connectAttr('{}.fkikBlend'.format(ctrl), '{}.input1D[1]'.format(plusMinus))
    blendRelatives = cmds.listRelatives(blendJnts[0], ad=1)
    for i in blendRelatives:
        if 'Constraint' in cmds.objectType(i):
            for attr in cmds.listAttr(i, ud=1):
                # These are hardcoded: It might be better to search for these constraint attrs by looking at what the fk ik joints are.
                if '_ik_' in attr:
                    cmds.connectAttr('{}.fkikBlend'.format(ctrl), '{}.{}'.format(i, attr))
                elif '_fk_' in attr:
                    cmds.connectAttr('{}.output1D'.format(plusMinus), '{}.{}'.format(i, attr))
    
