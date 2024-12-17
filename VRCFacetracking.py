bl_info = {
    "name": "VRCFT Shapekeys Extended",
    "author": "Frenetic Furry! (forked from Adjerry91)",
    "version": (0,0,1),
    "blender": (4,2,4),
    "location": "View3d > Tool",
    "category": "Shape Keys",
}

import bpy
from bpy.types import Scene, Panel, Operator
from bpy.props import EnumProperty, StringProperty

# -------------------------------------------------------------------
# VRChat Facetracking Partial Shapekeyz List   
# -------------------------------------------------------------------

VRCFT_Labels_Partial_Unsplit = [
    "EyeClosed",
    "EyeWide",
    "EyeSquint",
    "CheekPuff",
    "CheekSuck",
    "JawOpen",
    "MouthClosed",
    "JawRight",
    "JawLeft",
    "JawForward",
    "LipSuck",
    "LipSuckCorner",
    "LipPucker",
    "MouthUpperUp",
    "MouthLowerDown",
    "MouthSmile",
    "MouthSad",
    "TongueOut",
    "TongueUp",
    "TongueDown",
    "TongueRight",
    "TongueLeft",
    "TongueRoll",
    "TongueBendDown",
    "TongueCurlUp",
    "TongueSquish",
    "TongueFlat",
    "TongueTwistRight",
    "TongueTwistLeft"
    ]

VRCFT_Labels_Partial_Split = [
    "EyeClosedRight",
    "EyeClosedLeft",
    "EyeWideRight",
    "EyeWideLeft",
    "EyeSquintRight",
    "EyeSquintLeft",
    "CheekPuffRight",
    "CheekPuffLeft",
    "CheekSuckRight",
    "CheekSuckLeft",
    "JawOpen",
    "MouthClosed",
    "JawRight",
    "JawLeft",
    "JawForward",
    "LipSuckUpperRight",
    "LipSuckUpperLeft",
    "LipSuckLowerRight",
    "LipSuckLowerLeft",
    "LipSuckCornerRight",
    "LipSuckCornerLeft",
    "LipPuckerUpperRight",
    "LipPuckerUpperLeft",
    "LipPuckerLowerRight",
    "LipPuckerLowerLeft",
    "MouthUpperUpRight",
    "MouthUpperUpLeft",
    "MouthLowerDownRight",
    "MouthLowerDownLeft",
    "MouthSmileRight",
    "MouthSmileLeft",
    "MouthSadRight",
    "MouthSadLeft",
    "TongueOut",
    "TongueUp",
    "TongueDown",
    "TongueRight",
    "TongueLeft",
    "TongueRoll",
    "TongueBendDown",
    "TongueCurlUp",
    "TongueSquish",
    "TongueFlat",
    "TongueTwistRight",
    "TongueTwistLeft"
]

# -------------------------------------------------------------------
# VRChat Facetracking Full Shapekeyz List   
# -------------------------------------------------------------------

VRCFT_Labels_Full_Unsplit = [
    "EyeLookOut",
    "EyeLookUp",
    "EyeLookDown",
    "EyeLookIn",
    "EyeClosed",
    "EyeSquint",
    "EyeWide",
    "EyeDilation",
    "EyeConstrict",
    "BrowPinch",
    "BrowDown",
    "BrowUp",
    "BrowInnerUp",
    "BrowOuterUp",
    "NoseSneer",
    "NasalDilation",
    "NasalConstrict",
    "CheekSquint",
    "CheekPuff",
    "CheekSuck",
    "JawOpen",
    "MouthClosed",
    "JawRight",
    "JawLeft",
    "JawForward",
    "JawBackward",
    "JawClench",
    "LipSuck",
    "LipSuckCorner",
    "LipFunnel",
    "LipPucker",
    "MouthUpperUp",
    "MouthLowerDown",
    "MouthUpperDeepen",
    "MouthLower",
    "MouthCornerPull",
    "MouthCornerSlant",
    "MouthFrown",
    "MouthStretch",
    "MouthDimple",
    "MouthPress",
    "MouthTightener",
    "TongueOut",
    "TongueUp",
    "TongueDown",
    "TongueRight",
    "TongueLeft",
    "TongueRoll",
    "TongueBendDown",
    "TongueCurlUp",
    "TongueSquish",
    "TongueFlat",
    "TongueTwistRight",
    "TongueTwistLeft",
    "MouthRight",
    "MouthLeft",
    "MouthSmile",
    "MouthSad",
]

