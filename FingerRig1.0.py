# Li Ling, FingerRig 1.0, for test and for fun~ :)  Only FK part for now, IK and switching please wait for update (Nov 26, 2018).
# Applicable for the Joints Structure named as the Motion builder standard. Character in T pose facing +Z

################################################################
# Get the size of Controller regarding to the size of finger.
import maya.cmds as mc
import math
import pymel.core as pm

TA = mc.xform("LeftHandPinky1", q = True, t = True, ws = True)
TB = mc.xform("LeftHandPinky2", q = True, t = True, ws = True)
print TA, TB
size = math.sqrt(math.pow((TB[0]-TA[0]),2)+math.pow((TB[1]-TA[1]),2)+math.pow((TB[2]-TA[2]),2))
print size

#def FingerRig():
# Create controller groups.
def CtrlUnit():
    CtrlUnit = mc.curve(n="FingerCurve", d = 1, p = [(0,0,0),(0,size,0),(size*0.2,size*1.2,0),(0,size*1.5,0),(size*-0.2,size*1.2,0),(0,size,0)])
    return CtrlUnit
    
mc.group (em = True, n = "FingerCtrlGrp_L_0")
for i in range (0,15,1):
    if i == 0:
        mc.group (em = True, n = "FKCtrlGrp_Thumb_L_0")
        mc.parent ("FKCtrlGrp_Thumb_L_0","FingerCtrlGrp_L_0")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Thumb_L_1")
        mc.parent ("FKCtrl_Thumb_L_1","FKCtrlGrp_Thumb_L_0")
    elif i == 1:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Thumb_L_2")
        mc.parent ("FKCtrl_Thumb_L_2", "FKCtrl_Thumb_L_1")
    elif i == 2:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Thumb_L_3")
        mc.parent ("FKCtrl_Thumb_L_3", "FKCtrl_Thumb_L_2")
        # Thumb
    elif i == 3:
        mc.group (em = True, n = "FKCtrlGrp_Index_L_0")
        mc.parent ("FKCtrlGrp_Index_L_0","FingerCtrlGrp_L_0")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Index_L_1")
        mc.parent ("FKCtrl_Index_L_1","FKCtrlGrp_Index_L_0")
    elif i == 4:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Index_L_2")
        mc.parent ("FKCtrl_Index_L_2", "FKCtrl_Index_L_1")
    elif i == 5:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Index_L_3")
        mc.parent ("FKCtrl_Index_L_3", "FKCtrl_Index_L_2")
        # Index
    elif i == 6:
        mc.group (em = True, n = "FKCtrlGrp_Middle_L_0")
        mc.parent ("FKCtrlGrp_Middle_L_0","FingerCtrlGrp_L_0")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Middle_L_1")
        mc.parent ("FKCtrl_Middle_L_1", "FKCtrlGrp_Middle_L_0")
    elif i == 7:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Middle_L_2")
        mc.parent ("FKCtrl_Middle_L_2", "FKCtrl_Middle_L_1")
    elif i == 8:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Middle_L_3")
        mc.parent ("FKCtrl_Middle_L_3", "FKCtrl_Middle_L_2")
        # Middle
    elif i == 9:
        mc.group (em = True, n = "FKCtrlGrp_Ring_L_0")
        mc.parent ("FKCtrlGrp_Ring_L_0","FingerCtrlGrp_L_0")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Ring_L_1")
        mc.parent ("FKCtrl_Ring_L_1", "FKCtrlGrp_Ring_L_0")
    elif i == 10:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Ring_L_2")
        mc.parent ("FKCtrl_Ring_L_2", "FKCtrl_Ring_L_1")
    elif i == 11:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Ring_L_3")
        mc.parent ("FKCtrl_Ring_L_3", "FKCtrl_Ring_L_2")
        # Ring
    elif i == 12:
        mc.group (em = True, n = "FKCtrlGrp_Pinky_L_0")
        mc.parent ("FKCtrlGrp_Pinky_L_0","FingerCtrlGrp_L_0")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Pinky_L_1")
        mc.parent ("FKCtrl_Pinky_L_1", "FKCtrlGrp_Pinky_L_0")
    elif i == 13:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Pinky_L_2")
        mc.parent ("FKCtrl_Pinky_L_2", "FKCtrl_Pinky_L_1")
    elif i == 14:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Pinky_L_3")
        mc.parent ("FKCtrl_Pinky_L_3", "FKCtrl_Pinky_L_2")
        # Pinky

