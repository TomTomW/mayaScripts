import maya.cmds as cmds

''' create group with the name of the selected object with ctrlSpace at the end.
    Match transforms of the selected object and parent selected object under new group'''


# -------------------------------------------------------------------------
def ctrlSpace(targets, name='Space'):
    # Parents target under a group created at the same location.

    try:
        if len(targets) > 1:
            for target in targets:
                ctrlGrp = cmds.group(em=True, name=target + name)
                matchXfos(target, ctrlGrp)
                cmds.parent(target, ctrlGrp)

        else:
            ctrlGrp = cmds.group(em=True, name=targets[0] + name)
            matchXfos(targets[0], ctrlGrp)
            cmds.parent(targets[0], ctrlGrp)

    except IndexError:
        print '//Error//: Something needs to be selected for ctrlSpace() to run!!!'

# -------------------------------------------------------------------------
def matchXfos(srcObj, target):
    # match transforms of srcObj to the target

    srcXfo = cmds.xform(srcObj, query=True, worldSpace=True, matrix=True)
    cmds.xform(target, worldSpace=True, matrix=srcXfo)


ctrlSpace(cmds.ls(sl=1), 'Space')