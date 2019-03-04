import maya.cmds as cmds

'''
This file will be used to store different types of curves. 

You can specify the color of the curve. This will be a class based file. 

'''
# This will make the classic FK control
# [[1.4654943925052066e-14, 3.0, 0.0], [7.105427357601002e-15, 2.0, 2.0], [-3.9968028886505635e-15, 0.0, 3.0], [-1.2434497875801753e-14, -2.0, 2.0], [-1.4654943925052066e-14, -3.0, 0.0], [-7.105427357601002e-15, -2.0, -2.0], [3.9968028886505635e-15, 0.0, -3.0], [1.2434497875801753e-14, 2.0, -2.0], [1.4654943925052066e-14, 3.0, 0.0], [0.0, 0.0, 0.0], [4.0, -1.9539925233402755e-14, 5.329070518200751e-15]]


# -------------------------------------------------------------------------
def writeCurveData(crv):
    # takes in curve and creates a list of all the positions of each CV of the curve

    cvLocations = []
    crvShape = cmds.listRelatives(crv[0], type='shape')
    cvs = cmds.ls('{}.cv[*]'.format(crvShape[0]), fl=1)

    for cv in cvs:
        cvLocations.append(cmds.pointPosition(cv))

    return cvLocations

# -------------------------------------------------------------------------
def createCurve(locations):
    # takes in a list and creates a linear curve with CVs at the locations provided

    cmds.curve(d=1, p=locations)



# -------------------------------------------------------------------------
def ctrlCurves(name='ctrlCurve', type='circle', color=None):
    
    colorsDic = {'red': 13, 'blue': 6, 'yellow': 17}

    if type == 'circle':
        ctrl=cmds.circle()[0]
        
        cmds.rename(ctrl, name)
        if color != None:
            ctrlShape = cmds.listRelatives(name, shapes=1)[0]
            cmds.setAttr('{}.overrideEnabled'.format(ctrlShape), 1)
            cmds.setAttr('{}.overrideColor'.format(ctrlShape), colorsDic[color])
        
        return name        

    elif type == 'box':
        ctrl=cmds.curve(d=1, p=[[-0.5, 0.5, 0.5], [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5],
                           [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [0.5, -0.5, -0.5],
                           [0.5, 0.5, -0.5], [0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5],
                           [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5]])
        cmds.rename(ctrl, name)
        if color != None:
            ctrlShape = cmds.listRelatives(name, shapes=1)[0]
            cmds.setAttr('{}.overrideEnabled'.format(ctrlShape), 1)
            cmds.setAttr('{}.overrideColor'.format(ctrlShape), colorsDic[color])
        
        return name

    elif type =='L':
        ctrl=cmds.curve(d=1, p=[[0.171, 0.0, 0.244], [-0.137, 0.0, 0.244], [-0.137, 0.0, -0.234], [-0.048, 0.0, -0.234],
                           [-0.048, 0.0, 0.162], [0.171, 0.0, 0.162], [0.171, 0.0, 0.244]])
        cmds.rename(ctrl, name)
        if color != None:
            ctrlShape = cmds.listRelatives(name, shapes=1)[0]
            cmds.setAttr('{}.overrideEnabled'.format(ctrlShape), 1)
            cmds.setAttr('{}.overrideColor'.format(ctrlShape), colorsDic[color])
        
        return name

    elif type == 'R':
        ctrl=cmds.curve(d=1, p=[[-0.097, 0.0, -0.03], [-0.037, 0.0, -0.03], [0.022, 0.0, -0.03], [0.046, 0.0, -0.03],
                           [0.08, 0.0, -0.037], [0.102, 0.0, -0.052], [0.112, 0.0, -0.076], [0.112, 0.0, -0.094],
                           [0.112, 0.0, -0.126], [0.072, 0.0, -0.155], [0.031, 0.0, -0.155], [-0.033, 0.0, -0.155],
                           [-0.097, 0.0, -0.155], [-0.097, 0.0, -0.093], [-0.097, 0.0, -0.03]])
        cmds.rename(ctrl, name)
        if color != None:
            ctrlShape = cmds.listRelatives(name, shapes=1)[0]
            cmds.setAttr('{}.overrideEnabled'.format(ctrlShape), 1)
            cmds.setAttr('{}.overrideColor'.format(ctrlShape), colorsDic[color])
        
        return name

    elif type == 'pin':
        ctrl=cmds.curve(d=1, p=[[0.0, 0.0, -0.5], [-0.17, 0.0, -0.57], [-0.25, 0.0, -0.75], [-0.17, 0.0, -0.93],
                           [0.0, 0.0, -1.0], [0.17, 0.0, -0.93], [0.25, 0.0, -0.75], [0.17, 0.0, -0.57],
                           [0.0, 0.0, -0.5], [0.0, 0.0, 0.0]])
        cmds.rename(ctrl, name)
        if color != None:
            ctrlShape = cmds.listRelatives(name, shapes=1)[0]
            cmds.setAttr('{}.overrideEnabled'.format(ctrlShape), 1)
            cmds.setAttr('{}.overrideColor'.format(ctrlShape), colorsDic[color])
        
        return name

    elif type == 'directionShape':
        ctrl=cmds.curve(d=1, p=[[1.4654943925052066e-14, 3.0, 0.0], [7.105427357601002e-15, 2.0, 2.0],
                           [-3.9968028886505635e-15, 0.0, 3.0], [-1.2434497875801753e-14, -2.0, 2.0],
                           [-1.4654943925052066e-14, -3.0, 0.0], [-7.105427357601002e-15, -2.0, -2.0],
                           [3.9968028886505635e-15, 0.0, -3.0], [1.2434497875801753e-14, 2.0, -2.0],
                           [1.4654943925052066e-14, 3.0, 0.0], [0.0, 0.0, 0.0], [4.0, -1.9539925233402755e-14, 5.329070518200751e-15]])
        cmds.rename(ctrl, name)
        if color != None:
            ctrlShape = cmds.listRelatives(name, shapes=1)[0]
            cmds.setAttr('{}.overrideEnabled'.format(ctrlShape), 1)
            cmds.setAttr('{}.overrideColor'.format(ctrlShape), colorsDic[color])
        
        return name