VRCFT_Labels_Full_Split = [
    "EyeLookOutRight",
    "EyeLookInRight",
    "EyeLookUpRight",
    "EyeLookDownRight",
    "EyeLookOutLeft",
    "EyeLookInLeft",
    "EyeLookUpLeft",
    "EyeLookDownLeft",
    "EyeClosedRight",
    "EyeClosedLeft",
    "EyeSquintRight",
    "EyeSquintLeft",
    "EyeWideRight",
    "EyeWideLeft",
    "EyeDilationRight",
    "EyeDilationLeft",
    "EyeConstrictRight",
    "EyeConstrictLeft",
    "BrowPinchRight",
    "BrowPinchLeft",
    "BrowLowererRight",
    "BrowLowererLeft",
    "BrowInnerUpRight",
    "BrowInnerUpLeft",
    "BrowOuterUpRight",
    "BrowOuterUpLeft",
    "NoseSneerRight",
    "NoseSneerLeft",
    "NasalDilationRight",
    "NasalDilationLeft",
    "NasalConstrictRight",
    "NasalConstrictLeft",
    "CheekSquintRight",
    "CheekSquintLeft",
    "CheekPuffRight",
    "CheekPuffLeft",
    "CheekSuckRight",
    "CheekSuckLeft",
    "JawOpen",
    "MouthClosed",
    "JawRight",
    "JawLeft",
    "JawForward",
    "JawBackward",
    "JawClench",
    "LipSuckUpperRight",
    "LipSuckUpperLeft",
    "LipSuckLowerRight",
    "LipSuckLowerLeft",
    "LipSuckCornerRight",
    "LipSuckCornerLeft",
    "LipFunnelUpperRight",
    "LipFunnelUpperLeft",
    "LipFunnelLowerRight",
    "LipFunnelLowerLeft",
    "LipPuckerUpperRight",
    "LipPuckerUpperLeft",
    "LipPuckerLowerRight",
    "LipPuckerLowerLeft",
    "MouthUpperUpRight",
    "MouthUpperUpLeft",
    "MouthLowerDownRight",
    "MouthLowerDownLeft",
    "MouthUpperDeepenRight",
    "MouthUpperDeepenLeft",
    "MouthUpperRight",
    "MouthUpperLeft",
    "MouthLowerRight",
    "MouthLowerLeft",
    "MouthCornerPullRight",
    "MouthCornerPullLeft",
    "MouthCornerSlantRight",
    "MouthCornerSlantLeft",
    "MouthFrownRight",
    "MouthFrownLeft",
    "MouthStretchRight",
    "MouthStretchLeft",
    "MouthDimpleRight",
    "MouthDimpleLeft",
    "MouthPressRight",
    "MouthPressLeft",
    "MouthTightenerRight",
    "MouthTightenerLeft",
    "TongueOut",
    "TongueUp",
    "TongueDown",
    "TongueRight",
    "TongueLeft",
    "TongueRoll",
    "TongueBendDown",
    "TongueCurlUp",
    "TongueSquish",
    "TongueFlat",
    "TongueTwistRight",
    "TongueTwistLeft",
    "BrowDownRight",
    "BrowDownLeft",
    "BrowUpRight",
    "BrowUpLeft",
    "MouthSmileRight",
    "MouthSmileLeft",
    "MouthSadRight",
    "MouthSadLeft"
]

# -------------------------------------------------------------------
# Memory List (so when switching modes eg. Partial, Full, etc it wont save the deleted keys and will refresh instead)
# -------------------------------------------------------------------

VRCFT_PU_OG = VRCFT_Labels_Partial_Unsplit.copy()
VRCFT_PS_OG = VRCFT_Labels_Partial_Split.copy()
VRCFT_FU_OG = VRCFT_Labels_Full_Unsplit.copy()
VRCFT_FS_OG = VRCFT_Labels_Full_Split.copy()

# -------------------------------------------------------------------
# Bunch o' stuff that im not going to explain
# -------------------------------------------------------------------

def update_mode(self, context):
    global VRCFT_Labels_Partial_Unsplit, VRCFT_Labels_Partial_Split
    global VRCFT_Labels_Full_Unsplit, VRCFT_Labels_Full_Split
    
    if context.scene.vrcft_mode == 'FULL':
        VRCFT_Labels_Full_Unsplit = VRCFT_FU_OG.copy()
        VRCFT_Labels_Full_Split = VRCFT_FS_OG.copy()
    else:
        VRCFT_Labels_Partial_Unsplit = VRCFT_PU_OG.copy()
        VRCFT_Labels_Partial_Split = VRCFT_PS_OG.copy()

def update_split(self, context):
    update_mode(self, context)

def get_meshes(self, context):
    return [(obj.name, obj.name, obj.name) for obj in bpy.context.view_layer.objects if obj.type == 'MESH']

def get_shapekeys(self, context):
    mesh = bpy.context.view_layer.objects.get(context.scene.vrcft_mesh)
    if not mesh or not mesh.data.shape_keys:
        return []
    return [(sk.name, sk.name, '') for sk in mesh.data.shape_keys.key_blocks]

