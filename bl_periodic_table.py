import bpy
import bmesh
import math
import mathutils

import json
import random
import os
from math import *
# <pep8 compliant>
# <pep8-80 compliant>
# print(bpy.utils.user_resource("SCRIPTS", "addons"))

json_file = '/home/ramona/PycharmProjects/blender_periodic_table/bl_periodic_table/Periodic_Table_JSON/my_periodic_table.json'
with open(json_file, "r") as read_file:
    json_file = json.load(read_file)

bl_info = {
    "name": "Periodic Table",
    "author": "Ramona Niederhausern <ramonajenny.com> <ramonajenny.n@gmail.com>",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "VIEW_3D",
    "description": "adds elements/atoms",
    "warning": "",
    "doc_url": "https://github.com/ramonajenny/blender_periodic_table",
    "tracker_url": "ramonajenny.com",
    "category": "Add Periodic Table"
}


class the_panel(bpy.types.Panel):
    """Creates a Panel in the Object Properties window"""
    bl_idname = "VIEW3D_PT_periodic_table"
    bl_label = "Periodic Table"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Periodic Table'

    def draw(self, context):
        self.layout.row()
        self.layout.row().operator_menu_enum("object.select_by_type", "type='items'", text="Select an Element...")
        self.layout.row()
        self.layout.row().label(text="Atomic Number:")
        self.layout.row()
        self.layout.row().label(text="Element Name:")
        self.layout.row().operator("object.text_add", text="Add Element Name", icon='FONT_DATA')
        self.layout.row()
        self.layout.row().label(text="Symbol")
        self.layout.row()
        self.layout.row().label(text="Color:")
        self.layout.row()
        self.layout.row().label(text="Phase:")
        self.layout.row()
        self.layout.row().label(text="Atomic Mass:")
        self.layout.row()
        self.layout.row().label(text="Category:")
        self.layout.row()
        self.layout.row().label(text="Density:") #g/l if gas, solid g/cm^3
        self.layout.row()
        self.layout.row().label(text="Shells:")
        self.layout.row()
        self.layout.row().label(text="Electron Configuration:")
        self.layout.row()
        self.layout.row().label(text="Atomic Radius:") #empirical
        self.layout.row()
        self.layout.row().label(text="van der Waals Radius:")
        self.layout.row()
        self.layout.row().label(text="Covalent Radius Single Bond:")
        self.layout.row()
        self.layout.row().label(text="Electronegativity Pauling:")
        self.layout.row()
        self.layout.row().label(text="Ionization Energies:")
        self.layout.row()
        self.layout.row().operator("mesh.primitive_uv_sphere_add", text="Add Atom", icon='SPHERE')
        self.layout.row()

        self.layout.row()


class MENU_PT_Part(bpy.types.Panel):
    bl_label = "Name of the Panel"
    bl_idname = "MENU_PT_Part"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Template Tab"

    def draw(self, context):
        self.layout.operator("wm.template_operator")


class MENU_PT(bpy.types.Operator):
    bl_label = "Template Operator"
    bl_idname = "wm.template_operator"

    preset_enum: bpy.props.EnumProperty(
        #number="32",
        name="",
        description="Select an option",
        items=[
            ('Option1', 'Helium', "Add an element to your scene"),
            ('OP2', 'this one', "AddAdd an element to your scene"),
            ('Option3', 'Hydrogen', "Add an element to your scene"),
            ('Option4', 'Lithium', "Add an element to your scene"),
            ('Option5', 'Helium', "Add an element to your scene")
        ]
    )

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        self.layout.prop(self, "preset_enum")

    def execute(self, context):

        if self.preset_enum == 'Option1':
            bpy.ops.mesh.primitive_uv_sphere_add()

        if self.preset_enum == 'OP2':
            bpy.ops.mesh.primitive_cube_add()

        print("hello execute")
        return {'FINISHED'}


class choose_atom(bpy.types.Operator):
    bl_idname = "wm.choose_atom"
    bl_label = "Characteristics"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_parent_id = 'VIEW3D_PT_periodic_table'
    #bl_options = {'DEFAULT_CLOSED'}

    def execute(self, context):
        self.layout.row().operator("object.text_add")
        bpy.ops.mesh.primitive_uv_sphere_add(radius=2.0, align='WORLD')



class MyProperties(bpy.types.PropertyGroup):
    my_string: bpy.props.StringProperty(name="Enter Text")

    my_float_vector: bpy.props.FloatVectorProperty(name="Scale", soft_min=0, soft_max=1000, default=(1, 1, 1))

    my_enum: bpy.props.EnumProperty(
        name="Enumerator / Dropdown",
        description="sample text",
        items=[('OP1', "Add Cube", ""),
               ('OP2', "Add Sphere", ""),
               ('OP3', "Add Suzanne", "")
               ]
    )


class ADDONNAME_PT_main_panel(bpy.types.Panel):
    bl_label = "Main Panel"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "New Tab"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "my_string")
        layout.prop(mytool, "my_float_vector")
        layout.prop(mytool, "my_enum")

        layout.operator("addonname.myop_operator")


class ADDONNAME_OT_my_op(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operator"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        if mytool.my_enum == 'OP1':
            bpy.ops.mesh.primitive_cube_add()
            bpy.context.object.name = mytool.my_string
            bpy.context.object.scale[0] = mytool.my_float_vector[0]
            bpy.context.object.scale[1] = mytool.my_float_vector[1]
            bpy.context.object.scale[2] = mytool.my_float_vector[2]

        if mytool.my_enum == 'OP2':
            bpy.ops.mesh.primitive_uv_sphere_add()
            bpy.context.object.name = mytool.my_string
            bpy.context.object.scale[0] = mytool.my_float_vector[0]
            bpy.context.object.scale[1] = mytool.my_float_vector[1]
            bpy.context.object.scale[2] = mytool.my_float_vector[2]

        if mytool.my_enum == 'OP3':
            bpy.ops.mesh.primitive_monkey_add()
            bpy.context.object.name = mytool.my_string
            bpy.context.object.scale[0] = mytool.my_float_vector[0]
            bpy.context.object.scale[1] = mytool.my_float_vector[1]
            bpy.context.object.scale[2] = mytool.my_float_vector[2]

        return {'FINISHED'}


blender_classes = [
    the_panel,
    choose_atom,
    MENU_PT_Part,
    MENU_PT,
    MyProperties,
    ADDONNAME_PT_main_panel,
    ADDONNAME_OT_my_op
]


def register():
    for i in blender_classes:
        bpy.utils.register_class(i)
    print("Hello my World")
    #print(json_file)


def unregister():
    for i in blender_classes:
        bpy.utils.unregister_class(i)
        print("am i unregistered")
    print("Goodbye my World")


if __name__ == "__main__":
    register()