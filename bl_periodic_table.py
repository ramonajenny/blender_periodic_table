import bpy
import json
from math import *
# <pep8 compliant>
# <pep8-80 compliant>

with open("periodic-table-lookup.json", "r") as read_file:
    periodic_table = json.load(read_file)

if "bpy" in locals():
    # reloading .py files
    import importlib
    print("import lib lib")

else:
    print("importing .py files")
    import bpy
    #from . import addon_panel

bl_info = {
    "name": "Periodic Table",
    "author": "Ramona Niederhausern <ramonajenny.com> <ramonajenny.n@gmail.com>",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "Veiw3D",
    "description": "adds elements/atoms",
    "warning": "",
    "doc_url": "",
    "tracker_url": "ramonajenny.com",
    "category": "Add Mesh",
}


class VIEW3D_PT_periodic_table(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Periodic Table'
    bl_idname = "VIEW3D_PT_periodic_table"
    bl_label = "Elements"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", text="")
        row.operator("mesh.primitive_uv_sphere_add", text="Add AtomsAtoms")

        for i in range(7):
            row = layout.row(align=True, heading_ctxt="this one")
            #row.scale_y = 1
            for j in range(5):
                col = row.column(align=True, heading_ctxt="this two")
                col.operator("mesh.primitive_uv_sphere_add", text="Helium")
                cursor = context.cursor
                layout.prop(cursor, "rotation_mode", text="")


class WM_OT_text_operator(bpy.types.Operator):
    bl_idname = "WM_OT_text_operator"
    bl_label = "inset json file"

    text = bpy.props.StringProperty(name="readin JSON file")
    scale = bpy.props.FloatProperty(name="Scale:", default=1)

    def execute(self, context):

        return {'FINISHED'}

    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)


blender_classes = [
    VIEW3D_PT_periodic_table,
    #WM_OT_text_operator
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

