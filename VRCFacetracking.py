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
# VRChat Facetracking Partial Shapekey List   
# -------------------------------------------------------------------

VRCFT_Labels_Partial = [
    "EyeClosedRight",
    "EyeClosedLeft",
    "EyeSquintRight",
    "EyeSquintLeft",
    "EyeWideRight",
    "EyeWideLeft",
    "EyeDilation",
    "EyeConstrict",
    "CheekPuffRight",
    "CheekPuffLeft",
    "CheekSuck",
    "JawOpen",
    "JawRight",
    "JawLeft",
    "JawForward",
    "JawBackward",
    "MouthUpperUp",
    "MouthLowerDown",
    "MouthStretch",
    "BrowDownRight",
    "BrowDownLeft",
    "BrowUpRight",
    "BrowUpLeft",
    "MouthRight",
    "MouthLeft",
    "MouthSmile",
    "MouthSad",
    "TongueOut",
    "TongueUp",
    "TongueDown",
    "TongueRight",
    "TongueLeft",
    "TongueRoll"
]

# -------------------------------------------------------------------
# VRChat Facetracking Full Shapekey List   
# -------------------------------------------------------------------

VRCFT_Labels_Full = [
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
    "JawMandibleRaise",
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
    "MouthRaiserUpper",
    "MouthRaiserLower",
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
# Bunch o' stuff
# -------------------------------------------------------------------

def get_meshes(self, context):
    return [(obj.name, obj.name, obj.name) for obj in bpy.context.view_layer.objects 
            if obj.type == 'MESH']

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
        return VRCFT_Labels_Full
    return VRCFT_Labels_Partial

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
            
        OG = {}
        existing_keys = [key.name for key in mesh.data.shape_keys.key_blocks]
        
        for i, label in enumerate(active_list):
            source_key = getattr(context.scene, f"vrcft_shapekeys_{i}")
            vertex_group = getattr(context.scene, f"vrcft_vertex_groups_{i}")
            
            if source_key != "Basis":
                OG[source_key] = mesh.data.shape_keys.key_blocks[source_key].value
            
            if label in existing_keys and source_key == "Basis":
                continue
                
            if label not in existing_keys:
                mesh.shape_key_add(name=label, from_mix=source_key != "Basis")
            
            if source_key != "Basis":
                mesh.data.shape_keys.key_blocks[source_key].value = 1
                mesh.active_shape_key_index = mesh.data.shape_keys.key_blocks.find(label)
                
                if vertex_group != 'NONE':
                    mesh.data.shape_keys.key_blocks[label].vertex_group = vertex_group
                
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.blend_from_shape(shape=source_key, blend=1.0)
                bpy.ops.object.mode_set(mode='OBJECT')
        
        for key, value in OG.items():
            mesh.data.shape_keys.key_blocks[key].value = value
                
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
        for key in mesh.data.shape_keys.key_blocks[:]:
            if (key.name in VRCFT_Labels_Partial or 
                key.name in VRCFT_Labels_Full or 
                key.name == separator_name):
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
        protected_keys = ['Basis'] + VRCFT_Labels_Partial + VRCFT_Labels_Full + [separator_name]
        
        for key in mesh.data.shape_keys.key_blocks[:]:
            if key.name not in protected_keys:
                mesh.shape_key_remove(key)
                
        self.report({'INFO'}, "Non-VRCFT shapekeys have been removed")
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
        
        if mesh and mesh.data.shape_keys:
            layout.label(text='Select shape keys and vertex groups to create VRCFT shape keys.', icon='INFO')
            box = layout.box()
            active_list = get_the_among_us(context)
            for i, label in enumerate(active_list):
                row = box.row(align=True)
                row.label(text=f"{label}:")
                col = row.column()
                col.prop(context.scene, f'vrcft_shapekeys_{i}', icon='SHAPEKEY_DATA')
                col = row.column()
                col.prop(context.scene, f'vrcft_vertex_groups_{i}', icon='GROUP_VERTEX')
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
    bpy.utils.register_class(VRCFT_UL)
    
    Scene.vrcft_username = StringProperty(
        name="Username",
        default="VRChat Face Tracking"
    )
    Scene.vrcft_mesh = EnumProperty(name='Mesh', items=get_meshes)
    Scene.vrcft_mode = EnumProperty(
        name="Mode",
        items=[
            ('PARTIAL', "Partial Unified", "Use partial unified shape key list"),
            ('FULL', "Full Unified", "Use full unified shape key list")
        ],
        default='PARTIAL'
    )
    for i in range(max(len(VRCFT_Labels_Partial), len(VRCFT_Labels_Full))):
        setattr(Scene, f"vrcft_shapekeys_{i}", EnumProperty(name='', items=get_shapekeys))
        setattr(Scene, f"vrcft_vertex_groups_{i}", EnumProperty(name='', items=get_the_sus))

def unregister():
    bpy.utils.unregister_class(VRCFTCreateShapeKeys)
    bpy.utils.unregister_class(VRCFTRemoveShapeKeys)
    bpy.utils.unregister_class(VRCFTClearNonVRCFT)
    bpy.utils.unregister_class(VRCFT_UL)
    
    del Scene.vrcft_username
    del Scene.vrcft_mesh
    del Scene.vrcft_mode
    for i in range(max(len(VRCFT_Labels_Partial), len(VRCFT_Labels_Full))):
        delattr(Scene, f"vrcft_shapekeys_{i}")
        delattr(Scene, f"vrcft_vertex_groups_{i}")

if __name__ == "__main__":
    register()
