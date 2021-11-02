import os
import bpy
import bmesh

bpyscene = bpy.context.scene

# output folder
folder = os.path.abspath("//Users//duch//Documents//PhD//ita21_materials//simulation")

# frames
frame_start = bpy.data.scenes["Scene"].frame_start
frame_end = bpy.data.scenes["Scene"].frame_end

for f in range(frame_end - frame_start):
    # output every 10 frames
    if f % 10 == 0:
        print ('Running frame {}'.format(f))
        bpyscene.frame_set(f) # set the scene to the frame
        
        # Get the dependency graph state for this frame
        dg = bpy.context.evaluated_depsgraph_get()
        
        for ob in bpyscene.objects:
#            bpy.ops.object.select_all(action='DESELECT')    
            if ob.name == 'Cube':
                # The mesh from the object and dependency graph
                me = ob.datas
                bm = bmesh.new()
                bm.from_object(ob, dg)
                bm.to_mesh(me)
                bm.free()
                
    #            # Take the coordinates
    #            for v in bm.verts:
    #                print(v.co)
                
                # output the selected object 
                ob.select_set(state=True)            
                bpy.ops.export_scene.obj(
                        filepath=os.path.join(folder, str(f) + ob.name + '.obj'),
                        use_selection=True,
                        )
                ob.select_set(state=False)