def get_the_sus(self, context):
    mesh = bpy.context.view_layer.objects.get(context.scene.vrcft_mesh)
    if not mesh:
        return [('NONE', 'None', '')]
    return [('NONE', 'None', '')] + [(vg.name, vg.name, '') for vg in mesh.vertex_groups]

def get_the_among_us(context):
    if context.scene.vrcft_mode == 'FULL':
        return VRCFT_Labels_Full_Unsplit if context.scene.vrcft_split == 'UNSPLIT' else VRCFT_Labels_Full_Split
    return VRCFT_Labels_Partial_Unsplit if context.scene.vrcft_split == 'UNSPLIT' else VRCFT_Labels_Partial_Split

class VRCFTCreateShapeKeys(Operator):
    bl_label = "Create VRCFT Shape Keys"
    bl_idname = "vrcft.create_shapekeys"
    bl_description = "Creates VRCFT Shapekeys"

    def execute(self, context):
        mesh = bpy.context.view_layer.objects[context.scene.vrcft_mesh]
        bpy.context.view_layer.objects.active = mesh
        active_list = get_the_among_us(context)

        if not mesh.data.shape_keys:
            self.report({'WARNING'}, "No shape keys found on mesh")
            return {'FINISHED'}

        separator_name = f"-~{{{context.scene.vrcft_username}}}~-"
        if separator_name not in mesh.data.shape_keys.key_blocks:
            mesh.shape_key_add(name=separator_name)

        existing_keys = [key.name for key in mesh.data.shape_keys.key_blocks]

        for key in mesh.data.shape_keys.key_blocks:
            key.value = 0

        for i, label in enumerate(active_list):
            source_key = getattr(context.scene, f"vrcft_shapekeys_{i}")
            vertex_group = getattr(context.scene, f"vrcft_vertex_groups_{i}")

            if label in existing_keys and source_key == "Basis":
                continue

            if label not in existing_keys:
                target_key = mesh.shape_key_add(name=label)
            else:
                target_key = mesh.data.shape_keys.key_blocks[label]

            if vertex_group != 'NONE':
                target_key.vertex_group = vertex_group

            if source_key != "Basis":
                for vert_idx in range(len(target_key.data)):
                    target_key.data[vert_idx].co = mesh.data.shape_keys.key_blocks['Basis'].data[vert_idx].co

                source_shape = mesh.data.shape_keys.key_blocks[source_key]
                source_shape.value = 1.0

                bpy.context.view_layer.objects.active = mesh
                mesh.active_shape_key_index = mesh.data.shape_keys.key_blocks.find(label)
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.blend_from_shape(shape=source_key, blend=1.0)
                bpy.ops.object.mode_set(mode='OBJECT')

                source_shape.value = 0.0

        mesh.active_shape_key_index = 0
        return {'FINISHED'}


class VRCFTRemoveShapeKeys(Operator):
    bl_label = "Remove VRCFT Shape Keys"
    bl_idname = "vrcft.remove_shapekeys"
    bl_description = "Removes all VRCFT shape keys from the selected mesh"

    def execute(self, context):
        mesh = bpy.context.view_layer.objects[context.scene.vrcft_mesh]
        bpy.context.view_layer.objects.active = mesh

        if not mesh.data.shape_keys:
            self.report({'WARNING'}, "No shape keys found on mesh")
            return {'FINISHED'}

        separator_name = f"-~{{{context.scene.vrcft_username}}}~-"
        all_lists = VRCFT_Labels_Partial_Unsplit + VRCFT_Labels_Partial_Split + VRCFT_Labels_Full_Unsplit + VRCFT_Labels_Full_Split

        for key in mesh.data.shape_keys.key_blocks[:]:
            if key.name in all_lists or key.name == separator_name:
                mesh.shape_key_remove(key)

        self.report({'INFO'}, "VRCFT shapekeys have been removed")
        return {'FINISHED'}

class VRCFTClearNonVRCFT(Operator):
    bl_label = "Clear Non-VRCFT Shape Keys"
    bl_idname = "vrcft.clear_non_vrcft"
    bl_description = "Removes all shape keys except Basis and VRCFT shape keys"

    def execute(self, context):
        mesh = bpy.context.view_layer.objects[context.scene.vrcft_mesh]
        bpy.context.view_layer.objects.active = mesh

        if not mesh.data.shape_keys:
            self.report({'WARNING'}, "No shape keys found on mesh")
            return {'FINISHED'}

        separator_name = f"-~{{{context.scene.vrcft_username}}}~-"
        all_lists = VRCFT_Labels_Partial_Unsplit + VRCFT_Labels_Partial_Split + VRCFT_Labels_Full_Unsplit + VRCFT_Labels_Full_Split
        protected_keys = ['Basis'] + all_lists + [separator_name]

        for key in mesh.data.shape_keys.key_blocks[:]:
            if key.name not in protected_keys:
                mesh.shape_key_remove(key)

        self.report({'INFO'}, "Non-VRCFT shapekeys have been removed")
        return {'FINISHED'}

