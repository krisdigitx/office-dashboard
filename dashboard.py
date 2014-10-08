__author__ = 'krishnaa'

import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import *
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from random import random
from kivy.properties import ListProperty

kv = '''
<ColoredLabel>:
    size: (100,100)

    background_color:
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size
    '''

Builder.load_string(kv)

class ColoredLabel(Label):
    background_color = ListProperty((0,0,0,1))

class MyApp(App):

    def build(self):
        f = FloatLayout()
        g = GridLayout(cols=5, rows=2, row_force_default=True, row_default_height=80)
        layout = BoxLayout(size_hint=(1, None), height=50, spacing=100, pos_hint={'top': 1})
        v = Video(source='driver.mp4', state='play', options={'eos':'loop'})
        l1 = Label(text="jenkins", font_size=32)
        l2 = Label(text="git", font_size=32)
        f.add_widget(v)

        """
        label1 = ColoredLabel(text="jenkins output", pos_hint={'top': 1, 'right': .1}, size_hint=(None, None) , background_color=(160,160,160,.5))
        f.add_widget(label1)

        label2 = ColoredLabel(text="git output", pos_hint={'top': 1, 'right': .5}, size_hint=(None, None) , background_color=(160,160,160,.5))
        f.add_widget(label2)

        label3 = ColoredLabel(text="dev output", pos_hint={'top': 1, 'right': .8}, size_hint=(None, None) , background_color=(160,160,160,.5))
        f.add_widget(label3)
        """

        text1 = "jenkins"


        text1 = "red"
        if text1 == "red":
            label1 = ColoredLabel(text=text1, background_color=(204,0,0,.5))
            layout.add_widget(label1)
        else:
            label1 = ColoredLabel(text=text1, background_color=(160,160,160,.5))
            layout.add_widget(label1)


        label2 = ColoredLabel(text="git", background_color=(160,160,160,.5))
        layout.add_widget(label2)

        label3 = ColoredLabel(text="portal", background_color=(160,160,160,.5))
        layout.add_widget(label3)

        label4 = ColoredLabel(text="network", background_color=(160,160,160,.5))
        layout.add_widget(label4)

        label5 = ColoredLabel(text="skyscape", background_color=(160,160,160,.5))
        layout.add_widget(label5)


        f.add_widget(layout)

        #w.add_widget(f)

        return f

if __name__ == "__main__":
    MyApp().run()