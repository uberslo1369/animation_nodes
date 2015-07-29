import bpy, random
from ... algorithms.perlin_noise import perlinNoise
from ... base_types.node import AnimationNode
from ... mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling


class mn_FloatWiggle(bpy.types.Node, AnimationNode):
    bl_idname = "mn_FloatWiggle"
    bl_label = "Number Wiggle"
    isDetermined = True
    
    additionalSeed = bpy.props.IntProperty(update = nodePropertyChanged)
    
    def init(self, context):
        forbidCompiling()
        self.inputs.new("mn_FloatSocket", "Seed")
        self.inputs.new("mn_FloatSocket", "Evolution")
        self.inputs.new("mn_FloatSocket", "Speed").value = 15.0
        self.inputs.new("mn_FloatSocket", "Amplitude").value = 1
        self.inputs.new("mn_FloatSocket", "Persistance").value = 0.3
        self.inputs.new("mn_IntegerSocket", "Octaves").value = 2.0
        self.outputs.new("mn_FloatSocket", "Noise")
        allowCompiling()
        
    def draw_buttons(self, context, layout):
        layout.prop(self, "additionalSeed", text = "Additional Seed")
        
    def getInputSocketNames(self):
        return {"Seed" : "seed",
                "Evolution" : "x",
                "Speed" : "speed",
                "Amplitude" : "amplitude",
                "Persistance" : "persistance",
                "Octaves" : "octaves"}
    def getOutputSocketNames(self):
        return {"Noise" : "noise"}
        
    def execute(self, seed, x, speed, amplitude, persistance, octaves):
        x = x / speed + 2673 * seed + 823 * self.additionalSeed
        total = perlinNoise(x, persistance, octaves)
        return total * amplitude
        

