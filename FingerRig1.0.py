# Li Ling, FingerRig 1.0, for test and for fun~ :)  Only FK part for now, IK and switching please wait for update (Nov 26, 2018).
# Applicable for the Joints Structure named as the Motion builder standard. Character in T pose facing +Z

################################################################
# Get the size of Controller regarding to the size of finger.
import maya.cmds as mc
import math
import pymel.core as pm

TA = mc.xform("LocF5_1", q = True, t = True, ws = True)
TB = mc.xform("LocF5_2", q = True, t = True, ws = True)
print TA, TB
size = math.sqrt(math.pow((TB[0]-TA[0]),2)+math.pow((TB[1]-TA[1]),2)+math.pow((TB[2]-TA[2]),2))
print size

#def FingerRig():
# Create controller groups.
def CtrlUnit():
    CtrlUnit = mc.curve(n="FingerCurve", d = 1, p = [(0,0,0),(0,size,0),(size*0.2,size*1.2,0),(0,size*1.5,0),(size*-0.2,size*1.2,0),(0,size,0)])
    return CtrlUnit
    
mc.group (em = True, n = "FingerCtrlGrp_L")
# I know this loop looks wierd, I just instinctly feel I should prepare for cases like with different finger numbers. For now I don't want to optimize this part.
for i in range (0,15,1):
    if i == 0:
        mc.group (em = True, n = "FKCtrlGrp_Thumb_0_L")
        mc.parent ("FKCtrlGrp_Thumb_0_L","FingerCtrlGrp_0_L")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Thumb_1_L")
        mc.parent ("FKCtrl_Thumb_1_L","FKCtrlGrp_Thumb_0_L")
    elif i == 1:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Thumb_2_L")
        mc.parent ("FKCtrl_Thumb_2_L", "FKCtrl_Thumb_1_L")
    elif i == 2:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Thumb_3_L")
        mc.parent ("FKCtrl_Thumb_3_L", "FKCtrl_Thumb_2_L")
        # Thumb
    elif i == 3:
        mc.group (em = True, n = "FKCtrlGrp_Index_0_L")
        mc.parent ("FKCtrlGrp_Index_0_L","FingerCtrlGrp_0_L")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Index_1_L")
        mc.parent ("FKCtrl_Index_1_L","FKCtrlGrp_Index_0_L")
    elif i == 4:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Index_2_L")
        mc.parent ("FKCtrl_Index_2_L", "FKCtrl_Index_1_L")
    elif i == 5:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Index_3_L")
        mc.parent ("FKCtrl_Index_3_L", "FKCtrl_Index_2_L")
        # Index
    elif i == 6:
        mc.group (em = True, n = "FKCtrlGrp_Middle_0_L")
        mc.parent ("FKCtrlGrp_Middle_0_L","FingerCtrlGrp_0_L")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Middle_1_L")
        mc.parent ("FKCtrl_Middle_1_L", "FKCtrlGrp_Middle_0_L")
    elif i == 7:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Middle_2_L")
        mc.parent ("FKCtrl_Middle_2_L", "FKCtrl_Middle_1_L")
    elif i == 8:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Middle_3_L")
        mc.parent ("FKCtrl_Middle_3_L", "FKCtrl_Middle_2_L")
        # Middle
    elif i == 9:
        mc.group (em = True, n = "FKCtrlGrp_Ring_0_L")
        mc.parent ("FKCtrlGrp_Ring_0_L","FingerCtrlGrp_0_L")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Ring_1_L")
        mc.parent ("FKCtrl_Ring_1_L", "FKCtrlGrp_Ring_0_L")
    elif i == 10:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Ring_2_L")
        mc.parent ("FKCtrl_Ring_2_L", "FKCtrl_Ring_1_L")
    elif i == 11:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Ring_3_L")
        mc.parent ("FKCtrl_Ring_3_L", "FKCtrl_Ring_2_L")
        # Ring
    elif i == 12:
        mc.group (em = True, n = "FKCtrlGrp_Pinky_0_L")
        mc.parent ("FKCtrlGrp_Pinky_0_L","FingerCtrlGrp_0_L")
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Pinky_1_L")
        mc.parent ("FKCtrl_Pinky_1_L", "FKCtrlGrp_Pinky_0_L")
    elif i == 13:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Pinky_2_L")
        mc.parent ("FKCtrl_Pinky_2_L", "FKCtrl_Pinky_1_L")
    elif i == 14:
        CtrlUnit()
        mc.rename ("FingerCurve","FKCtrl_Pinky_3_L")
        mc.parent ("FKCtrl_Pinky_3_L", "FKCtrl_Pinky_2_L")
        # Pinky

