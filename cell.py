import pyglet
from collections import deque
from pyglet.image import load


class Cell(pyglet.sprite.Sprite):
    '''A cell in the minefield.'''
    open_soundeffect = pyglet.media.load("sounds/open_soundeffect.wav", streaming=False)
    explosion_frames = load('images/0.png'), load('images/1.png'), load('images/2.png'), load('images/3.png'), load('images/4.png'), load('images/5.png')
    expl_ani = pyglet.image.Animation.from_image_sequence(explosion_frames, duration=0.2, loop=False)
    explosion = pyglet.media.load('sounds/explosion.wav', streaming=False)
    unopenned_image = load('images/unopenned.png')
    bomb_image = load('images/bomb.png')
    bomb_blownup_image = load('images/bomb_blownup.png')
    zero_image = load('images/zero.png')
    one_image = load('images/one.png')
    two_image = load('images/two.png')
    three_image = load('images/three.png')
    four_image = load('images/four.png')
    five_image = load('images/five.png')
    six_image = load('images/six.png')
    seven_image = load('images/seven.png')
    eight_image = load('images/eight.png')
    flag_image = load('images/flag.png')
    pressed_image = load('images/pressed.png')
    question_mark_image = load('images/question_mark.png')
    values_dict = {0:zero_image, 
                    1:one_image, 
                    2:two_image, 
                    3:three_image, 
                    4:four_image, 
                    5:five_image, 
                    6:six_image, 
                    7:seven_image, 
                    8:eight_image, 
                    'b':bomb_image,
                    'bb':bomb_blownup_image} 
    rmb_states_dict = {'x':unopenned_image, 
                        'f':flag_image, 
                        '?':question_mark_image}

    def __init__(self, value=0, x=0, y=0, scale=1, batch=None, group=None):
        self.value = value
        self.unchecked = not value
        self.openned = False 
        self.pressed = False
        self.rmb_state = 'x'
        self.rmb_states_deque = deque(['x', 'f', '?'])
        super(Cell, self).__init__(self.unopenned_image, x=x, y=y, batch=batch, group=group)
        self.scale = scale

    def press(self):
        if not self.pressed and not self.openned and self.rmb_state == 'x':
            self.pressed = True
            self.old_image = self.image
            self.image = self.pressed_image

    def depress(self):
        if self.pressed:
            self.pressed = False
            self.image = self.old_image


    def open(self, sound:bool=False):
        if not self.openned and self.rmb_state == 'x':
            self.openned = True
            self.image = self.values_dict[self.value]
            if sound:
                self.open_soundeffect.play()


    def on_rmb(self):
        if not self.openned:
            self.rmb_states_deque.rotate(-1)
            self.rmb_state = self.rmb_states_deque[0]
            self.image = self.rmb_states_dict[self.rmb_state]
            
    def explode(self):
        if self.value == 'b':
            explosion_sprite = pyglet.sprite.Sprite(img=self.expl_ani, x=self.x, y=self.y, batch=self.batch)
            explosion_sprite.scale = self.scale
            self.explosion.play()


if __name__ == "__main__":
    cell = Cell()
    cell.open()