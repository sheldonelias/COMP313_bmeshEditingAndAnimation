'''
Editing Meshes in bmesh
edit-mesh-bmesh.py
'''

import bpy
import bmesh

'''

# Force the app into object mode
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete()



# Create a cube 
bpy.ops.mesh.primitive_cube_add(location = (-3, 0, 0))
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action = 'DESELECT')



# Select and rotate a face around the z-axis
bpy.ops.mesh.select_mode(type = 'FACE')
bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.faces.ensure_lookup_table()
bm.faces[5].select = True
bpy.ops.transform.rotate(value = .3, orient_axis='Z')
bpy.ops.object.mode_set(mode='OBJECT')



# Create a cube and edit an edge
bpy.ops.mesh.primitive_cube_add(location = (3, 0, 0))
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action = 'DESELECT')

bpy.ops.mesh.select_mode(type = 'EDGE')
bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.edges.ensure_lookup_table()

bm = bmesh.from_edit_mesh(bpy.context.object.data)

bm.edges[11].select = True

bpy.ops.transform.translate( value = (0, 0.5, 0) )

bpy.ops.object.mode_set(mode='OBJECT')

'''

# VERTEX EDITING

# Create a cube and edit a vertex position
bpy.ops.mesh.primitive_cube_add(location = (0, -3, 0))

cube_vert_edited = bpy.context.object

cube_vert_edited.name = 'cube_vert_edited'


# Put app into Edit mode
bpy.ops.object.mode_set(mode = 'EDIT')

# Deslect any previously selected mesh part
bpy.ops.mesh.select_all(action = 'DESELECT')

# Put app into selecting vertex mode
bpy.ops.mesh.select_mode(type = 'VERT')

# Send a copy of the data and mesh of the current object that is being edited
bm = bmesh.from_edit_mesh(bpy.context.object.data)

# Confirm that the bm data-mesh object is whole and not broken
bm.verts.ensure_lookup_table()

# Select the 8th vertex (remember, we count starting from 0)
bm.verts[7].select = True

# Move the chosen vertex
bpy.ops.transform.translate( value = (0, 0.5, 0) )

# Restore back to object mode
bpy.ops.object.mode_set(mode='OBJECT')



# --- ANIMATION

# --- VERTICES are animated one at a time unless grouped together (group is for another day)

# Deslecting all objects
bpy.ops.object.select_all(action='DESELECT')

# Selecting by name a specific object in the Outliner
bpy.data.objects[cube_vert_edited.name].select_set(True)

# Setting the mode to Edit
bpy.ops.object.mode_set(mode='EDIT')

# Choose the vertices type for mesh editing
bpy.ops.mesh.select_mode(type='VERT')

# deselect all verts
bpy.ops.mesh.select_all(action='DESELECT')

# Copy mesh of cube_vert_edited into variable vert_mesh in editable form
vert_mesh = bmesh.from_edit_mesh(cube_vert_edited.data)

# Confirm that the bm data-mesh object is whole and not broken
vert_mesh.verts.ensure_lookup_table()

# Selects the desired vertex to animate
vert_mesh.verts[5].select = True

# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 0)

# Transfer the whole coordinate value tuple into x, y, z variables
x, y, z = cube_vert_edited.data.vertices[5].co

# Perform arithmetic on the values
cube_vert_edited.data.vertices[5].co = (x + 3, y, z)

# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 50)

# Directly change just one coordinate value
cube_vert_edited.data.vertices[5].co.z = 3

# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 100)

# REMINDER: Animation is not visible in Edit mode of an object. Change to Object mode to see movement

# Looping using time or frame count across a range of 240 frames.

for frame_basis in range(16):
    
    # Exposes the coord values of vertex at index 5 of the cube_vert_edited.vertices[] list
    x, y, z = cube_vert_edited.data.vertices[5].co
    
    # For every even numbered frame_basis
    if frame_basis % 2 == 0:
        # Perform arithmetic on the values
        cube_vert_edited.data.vertices[5].co = (x + 1, y + 1, z + 1)
        
    else:     
        # Perform arithmetic on the values
        cube_vert_edited.data.vertices[5].co = (x - 1, y - 1, z - 1)
    
    
    # Insert a key frame of the state of vertex coord values ever 10 frames after the 100th frame
    cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 100 + (frame_basis * 10))
    
    pass


# --- EDGES are animated with two vertices


# Choose the vertices type for mesh editing
bpy.ops.mesh.select_mode(type='VERT')

# deselect all verts
bpy.ops.mesh.select_all(action='DESELECT')

# Copy mesh of cube_vert_edited into variable vert_mesh in editable form
vert_mesh = bmesh.from_edit_mesh(cube_vert_edited.data)

# Confirm that the bm data-mesh object is whole and not broken
vert_mesh.verts.ensure_lookup_table()

# Store two vertices that together make an edges

# Selects the desired vertex to animate
vert_mesh.verts[5].select = True

# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 0)

# Transfer the whole coordinate value tuple into x, y, z variables
x1, y1, z1 = cube_vert_edited.data.vertices[5].co


# Selects the desired vertex to animate
vert_mesh.verts[7].select = True

# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[7].keyframe_insert('co', frame = 0)

# Transfer the whole coordinate value tuple into x, y, z variables
x2, y2, z2 = cube_vert_edited.data.vertices[7].co


# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 260)

# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[7].keyframe_insert('co', frame = 260)


cube_vert_edited.data.vertices[5].co = (x1 + 3, y1, z1) 
 
 
cube_vert_edited.data.vertices[7].co = (x2 + 3, y2, z2) 


# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 270)

# Insets keyframe at 0. That data path 'co' stands for coordinate
cube_vert_edited.data.vertices[7].keyframe_insert('co', frame = 270)


# Loop animates an edge using 2 vertices
for frame_basis in range(16):
    
    # Exposes the coord values of vertex at index 5 of the cube_vert_edited.vertices[] list
    x1, y1, z1 = cube_vert_edited.data.vertices[5].co
    
    x2, y2, z2 = cube_vert_edited.data.vertices[7].co
    
    # For every even numbered frame_basis
    if frame_basis % 2 == 0:
        # Perform arithmetic on the values
        cube_vert_edited.data.vertices[5].co = (x1 - 3, y1, z1 - 1)
        cube_vert_edited.data.vertices[7].co = (x2 - 3, y2, z2 - 1)
        
    else:     
        # Perform arithmetic on the values
        cube_vert_edited.data.vertices[5].co = (x1 + 3, y1, z1 + 1)
        cube_vert_edited.data.vertices[7].co = (x2 + 3, y2, z2 + 1)
    
    
    # Insert a key frame of the state of vertex coord values ever 10 frames after the 100th frame
    cube_vert_edited.data.vertices[5].keyframe_insert('co', frame = 280 + (frame_basis * 10))
    cube_vert_edited.data.vertices[7].keyframe_insert('co', frame = 280 + (frame_basis * 10))
    
    pass




'''
# Restore back to object mode
bpy.ops.object.mode_set(mode='OBJECT')

# Deslect all
bpy.ops.object.select_all(action = 'DESELECT')
'''