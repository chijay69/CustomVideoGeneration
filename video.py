import bpy

class MyBlenderClass:
    def __init__(self):
        self.scene = bpy.context.scene

    def create_cube(self):
        bpy.ops.mesh.primitive_cube_add()

# Create an instance of the class
blender_obj = MyBlenderClass()

# Call a method of the class
blender_obj.create_cube()
