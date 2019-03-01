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
    "description": "Exporter for .ffa & .ffm files"
}

import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
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
    bl_label = "OP"

    def execute(self, context):
        return {'FINISHED'}

    @classmethod
    def register(cls):
        print("Registered Class: %s " % cls.bl_label)

        bpy.types.Scene.file_type = EnumProperty(
            name="File type",
            items=(('.ffm', "FFM", ""),
                   ('.ffa', "FFA", "")),
            description="Choose your file type")

        bpy.types.Scene.version = EnumProperty(
            name="Version",
            items=(('v2', "version 2", "blah"),
                    ('v3', "version 3", "blah")),
            description="Choose your version")

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
    def unregister(cls):
        print("Unregistering Class: %s " % cls.bl_label)
        del bpy.types.Scene.export_types
        del bpy.types.Scene.file_type
        del bpy.types.Scene.float_color_format
        del bpy.types.Scene.version


class ExporterPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "TEST"
    bl_label = "Select Export Options:"


    def draw(self, context):

        layout = self.layout

        row = layout.row(align=True)
        row.label(text="Select a File Type:")
        row.separator()
        row.prop_enum(context.scene, 'file_type', '.ffm')
        row.prop_enum(context.scene, 'file_type', '.ffa')

        row.separator()

        row = layout.row(align=True)
        row.label(text="Select a Version:")
        row.separator()
        row.prop_enum(context.scene, 'version', 'v2')
        row.prop_enum(context.scene, 'version', 'v3')

        row.separator()

        col = layout.column(align=True)
        col.label(text="What would you like to export?")
        row = col.row(align=True)
        row.prop(context.scene, 'export_types')

        col.separator()

        row = layout.row()
        row.prop(context.scene, 'float_color_format')

        row.separator()

        row = layout.row()
        row.operator("object.export_file", text="Export Selected")


classes = (
    ExportFile,
    ExporterSettingsOperators,
    ExporterPanel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    print("Exporter Load Finished in: %.4f sec" % (time.time() - time_start))


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    try:
        unregister()
    except Exception as e:
        print(e)
        pass

    register()