# Place the controllers to the joints' position
mc.parentConstraint("LeftHand","FingerCtrlGrp_L_0")
mc.parentConstraint("LeftHandThumb1","FKCtrlGrp_Thumb_L_0", mo = False)
mc.pointConstraint("LeftHandThumb2", "FKCtrl_Thumb_L_2", mo = False)
mc.pointConstraint("LeftHandThumb3", "FKCtrl_Thumb_L_3", mo = False)

mc.parentConstraint("LeftHandIndex1","FKCtrlGrp_Index_L_0", mo = False)
mc.pointConstraint("LeftHandIndex2","FKCtrl_Index_L_2", mo = False)
mc.pointConstraint("LeftHandIndex3","FKCtrl_Index_L_3", mo = False)

mc.parentConstraint("LeftHandMiddle1","FKCtrlGrp_Middle_L_0", mo = False)
mc.pointConstraint("LeftHandMiddle2","FKCtrl_Middle_L_2", mo = False)
mc.pointConstraint("LeftHandMiddle3","FKCtrl_Middle_L_3", mo = False)

mc.parentConstraint("LeftHandRing1","FKCtrlGrp_Ring_L_0", mo = False)
mc.pointConstraint("LeftHandRing2","FKCtrl_Ring_L_2", mo = False)
mc.pointConstraint("LeftHandRing3","FKCtrl_Ring_L_3", mo = False)

mc.parentConstraint("LeftHandPinky1","FKCtrlGrp_Pinky_L_0", mo = False)
mc.pointConstraint("LeftHandPinky2","FKCtrl_Pinky_L_2", mo = False)
mc.pointConstraint("LeftHandPinky3","FKCtrl_Pinky_L_3", mo = False)

mc.delete("FingerCtrlGrp_L_0_parentConstraint1","FKCtrlGrp_Thumb_L_0_parentConstraint1","FKCtrlGrp_Index_L_0_parentConstraint1","FKCtrlGrp_Middle_L_0_parentConstraint1","FKCtrlGrp_Ring_L_0_parentConstraint1","FKCtrlGrp_Pinky_L_0_parentConstraint1", "FKCtrl_Thumb_L_2_pointConstraint1", "FKCtrl_Thumb_L_3_pointConstraint1", "FKCtrl_Index_L_2_pointConstraint1", "FKCtrl_Index_L_3_pointConstraint1", "FKCtrl_Middle_L_2_pointConstraint1", "FKCtrl_Middle_L_3_pointConstraint1", "FKCtrl_Ring_L_2_pointConstraint1", "FKCtrl_Ring_L_3_pointConstraint1", "FKCtrl_Pinky_L_2_pointConstraint1", "FKCtrl_Pinky_L_3_pointConstraint1")

# Mirror the Controller group and Freeze the transformation of controllers
mc.group (em = True, n = "TempFCtrlGrp", w = True)
mc.duplicate ("FingerCtrlGrp_L_0")
mc.parent ( "FingerCtrlGrp_L_1", "TempFCtrlGrp")
mc.scale ("TempFCtrlGrp", x = -1)
mc.select (hi = True)
RenameList = pm.ls(sl=True)

for i in RenameList:
    Rename = i.nodeName().replace("_L_", "_R_")
    i.rename(Rename)

mc.rename ('FingerCtrlGrp_R_1','FingerCtrlGrp_R_0')
mc.setAttr ('TempFCtrlGrp' + '.scaleX', -1)
mc.ungroup ("TempFCtrlGrp")