# Place the controllers to the joints' position
mc.parentConstraint("LeftHand","FingerCtrlGrp_0_L")
mc.parentConstraint("LeftHandThumb1","FKCtrlGrp_Thumb_0_L", mo = False)
mc.pointConstraint("LeftHandThumb2", "FKCtrl_Thumb_2_L", mo = False)
mc.pointConstraint("LeftHandThumb3", "FKCtrl_Thumb_3_L", mo = False)

mc.parentConstraint("LeftHandIndex1","FKCtrlGrp_Index_0_L", mo = False)
mc.pointConstraint("LeftHandIndex2","FKCtrl_Index_2_L", mo = False)
mc.pointConstraint("LeftHandIndex3","FKCtrl_Index_3_L", mo = False)

mc.parentConstraint("LeftHandMiddle1","FKCtrlGrp_Middle_0_L", mo = False)
mc.pointConstraint("LeftHandMiddle2","FKCtrl_Middle_2_L", mo = False)
mc.pointConstraint("LeftHandMiddle3","FKCtrl_Middle_3_L", mo = False)

mc.parentConstraint("LeftHandRing1","FKCtrlGrp_Ring_0_L", mo = False)
mc.pointConstraint("LeftHandRing2","FKCtrl_Ring_2_L", mo = False)
mc.pointConstraint("LeftHandRing3","FKCtrl_Ring_3_L", mo = False)

mc.parentConstraint("LeftHandPinky1","FKCtrlGrp_Pinky_0_L", mo = False)
mc.pointConstraint("LeftHandPinky2","FKCtrl_Pinky_2_L", mo = False)
mc.pointConstraint("LeftHandPinky3","FKCtrl_Pinky_3_L", mo = False)

mc.delete("FingerCtrlGrp_0_L_parentConstraint1","FKCtrlGrp_Thumb_0_L_parentConstraint1","FKCtrlGrp_Index_0_L_parentConstraint1","FKCtrlGrp_Middle_0_L_parentConstraint1","FKCtrlGrp_Ring_0_L_parentConstraint1","FKCtrlGrp_Pinky_0_L_parentConstraint1", "FKCtrl_Thumb_2_L_pointConstraint1", "FKCtrl_Thumb_3_L_pointConstraint1", "FKCtrl_Index_2_L_pointConstraint1", "FKCtrl_Index_3_L_pointConstraint1", "FKCtrl_Middle_2_L_pointConstraint1", "FKCtrl_Middle_3_L_pointConstraint1", "FKCtrl_Ring_2_L_pointConstraint1", "FKCtrl_Ring_3_L_pointConstraint1", "FKCtrl_Pinky_2_L_pointConstraint1", "FKCtrl_Pinky_3_L_pointConstraint1")

# Mirror the Controller group and Freeze the transformation of controllers
mc.group (em = True, n = "TempFCtrlGrp", w = True)
mc.duplicate ("FingerCtrlGrp_0_L")
mc.parent ( "FingerCtrlGrp_1_L", "TempFCtrlGrp")
mc.scale ("TempFCtrlGrp", x = -1)
mc.select (hi = True)
RenameList = pm.ls(sl=True)

for i in RenameList:
    Rename = i.nodeName().replace("_L_", "_R_")
    i.rename(Rename)

mc.rename ('FingerCtrlGrp_1_R','FingerCtrlGrp_0_R')
mc.setAttr ('TempFCtrlGrp' + '.scaleX', -1)
mc.ungroup ("TempFCtrlGrp")

