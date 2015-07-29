import bpy
from ... base_types.node import AnimationNode
from ... mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling

class mn_FloatRangeListNode(bpy.types.Node, AnimationNode):
    bl_idname = "mn_FloatRangeListNode"
    bl_label = "Number Range"
    node_category = "Math"
    isDetermined = True
    
    def init(self, context):
        forbidCompiling()
        self.inputs.new("mn_IntegerSocket", "Amount").value = 5
        self.inputs.new("mn_FloatSocket", "Start")
        self.inputs.new("mn_FloatSocket", "Step").value = 1
        self.outputs.new("mn_FloatListSocket", "List")
        allowCompiling()
        
    def getInputSocketNames(self):
        return {"Amount" : "amount", "Start" : "start", "Step" : "step"}
    def getOutputSocketNames(self):
        return {"List" : "list"}
        
    def execute(self, amount, start, step):
        list = []
        for i in range(amount):
            list.append(start + i * step)
        return list
