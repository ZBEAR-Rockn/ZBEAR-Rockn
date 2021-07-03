"""

Hello, I'm ZBEAR. The Hard Rock Guitarist and 3D Music Video maker using Blender.

First, before I say something, I am sorry about my hard rock promotion, which is decided 
as much as to make and distribute functions for people free of charge.
I am very sorry that my urgent problem, the global hard rock inflation problem, 
has led to the inclusion of advertisements for my artist's name 'ZBEAR' and its activity, 
hard rock guitar solo albums, and if the world could have prevented me from becoming such a 
hungry guitarist by blind capitalism(I support capitalism system with not-blinded options), 
all of these advertisements in everyside of this add-on could have been removed. I want you to understand.

This Code has simple routine but I thought the idea for making this feature would be worthwhile in that no one tried to implement this convenient function.
So, despite having to burn out the guitar strings as a guitarist, I decided to make this add-on while making music videos using Great Tool called Blender.

In many cases, someone may not be aware of why this add-on's core vision is currently needed for them.
However, if it is used properly at the proper situation, this idea can save your non-productive time by selectively initializing the values ​​of the complexly twisted weighting table and re-painting the weights for the mesh part that comes back into view.
Check out the description on the product page and packed readme files for more details.

'And if possible, if someday the blender team decide to include this partial weighting management idea of ​​this addon, I would be very grateful if that function is added with marking my active name 'ZBEAR'.'

"""

bl_info = {
    "name": "ZBEAR's Weight Resetter",
    "description": "Reset weights N' attach a bone ",
    "author": "ZBEAR, Hard Rock Guitarist",
    "version": (1, 80),
    "blender": (2, 93, 0),
    "location": "View 3D Panel Line",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Vertex Weighting",
    }

import os
import bpy
from bpy.props import FloatProperty, StringProperty
from bpy.types import Operator, Panel, PropertyGroup

class Reset_PT_Alive_Weights_Panel(bpy.types.Panel):
    
    bl_idname = "REWEIGHT_PT_panel"
    bl_space_type = "VIEW_3D"
    #bl_context = "objectmode"
    bl_region_type = "UI"
    bl_label = "ZBEAR's Weight Resetter"
    bl_category = "ZB_RWT"
    

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        row = layout.row()
        row.label(text="::: Check out Active Object :::")
        row = layout.row()
        row.label(text="0.Check out whether your weirdly")
        row.label(text="weighted mesh object is selected")
        row.label(text="as an Active Object >>> ")
        row = layout.row()
        row.label(text="" + context.object.name)
        row = layout.row()
        
        #Choose the bone that should be most influential. You can only choose one bone.
    
        layout.label(text="1.Make a New Vertex Group that")
        layout.label(text="has weirdly weighted verts")
        layout.label(text="2.Insert the Name of This Group")
        layout.label(text=">>>")
        row = layout.row()
        row.prop(context.scene,"G_Name_for_Reset_prop")
        layout.label(text="3.Decide a bone : Most relevant") 
        layout.label(text="to your New Vertex Group")  
        layout.label(text="4.Insert the Name of This Bone")    
        layout.label(text="(Bone must have its Verts-Group)")  
        layout.label(text=">>>")     
        row = layout.row()
        row.prop(context.scene, "G_Name_for_Alive_prop")
        layout.label(text="5.New Weight to The Bone:")
        layout.label(text=">>>")
        row = layout.row()
        row.prop(context.scene, "weight_for_alive_prop")         
              
        #You can access the string by context.scene.'strname'    
        row = layout.row()
     
        layout.label(text="6.Let's Rock that V-Group >>>")
        row = layout.row()
        row.scale_y = 3.0
                
        #Do it!
        row.operator("reweight.reweightprocess")
        row = layout.row()
        row.label(text="7.Listen to ZBEAR's Hard", icon='WORLD_DATA')
        row = layout.row()
        row.label(text="Rock Guitar Solo Albums")
        row = layout.row()
        row.label(text="on the internet")


