from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enabled = False
# window.exit_button.visible = False

Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('assets/skytest2.jpg'),
    scale=500,
    double_sided=True
)

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/block/Grass_Block/Grass_Block_TEX.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block/Grass_Block/Grass_Block.obj',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal)
            elif key == 'right mouse down':
                destroy(self)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()

app.run()