class VRCFTRemoveKey(Operator):
    bl_label = "Remove Entry"
    bl_idname = "vrcft.remove_single"
    bl_description = "Remove this shape key entry"
    
    index: bpy.props.IntProperty()
    label: bpy.props.StringProperty()
    
    def execute(self, context):
        active_list = get_the_among_us(context)
        if self.label in active_list:
            active_list.remove(self.label)
        return {'FINISHED'}

class VRCFT_UL(Panel):
    bl_label = "VRCFT Shapekeys"
    bl_idname = "VRCFT Shapekeys"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "VRCFT-SK"

    def draw(self, context):
        layout = self.layout
        mesh = bpy.context.view_layer.objects.get(context.scene.vrcft_mesh)

        layout.prop(context.scene, 'vrcft_username', icon='USER')
        layout.prop(context.scene, 'vrcft_mesh', icon='MESH_DATA')
        layout.prop(context.scene, 'vrcft_mode')
        layout.prop(context.scene, 'vrcft_split')

        if mesh and mesh.data.shape_keys:
            layout.label(text='Select ShapeKeys & Vertex groups to create VRCFT ShapeKeys.', icon='INFO')
            box = layout.box()
            active_list = get_the_among_us(context)

            for i, label in enumerate(active_list):
                row = box.row(align=True)
                row.label(text=f"{label}:")
                col = row.column()
                col.prop(context.scene, f'vrcft_shapekeys_{i}', icon='SHAPEKEY_DATA')
                col = row.column()
                col.prop(context.scene, f'vrcft_vertex_groups_{i}', icon='GROUP_VERTEX')
                remove_op = row.operator("vrcft.remove_single", icon='X', text="")
                remove_op.index = i
                remove_op.label = label

            row = layout.row()
            row.operator("vrcft.create_shapekeys", icon='MESH_MONKEY')
            row = layout.row()
            row.operator("vrcft.remove_shapekeys", icon='X')
            row = layout.row()
            row.operator("vrcft.clear_non_vrcft", icon='TRASH')
        else:
            layout.label(text='Select the mesh with face shape keys.', icon='INFO')

def register():
    bpy.utils.register_class(VRCFTCreateShapeKeys)
    bpy.utils.register_class(VRCFTRemoveShapeKeys)
    bpy.utils.register_class(VRCFTClearNonVRCFT)
    bpy.utils.register_class(VRCFTRemoveKey)
    bpy.utils.register_class(VRCFT_UL)

    Scene.vrcft_username = StringProperty(
        name="Username",
        default="VRChat Face Tracking"
    )
    Scene.vrcft_mesh = EnumProperty(name='Mesh', items=get_meshes)
    Scene.vrcft_mode = EnumProperty(
        name="Mode",
        items=[
            ('PARTIAL', "Partial", "Use partial shape key list"),
            ('FULL', "Full", "Use full shape key list")
        ],
        default='PARTIAL',
        update=update_mode
    )
    Scene.vrcft_split = EnumProperty(
        name="Splitting",
        items=[
            ('UNSPLIT', "Unsplit", "Use unsplit shape key list"),
            ('SPLIT', "Split", "Use split shape key list")
        ],
        default='UNSPLIT',
        update=update_split
    )

    max_length = max(
        len(VRCFT_Labels_Partial_Unsplit),
        len(VRCFT_Labels_Partial_Split),
        len(VRCFT_Labels_Full_Unsplit),
        len(VRCFT_Labels_Full_Split)
    )

    for i in range(max_length):
        setattr(Scene, f"vrcft_shapekeys_{i}", EnumProperty(name='', items=get_shapekeys))
        setattr(Scene, f"vrcft_vertex_groups_{i}", EnumProperty(name='', items=get_the_sus))

def unregister():
    bpy.utils.unregister_class(VRCFTCreateShapeKeys)
    bpy.utils.unregister_class(VRCFTRemoveShapeKeys)
    bpy.utils.unregister_class(VRCFTClearNonVRCFT)
    bpy.utils.unregister_class(VRCFTRemoveKey)
    bpy.utils.unregister_class(VRCFT_UL)

    del Scene.vrcft_username
    del Scene.vrcft_mesh
    del Scene.vrcft_mode
    del Scene.vrcft_split

    max_length = max(
        len(VRCFT_Labels_Partial_Unsplit),
        len(VRCFT_Labels_Partial_Split),
        len(VRCFT_Labels_Full_Unsplit),
        len(VRCFT_Labels_Full_Split)
    )

    for i in range(max_length):
        delattr(Scene, f"vrcft_shapekeys_{i}")
        delattr(Scene, f"vrcft_vertex_groups_{i}")

if __name__ == "__main__":
    register()
