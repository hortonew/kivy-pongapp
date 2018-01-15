from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.vector import Vector
import math


class PongPaddle(Widget):
	score = NumericProperty(0)

	def bounce_ball(self, ball):
		if self.collide_widget(ball):
			speedup = 1.1
			offset = 0.15 * Vector(0, ball.center_y-self.center_y)
			ball.velocity = speedup * (offset - ball.velocity)
