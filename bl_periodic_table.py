import bpy
import json
import os
from math import *
# <pep8 compliant>
# <pep8-80 compliant>
# print(bpy.utils.user_resource("SCRIPTS", "addons"))

json_file = '/home/ramona/PycharmProjects/blender_periodic_table/bl_periodic_table/Periodic_Table_JSON/MyPeriodic_Table.json'
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
    "doc_url": "",
    "tracker_url": "ramonajenny.com",
    "category": "Add Periodic Table",
}


class VIEW3D_PT_periodic_table(bpy.types.Panel):
    """Creates a Panel in the Object Properties window"""
    bl_idname = "VIEW3D_PT_periodic_table"
    bl_label = "Elements"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Periodic Table'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        layout.operator_menu_enum("object.select_by_type", "type", text="Select an Element...")
        row = layout.row()
        row.label(text="Number:")
        row.operator("Object.add_and_define_atom", text="json_file['number']")
        row = layout.row()
        row.label(text="Name")
        row.operator("Object.add_and_define_atom", text="json_file['name']")
        row = layout.row()
        row.label(text="Color:")
        row.operator("Object.add_and_define_atom", text="json_file['color']")
        row = layout.row()
        row.label(text="Atomic Mass:")
        row.operator("Object.add_and_define_atom", text="json_file['Atomic Mass']")

        layout.operator("Object.add_and_define_atom", text="Add Atom")
       # layout.separator()
       # layout.operator_enum("object.light_add", "type")


class add_and_define_atom(bpy.types.Operator):
    bl_idname = "object.add_and_define_atom"
    bl_label = "Characteristics"

    def execute(self, context):
        layout = self.layout
        #row = layout.row()
        #row.operator("object.text_add")
        bpy.ops.mesh.primitive_uv_sphere_add(radius=2.0, align='WORLD')
        print("adding")




class JSON_PT_filepath(bpy.types.Panel):
    bl_label = "JSON_PT_filepath"
    bl_category = "JSON data"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        JSON_tools = context.scene.JSON_file
        row.prop(JSON_tools, "json_file")


blender_classes = [
    VIEW3D_PT_periodic_table,
    add_and_define_atom,
    JSON_PT_filepath,
]


def register():
    for i in blender_classes:
        bpy.utils.register_class(i)
    print("Hello my World")


def unregister():
    for i in blender_classes:
        bpy.utils.unregister_class(i)
        print("am i unregistered")
    print("Goodbye my World")


if __name__ == "__main__":
    register()