class REWEIGHT_OT_process(Operator):
    bl_idname = "reweight.reweightprocess"
    bl_label = "ZBEAR's Weight Resetter"
    bl_description = "Reset N' Assign New Weights"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context) -> bool:
        return bool(context.selected_objects)
    
    def execute(self, context):
        context.window_manager.progress_begin(0, 10)
        obj = context.active_object
        active_obj= context.active_object

        bpy.ops.object.mode_set(mode='OBJECT',toggle=True)
        
        mesh = obj.data

        g_i_for_reset_groups = active_obj.vertex_groups[context.scene.G_Name_for_Reset_prop].index
        g_i_for_alive_groups = active_obj.vertex_groups[context.scene.G_Name_for_Alive_prop].index
        
        
        print("index_resetgroup:", g_i_for_reset_groups, "index_alive_group:", g_i_for_alive_groups)
       
        vlist = []
       
       #have to make to work with only verts in reset-group
        for v in mesh.vertices:        
            for g in v.groups:
                if(g.group == g_i_for_reset_groups):
                    g.weight = 0.0
                    vlist.append(v.index)
                
        #If there are some verts that exists in this reset-group but not in the alive-group,
        # add this blinded verts to the alive-group
        alive_vg = bpy.context.active_object.vertex_groups[context.scene.G_Name_for_Alive_prop]        
             
        aliveG_CT = 0                        

        for vl in vlist :
            aliveG_CT = 0
            for i9 in range(0, len(mesh.vertices[vl].groups)-1) : #
                mesh.vertices[vl].groups[i9].weight = 0.0
                if mesh.vertices[vl].groups[i9].group == g_i_for_alive_groups :
                     aliveG_CT += 1
                     mesh.vertices[vl].groups[i9].weight = context.scene.weight_for_alive_prop
                
            if aliveG_CT == 0:
                #append this vertex to alive group's vextex list
                have_to_alive = []
                have_to_alive.append(vl)
                alive_vg.add(have_to_alive, context.scene.weight_for_alive_prop, 'ADD')
        
#---------------------------------------------------------------weights were reset and re allocated
#      context.window_manager.progress_begin(0, 10)

        context.window_manager.progress_end()
        return {'FINISHED'}



        # end progress bar
        

classes = (
    Reset_PT_Alive_Weights_Panel,
    REWEIGHT_OT_process,
    )

register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    
 #   for cls in classes:
#        bpy.utils.register_class(cls)
            
    bpy.utils.register_class(Reset_PT_Alive_Weights_Panel)
    
    bpy.utils.register_class(REWEIGHT_OT_process)
    
    bpy.types.Scene.G_Name_for_Reset_prop = bpy.props.StringProperty(
    name = "",
    description = "G_Name_for_Reset",
    default = "default",
    options = {'TEXTEDIT_UPDATE'}
    )
     
    bpy.types.Scene.G_Name_for_Alive_prop = bpy.props.StringProperty(
    name = "",
    description = "G_Name_for_Alive",
    default = "default",
    options = {'TEXTEDIT_UPDATE'}
    )
    
    bpy.types.Scene.weight_for_alive_prop = bpy.props.FloatProperty(
    name = "",
    description = "weight_for_alive",
    default = 0.7,
    min = 0.0,
    max = 1.0,
    options = {'TEXTEDIT_UPDATE'}
    )

def unregister():
   # for cls in classes:
    #    bpy.utils.unregister_class(cls)    
    
    
    bpy.utils.unregister_class(Reset_PT_Alive_Weights_Panel)
    bpy.utils.unregister_class(REWEIGHT_OT_process)
    del bpy.types.Scene.G_Name_for_Reset_prop
    del bpy.types.Scene.G_Name_for_Alive_prop
    del bpy.types.Scene.weight_for_alive_prop


if __name__ == "__main__":
    register()

# Let's Rock with ZBEAR.