import bpy
from mathutils import *
from ... base_types.node import AnimationNode
from ... mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling


class mn_ScaleMatrix(bpy.types.Node, AnimationNode):
    bl_idname = "mn_ScaleMatrix"
    bl_label = "Scale Matrix"
    isDetermined = True
    
    def init(self, context):
        forbidCompiling()
        self.inputs.new("mn_VectorSocket", "Scale").value = [1, 1, 1]
        self.outputs.new("mn_MatrixSocket", "Matrix")
        allowCompiling()
        
    def getInputSocketNames(self):
        return {"Scale" : "scale"}
    def getOutputSocketNames(self):
        return {"Matrix" : "matrix"}

    def useInLineExecution(self):
        return True
    def getInLineExecutionString(self, outputUse):
        return "$matrix$ = mathutils.Matrix.Scale(%scale%[0], 4, [1, 0, 0]) * mathutils.Matrix.Scale(%scale%[1], 4, [0, 1, 0]) * mathutils.Matrix.Scale(%scale%[2], 4, [0, 0, 1])"
        
    def getModuleList(self):
        return ["mathutils"]
        
    def copy(self, node):
        self.inputs[0].value = [1, 1, 1]
