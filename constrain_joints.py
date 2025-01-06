import bpy

# Define joint limits for each bone
Project Structure:

├── __pycache__
│   └── workingfunctions.cpython-311.pyc
├── bone_mapping.py
├── brute.py
├── brute2.py
├── brute3.py
├── constrain_joints.py
├── debug_shader.py
├── filtered_list_bones.py
├── gpu_based.py
├── gpu_based_with_checks.py
├── hull test.py
├── hyperplane separation.py
├── list_bones.py
├── list_vertex_groups.py
├── map all.py
├── merge_info.py
├── meshcollision.py
├── meshcollision2.py
├── meshcollision3.py
├── meshcollision4.py
├── meshcollision5.py
├── meshcollision6.py
├── meshcollision7.py
├── mixamo-rig-joint-constraint
│   ├── README.md
│   ├── constrain_joints.py
│   └── pics
│       ├── collision 138.png
│       ├── left wrist twist 86.png
│       ├── right wrist twist 114.png
│       └── right wrist untwisted 114.png
├── onion_skin_attempt_1.py
├── onion_skin_attempt_2.py
├── raycast.py
├── raycast10.py
├── raycast11.py
├── raycast12.py
├── raycast13.py
├── raycast14.py
├── raycast15.py
├── raycast16.py
├── raycast17.py
├── raycast2.py
├── raycast3.py
├── raycast4.py
├── raycast5.py
├── raycast6.py
├── raycast7.py
├── raycast8.py
├── raycast9.py
├── sat.py
├── sat2.py
├── sat3D2.py
├── sat3d.py
├── sat3d10.py
├── sat3d11.py
├── sat3d12.py
├── sat3d13.py
├── sat3d14.py
├── sat3d15.py
├── sat3d3.py
├── sat3d4.py
├── sat3d5.py
├── sat3d6.py
├── sat3d7.py
├── sat3d8.py
├── sat3d9.py
├── satmesh.py
├── satmesh2.py
├── satmesh3.py
├── satmesh4.py
├── satmesh5.py
├── satmesh6.py
├── satmesh7.py
├── satmesh8.py
├── satmesh9.py
├── test_bvh.py
├── testbvh.py
├── testbvh2.py
├── vertex_group_onion_skin.py
├── winding number algorithm.py
└── workingfunctions.py


File Contents:

File: constrain_joints.py

import bpy

