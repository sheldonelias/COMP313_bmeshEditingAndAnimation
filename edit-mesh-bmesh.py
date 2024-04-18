'''
Editing Meshes in bmesh
edit-mesh-bmesh.py
'''

import bpy
import bmesh

# Force into boject mode
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create a cube and roate a face around the y-axis
bpy.ops.mesh.primitive_cube_add(location = (-3, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='DESELECT')

# Set to face mode for transformations
bpy.ops.mesh.select_mode(type = 'FACE')
bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.faces.ensure_lookup_table()
# Selects a face, usually top one
bm.faces[5].select = True
bpy.ops.transform.rotate(value = 0.3, orient_axis='Z')
bpy.ops.object.mode_set(mode = 'OBJECT')


# Create a cube and pull an edge along the y-axis
bpy.ops.mesh.primitive_cube_add(location = (0, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='DESELECT')
bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.edges.ensure_lookup_table()

# Choose the edge to transform
bpy.ops.mesh.select_mode(type = 'EDGE')
bm.edges[7].select = True
bpy.ops.transform.translate(value = (0, 0.5, 0))
bpy.ops.object.mode_set(mode = 'OBJECT')

# Create a cube and pull a vertex
bpy.ops.mesh.primitive_cube_add(location=(3, 0, 0))
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action='DESELECT')
bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.verts.ensure_lookup_table()
bpy.ops.mesh.select_mode(type = 'VERT')
bm.verts[7].select = True
bpy.ops.transform.translate(value = (0, 1, 1))
bpy.ops.object.mode_set(mode = 'OBJECT')