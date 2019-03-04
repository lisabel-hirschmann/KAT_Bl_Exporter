# ____ KAT BLENDER EXPORTER ____ #
##################################
# Exporter UI for Blender to:    #
#   - .ffm                       #
#   - .ffa                       #
# <pep8 compliant>               #
# ______________________________ #
##################################

bl_info = {
    "name": "KAT FF Export",
    "author": "Lisa Bel Hirschmann",
    "version": (1, 0, 0),
    "blender": (2, 79, 0),
    "description": "Exporter for .ffa & .ffm files"
}

import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import BoolProperty, EnumProperty
from bpy.types import Operator

# ___ Execution timer (can be deleted after completion) ___ #
import time
time_start = time.time()
# _________________________________________________________ #


class ExportFile(Operator):
    bl_idname = "object.export_file"
    bl_label = "Export Pipeline"

    def execute(self, context ):
        return {'FINISHED'}

    @classmethod
    def register(cls):
        print("Registered Class %s " % cls.bl_label)

    @classmethod
    def unregister(cls):
        print("Unregistering Class: %s " % cls.bl_label)


class ExporterSettingsOperators(Operator):
    bl_idname = "object.operators"
    bl_label = "Object Operators"

    bpy.types.Scene.export_versions = EnumProperty(
        items=(('default', "Select a Version", "default if nothing is selected"),
               ('v2', "Version 2", "something about version"),
               ('v3', "Version 3", "something about version")),
        name="Export Version Selection",
        description="Choose which version of the exporter to use",  # why is there a comma here?
    )

    bpy.types.Scene.file_type = EnumProperty(
        name="File type",
        options={'ENUM_FLAG'},
        items=(('.ffm', "FFM", ""),
               ('.ffa', "FFA", "")),
        description="Choose your file type")

    bpy.types.Scene.export_types = EnumProperty(
        name="Export Types",
        options={'ENUM_FLAG'},
        items=(('MESH', "Mesh", ""),
               ('UV', "UVs", ""),
               ('JOINTS', "Joints", ""),
               ('ANIMATION', "Animation", "")),
        description="Choose what you want to export (SHIFT + Click for multiple)",
        default={'MESH', 'UV'})

    bpy.types.Scene.float_color_format = BoolProperty(
        name="Float Color Format",
        description="Color Format Export Type",
        default=True)

    @classmethod
    def register(cls):
        print("Registered Class %s " % cls.bl_label)

    @classmethod
    def unregister(cls):
        print("Unregistering Class: %s " % cls.bl_label)


class ExporterPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "KAT-Exporter"
    bl_label = "Select Export Options:"


    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.prop(context.scene, "export_versions")

        row = layout.row(align=True)
        row.label(text="Select a File Type:")
        row.separator()
        row.prop_enum(context.scene, 'file_type', '.ffm')
        row.prop_enum(context.scene, 'file_type', '.ffa')

        row.separator()

        col = layout.column(align=True)
        col.label(text="What would you like to export?")
        row = col.row(align=True)
        row.prop_enum(context.scene, 'export_types', 'MESH')
        row.prop_enum(context.scene, 'export_types', 'UV')

        row = col.row(align=True)
        row.prop_enum(context.scene, 'export_types', 'JOINTS')
        row.prop_enum(context.scene, 'export_types', 'ANIMATION')

        col.separator()

        row = layout.row()
        row.prop(context.scene, 'float_color_format')

        row.separator()

        row = layout.row()
        row.alignment = 'CENTER'
        row.operator("object.export_file", text="Export Selected")

    @classmethod
    def register(cls):
        print("Registered Class %s " % cls.bl_label)

    @classmethod
    def unregister(cls):
        print("Unregistering Class: %s " % cls.bl_label)


classes = (
    ExportFile,
    ExporterSettingsOperators,
    ExporterPanel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    #Execution Time TESTCASE (Delete)
    print("Exporter Load Finished in: %.4f sec" % (time.time() - time_start))
    # _____________________________________ #


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    try:
        unregister()
    except Exception as e:
        print(e)
        pass

    register()

