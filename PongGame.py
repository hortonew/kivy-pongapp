from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import ObjectProperty
from random import randint
from PongBall import PongBall
from PongPaddle import PongPaddle
import time
import math

class PongGame(Widget):
	ball = ObjectProperty(None)
	player1 = ObjectProperty(None)
	player2 = ObjectProperty(None)
	difficulty = ObjectProperty(None)

	def serve_ball(self, vel=(10, 0)):
		self.ball.center = self.center
		self.ball.velocity = vel

	def update(self, dt):
		# Variables used to detect if collision happened
		collided_p1, collided_p2 = False, False
		collided_top_or_bottom, scored = False, False

		# Get future value of x/y to determine if out of bounds
		future_x = self.ball.x + self.ball.velocity_x
		future_y = self.ball.y + self.ball.velocity_y

		# Ball outside bounds; increment by 1 until collision
		if (future_x <= 25 or (future_x+self.ball.width >= self.width-25) or (future_y <= 0 or (future_y+self.ball.height >= self.height))):
			while (not collided_p1 and not collided_p2 and not collided_top_or_bottom and not scored):

				# Determine the velocity; calculate increment
				if self.ball.velocity_x < 0:
					x_inc = -1
				else:
					x_inc = 1

				if self.ball.velocity_y < 0:
					y_inc = -1
				else:
					y_inc = 1

				# Move ball increment + collision detection
				self.ball.x = self.ball.x + x_inc
				self.ball.y = self.ball.y + y_inc
				collided_p1 = self.player1.bounce_ball(self.ball)
				collided_p2 = self.player2.bounce_ball(self.ball)

				# bounce off top and bottom
				if (self.ball.y < 0) or (self.ball.top > self.height):
					self.ball.velocity_y *= -1
					collided_top_or_bottom = True

				# Point scored; reset
				if self.ball.x < self.x:
					self.player2.score += 1
					self.serve_ball(vel=(10,0))
					scored = True
				if self.ball.x > self.width:
					self.player1.score += 1
					self.serve_ball(vel=(-10,0))
					scored = True
		else:
			# Ball won't be outside bounds; move it
			self.ball.move()
			
		# Basic AI for player 1 - increases in speed every 5 player points
		self.difficulty = math.floor((self.player2.score+5)/5)
		if self.ball.y > self.player1.center_y:
			self.player1.center_y += 3 + self.difficulty
		if self.ball.y < self.player1.center_y:
			self.player1.center_y -= 3 + self.difficulty

	# Handle drag
	def on_touch_move(self, touch):
		self.player2.center_y = touch.y

	# Handle tap
	def on_touch_down(self, touch):
		self.player2.center_y = touch.y