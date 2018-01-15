from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import ObjectProperty
from random import randint
from PongBall import PongBall
from PongPaddle import PongPaddle
import time

class PongGame(Widget):
	ball = ObjectProperty(None)
	player1 = ObjectProperty(None)
	player2 = ObjectProperty(None)

	def serve_ball(self, vel=(30, 0)):
		self.ball.center = self.center
		self.ball.velocity = vel

	def update(self, dt):
		# call ball.move and other stuff		
		self.ball.move()
		self.player1.bounce_ball(self.ball)
		self.player2.bounce_ball(self.ball)

		# bounce off top and bottom
		if (self.ball.y < 0) or (self.ball.top > self.height):
			self.ball.velocity_y *= -1

		# went off to a side to score point?
		if self.ball.x < self.x:
			self.player2.score += 1
			self.serve_ball(vel=(10,0))
		if self.ball.x > self.width:
			self.player1.score += 1
			self.serve_ball(vel=(-10,0))

		# Basic AI for player 1
		if self.ball.y > self.player1.center_y:
			self.player1.center_y += 3
		if self.ball.y < self.player1.center_y:
			self.player1.center_y -= 3

	def on_touch_move(self, touch):
		self.player2.center_y = touch.y

	def on_touch_down(self, touch):
		self.player2.center_y = touch.y