# Define joint limits for each bone
bone_constraints = {
    "mixamorig:Head": {"min_x": -40, "max_x": 40, "min_y": -30, "max_y": 30, "min_z": -60, "max_z": 60},
    "mixamorig:Neck": {"min_x": -45, "max_x": 45, "min_y": -20, "max_y": 20, "min_z": -70, "max_z": 70},
    "mixamorig:Spine": {"min_x": -20, "max_x": 20, "min_y": -10, "max_y": 10, "min_z": -15, "max_z": 15},
    "mixamorig:Spine1": {"min_x": -20, "max_x": 20, "min_y": -10, "max_y": 10, "min_z": -15, "max_z": 15},
    "mixamorig:Spine2": {"min_x": -20, "max_x": 20, "min_y": -10, "max_y": 10, "min_z": -15, "max_z": 15},
    "mixamorig:RightShoulder": {"min_x": -90, "max_x": 90, "min_y": -90, "max_y": 90, "min_z": -45, "max_z": 45},
    "mixamorig:LeftShoulder": {"min_x": -90, "max_x": 90, "min_y": -90, "max_y": 90, "min_z": -45, "max_z": 45},
    "mixamorig:RightArm": {"min_x": -45, "max_x": 90, "min_y": -45, "max_y": 90, "min_z": -90, "max_z": 90},
    "mixamorig:LeftArm": {"min_x": -45, "max_x": 90, "min_y": -45, "max_y": 90, "min_z": -90, "max_z": 90},
    "mixamorig:RightForeArm": {"min_x": 0, "max_x": 145, "min_y": 0, "max_y": 0, "min_z": -85, "max_z": 85},
    "mixamorig:LeftForeArm": {"min_x": 0, "max_x": 145, "min_y": 0, "max_y": 0, "min_z": -85, "max_z": 85},
    "mixamorig:Hips": {"min_x": -30, "max_x": 100, "min_y": -45, "max_y": 45, "min_z": -45, "max_z": 45},
    "mixamorig:RightUpLeg": {"min_x": -10, "max_x": 120, "min_y": -45, "max_y": 45, "min_z": -45, "max_z": 45},
    "mixamorig:LeftUpLeg": {"min_x": -10, "max_x": 120, "min_y": -45, "max_y": 45, "min_z": -45, "max_z": 45},
    "mixamorig:RightLeg": {"min_x": 0, "max_x": 135, "min_y": 0, "max_y": 0, "min_z": -10, "max_z": 10},
    "mixamorig:LeftLeg": {"min_x": 0, "max_x": 135, "min_y": 0, "max_y": 0, "min_z": -10, "max_z": 10},
    "mixamorig:RightFoot": {"min_x": -30, "max_x": 45, "min_y": -15, "max_y": 15, "min_z": -30, "max_z": 30},
    "mixamorig:LeftFoot": {"min_x": -30, "max_x": 45, "min_y": -15, "max_y": 15, "min_z": -30, "max_z": 30},
    "mixamorig:RightToeBase": {"min_x": -50, "max_x": 50, "min_y": -10, "max_y": 10, "min_z": -10, "max_z": 10},
    "mixamorig:LeftToeBase": {"min_x": -50, "max_x": 50, "min_y": -10, "max_y": 10, "min_z": -10, "max_z": 10},
    "mixamorig:RightHand": {"min_x": -60, "max_x": 60, "min_y": -20, "max_y": 30, "min_z": -40, "max_z": 40},
    "mixamorig:LeftHand": {"min_x": -60, "max_x": 60, "min_y": -20, "max_y": 30, "min_z": -40, "max_z": 40},
    "mixamorig:RightHandThumb1": {"min_x": 0, "max_x": 60, "min_y": -10, "max_y": 20, "min_z": -20, "max_z": 20},
    "mixamorig:RightHandThumb2": {"min_x": 0, "max_x": 80, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:RightHandThumb3": {"min_x": 0, "max_x": 80, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:RightHandIndex1": {"min_x": 0, "max_x": 90, "min_y": -10, "max_y": 10, "min_z": 0, "max_z": 0},
    "mixamorig:RightHandIndex2": {"min_x": 0, "max_x": 120, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:RightHandIndex3": {"min_x": 0, "max_x": 80, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:RightHandMiddle1": {"min_x": 0, "max_x": 90, "min_y": -10, "max_y": 10, "min_z": 0, "max_z": 0},
    "mixamorig:RightHandMiddle2": {"min_x": 0, "max_x": 120, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:RightHandMiddle3": {"min_x": 0, "max_x": 80, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:LeftHandThumb1": {"min_x": 0, "max_x": 60, "min_y": -10, "max_y": 20, "min_z": -20, "max_z": 20},
    "mixamorig:LeftHandThumb2": {"min_x": 0, "max_x": 80, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:LeftHandThumb3": {"min_x": 0, "max_x": 80, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:LeftHandIndex1": {"min_x": 0, "max_x": 90, "min_y": -10, "max_y": 10, "min_z": 0, "max_z": 0},
    "mixamorig:LeftHandIndex2": {"min_x": 0, "max_x": 120, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:LeftHandIndex3": {"min_x": 0, "max_x": 80, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:LefttHandMiddle1": {"min_x": 0, "max_x": 90, "min_y": -10, "max_y": 10, "min_z": 0, "max_z": 0},
    "mixamorig:LeftHandMiddle2": {"min_x": 0, "max_x": 120, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},
    "mixamorig:LefttHandMiddle3": {"min_x": 0, "max_x": 80, "min_y": 0, "max_y": 0, "min_z": 0, "max_z": 0},


}

class OBJECT_OT_AddLimitRotationConstraints(bpy.types.Operator):
    """Add Limit Rotation Constraints to Mixamo Armature"""
    bl_idname = "object.add_limit_rotation_constraints"
    bl_label = "Add Limit Rotation Constraints"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.object
        if obj is None or obj.type != 'ARMATURE':
            self.report({'ERROR'}, "Select an armature")
            return {'CANCELLED'}

        bpy.ops.object.mode_set(mode='POSE')

        for bone_name, limits in bone_constraints.items():
            if bone_name in obj.pose.bones:
                bone = obj.pose.bones[bone_name]
                constraint = bone.constraints.new(type='LIMIT_ROTATION')
                constraint.use_limit_x = True
                constraint.use_limit_y = True
                constraint.use_limit_z = True
                constraint.min_x = limits["min_x"] * (3.14159 / 180)  # Convert degrees to radians
                constraint.max_x = limits["max_x"] * (3.14159 / 180)
                constraint.min_y = limits["min_y"] * (3.14159 / 180)
                constraint.max_y = limits["max_y"] * (3.14159 / 180)
                constraint.min_z = limits["min_z"] * (3.14159 / 180)
                constraint.max_z = limits["max_z"] * (3.14159 / 180)
                constraint.owner_space = 'LOCAL'
        
        bpy.ops.object.mode_set(mode='OBJECT')
        self.report({'INFO'}, "Limit Rotation Constraints Added")
        return {'FINISHED'}


# Register the operator
def register():
    bpy.utils.register_class(OBJECT_OT_AddLimitRotationConstraints)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_AddLimitRotationConstraints)

if __name__ == "__main__":
    register()




class OBJECT_OT_AddLimitRotationConstraints(bpy.types.Operator):
    """Add Limit Rotation Constraints to Mixamo Armature"""
    bl_idname = "object.add_limit_rotation_constraints"
    bl_label = "Add Limit Rotation Constraints"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.object
        if obj is None or obj.type != 'ARMATURE':
            self.report({'ERROR'}, "Select an armature")
            return {'CANCELLED'}

        bpy.ops.object.mode_set(mode='POSE')

        for bone_name, limits in bone_constraints.items():
            if bone_name in obj.pose.bones:
                bone = obj.pose.bones[bone_name]
                constraint = bone.constraints.new(type='LIMIT_ROTATION')
                constraint.use_limit_x = True
                constraint.use_limit_y = True
                constraint.use_limit_z = True
                constraint.min_x = limits["min_x"] * (3.14159 / 180)  # Convert degrees to radians
                constraint.max_x = limits["max_x"] * (3.14159 / 180)
                constraint.min_y = limits["min_y"] * (3.14159 / 180)
                constraint.max_y = limits["max_y"] * (3.14159 / 180)
                constraint.min_z = limits["min_z"] * (3.14159 / 180)
                constraint.max_z = limits["max_z"] * (3.14159 / 180)
                constraint.owner_space = 'LOCAL'
        
        bpy.ops.object.mode_set(mode='OBJECT')
        self.report({'INFO'}, "Limit Rotation Constraints Added")
        return {'FINISHED'}


# Register the operator
def register():
    bpy.utils.register_class(OBJECT_OT_AddLimitRotationConstraints)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_AddLimitRotationConstraints)

if __name__ == "__main__":
    register()
