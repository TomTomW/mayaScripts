import maya.cmds as cmds
import pymel.core as pm

''' create group with the name of the selected object with ctrlSpace at the end.
    Match transforms of the selected object and parent selected object under new group'''


selection = pm.ls(sl=True)
selectionName = selection[0]

newGroup = pm.group(em=True, name=selectionName + 'Space')

def matchXfos():

    # get selection
    
    srcObj = selection[0]
    targets = newGroup
    
        
    srcXfo = pm.xform(srcObj, query=True, worldSpace=True, matrix=True)
      
    pm.xform(targets, worldSpace=True, matrix=srcXfo)

matchXfos()

pm.parent(selectionName, newGroup)