F = ["FKCtrl_Thumb_L_1", "FKCtrl_Index_L_1", "FKCtrl_Middle_L_1","FKCtrl_Ring_L_1", "FKCtrl_Pinky_L_1", "FKCtrl_Thumb_R_1", "FKCtrl_Index_R_1", "FKCtrl_Middle_R_1", "FKCtrl_Ring_R_1", "FKCtrl_Pinky_R_1"]

for i in range(0,len(F),1):
    mc.makeIdentity (F[i], apply = True, translate = True)

# Constraint the Controller goup and the Joints
mc.parentConstraint ("LeftHand", "FingerCtrlGrp_L_0", mo = True)

mc.parentConstraint ("FKCtrl_Thumb_L_1", "LeftHandThumb1", mo = True)
mc.parentConstraint ("FKCtrl_Thumb_L_2", "LeftHandThumb2", mo = True)
mc.parentConstraint ("FKCtrl_Thumb_L_3", "LeftHandThumb3", mo = True)

mc.parentConstraint ("FKCtrl_Index_L_1", "LeftHandIndex1", mo = True)
mc.parentConstraint ("FKCtrl_Index_L_2", "LeftHandIndex2", mo = True)
mc.parentConstraint ("FKCtrl_Index_L_3", "LeftHandIndex3", mo = True)

mc.parentConstraint ("FKCtrl_Middle_L_1", "LeftHandMiddle1", mo = True)
mc.parentConstraint ("FKCtrl_Middle_L_2", "LeftHandMiddle2", mo = True)
mc.parentConstraint ("FKCtrl_Middle_L_3", "LeftHandMiddle3", mo = True)

mc.parentConstraint ("FKCtrl_Ring_L_1", "LeftHandRing1", mo = True)
mc.parentConstraint ("FKCtrl_Ring_L_2", "LeftHandRing2", mo = True)
mc.parentConstraint ("FKCtrl_Ring_L_3", "LeftHandRing3", mo = True)

mc.parentConstraint ("FKCtrl_Pinky_L_1", "LeftHandPinky1", mo = True)
mc.parentConstraint ("FKCtrl_Pinky_L_2", "LeftHandPinky2", mo = True)
mc.parentConstraint ("FKCtrl_Pinky_L_3", "LeftHandPinky3", mo = True)

mc.parentConstraint ("RightHand", "FingerCtrlGrp_R_0", mo = True)

mc.parentConstraint ("FKCtrl_Thumb_R_1", "RightHandThumb1", mo = True)
mc.parentConstraint ("FKCtrl_Thumb_R_2", "RightHandThumb2", mo = True)
mc.parentConstraint ("FKCtrl_Thumb_R_3", "RightHandThumb3", mo = True)

mc.parentConstraint ("FKCtrl_Index_R_1", "RightHandIndex1", mo = True)
mc.parentConstraint ("FKCtrl_Index_R_2", "RightHandIndex2", mo = True)
mc.parentConstraint ("FKCtrl_Index_R_3", "RightHandIndex3", mo = True)

mc.parentConstraint ("FKCtrl_Middle_R_1", "RightHandMiddle1", mo = True)
mc.parentConstraint ("FKCtrl_Middle_R_2", "RightHandMiddle2", mo = True)
mc.parentConstraint ("FKCtrl_Middle_R_3", "RightHandMiddle3", mo = True)

mc.parentConstraint ("FKCtrl_Ring_R_1", "RightHandRing1", mo = True)
mc.parentConstraint ("FKCtrl_Ring_R_2", "RightHandRing2", mo = True)
mc.parentConstraint ("FKCtrl_Ring_R_3", "RightHandRing3", mo = True)

mc.parentConstraint ("FKCtrl_Pinky_R_1", "RightHandPinky1", mo = True)
mc.parentConstraint ("FKCtrl_Pinky_R_2", "RightHandPinky2", mo = True)
mc.parentConstraint ("FKCtrl_Pinky_R_3", "RightHandPinky3", mo = True)

#########################################################################