F = ["FKCtrl_Thumb_1_L", "FKCtrl_Index_1_L", "FKCtrl_Middle_1_L","FKCtrl_Ring_1_L", "FKCtrl_Pinky_1_L", "FKCtrl_Thumb_1_R", "FKCtrl_Index_1_R", "FKCtrl_Middle_1_R", "FKCtrl_Ring_1_R", "FKCtrl_Pinky_1_R"]

for i in range(0,len(F),1):
    mc.makeIdentity (F[i], apply = True, translate = True)

# Constraint the Controller goup and the Joints
mc.parentConstraint ("LeftHand", "FingerCtrlGrp_0_L", mo = True)

mc.parentConstraint ("FKCtrl_Thumb_1_L", "LeftHandThumb1", mo = True)
mc.parentConstraint ("FKCtrl_Thumb_2_L", "LeftHandThumb2", mo = True)
mc.parentConstraint ("FKCtrl_Thumb_3_L", "LeftHandThumb3", mo = True)

mc.parentConstraint ("FKCtrl_Index_1_L", "LeftHandIndex1", mo = True)
mc.parentConstraint ("FKCtrl_Index_2_L", "LeftHandIndex2", mo = True)
mc.parentConstraint ("FKCtrl_Index_3_L", "LeftHandIndex3", mo = True)

mc.parentConstraint ("FKCtrl_Middle_1_L", "LeftHandMiddle1", mo = True)
mc.parentConstraint ("FKCtrl_Middle_2_L", "LeftHandMiddle2", mo = True)
mc.parentConstraint ("FKCtrl_Middle_3_L", "LeftHandMiddle3", mo = True)

mc.parentConstraint ("FKCtrl_Ring_1_L", "LeftHandRing1", mo = True)
mc.parentConstraint ("FKCtrl_Ring_2_L", "LeftHandRing2", mo = True)
mc.parentConstraint ("FKCtrl_Ring_3_L", "LeftHandRing3", mo = True)

mc.parentConstraint ("FKCtrl_Pinky_1_L", "LeftHandPinky1", mo = True)
mc.parentConstraint ("FKCtrl_Pinky_2_L", "LeftHandPinky2", mo = True)
mc.parentConstraint ("FKCtrl_Pinky_3_L", "LeftHandPinky3", mo = True)

mc.parentConstraint ("RightHand", "FingerCtrlGrp_0_R", mo = True)

mc.parentConstraint ("FKCtrl_Thumb_1_R", "RightHandThumb1", mo = True)
mc.parentConstraint ("FKCtrl_Thumb_2_R", "RightHandThumb2", mo = True)
mc.parentConstraint ("FKCtrl_Thumb_3_R", "RightHandThumb3", mo = True)

mc.parentConstraint ("FKCtrl_Index_1_R", "RightHandIndex1", mo = True)
mc.parentConstraint ("FKCtrl_Index_2_R", "RightHandIndex2", mo = True)
mc.parentConstraint ("FKCtrl_Index_3_R", "RightHandIndex3", mo = True)

mc.parentConstraint ("FKCtrl_Middle_1_R", "RightHandMiddle1", mo = True)
mc.parentConstraint ("FKCtrl_Middle_2_R", "RightHandMiddle2", mo = True)
mc.parentConstraint ("FKCtrl_Middle_3_R", "RightHandMiddle3", mo = True)

mc.parentConstraint ("FKCtrl_Ring_1_R", "RightHandRing1", mo = True)
mc.parentConstraint ("FKCtrl_Ring_2_R", "RightHandRing2", mo = True)
mc.parentConstraint ("FKCtrl_Ring_3_R", "RightHandRing3", mo = True)

mc.parentConstraint ("FKCtrl_Pinky_1_R", "RightHandPinky1", mo = True)
mc.parentConstraint ("FKCtrl_Pinky_2_R", "RightHandPinky2", mo = True)
mc.parentConstraint ("FKCtrl_Pinky_3_R", "RightHandPinky3", mo = True)

#########################################################################
