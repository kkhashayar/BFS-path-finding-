import turtle, time
from collections import deque 
from walls import * 
from settings import *

#tile_size = 20
#width = 20
#height = 20 

#screen = turtle.Screen()
#screen.setup(700, 700, 800)
#screen.bgcolor("gray")
#screen.tracer(0)
#font = ("arial", "14")

class Grid(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.pencolor("black")
		self.shape("square")
		self.shapesize(tile_size / 20 )
		self.fillcolor("lightgray")
		self.speed(0)
		self.grid_list = []
		self.walls = walls
		self.connections = [(20,0),(-20,0),(0,20),(0,-20)]

	def draw_grid(self):
		screen.tracer(0)
		self.setpos(-280, 280)
		for x in range(height):
			for y in range(width):
					self.stamp()
					self.grid_list.append(self.pos())
					self.forward(tile_size)
			self.back(tile_size * width)
			self.right(90)
			self.forward(tile_size)
			self.left(90)
			self.hideturtle()
	
	def draw_walls(self):
		self.fillcolor("black")
		self.pencolor("brown")
		for wall in self.walls:
			self.goto(wall)
			self.stamp()
			

def find_neighbors(node):
	hold_position = node
	neighbors = []
	for next in grid.connections:
		 if node + next not in grid.walls and node + next in grid.grid_list:
			 neighbor = node + next
			 neighbors.append(neighbor)
	node = hold_position
	#print(neighbors)
	return(neighbors)
	neighbors = []

grid = Grid()
grid.draw_grid()
grid.draw_walls()

node = Grid()
goal = Grid()

	
def bfs(node, end):
	node.fillcolor("yellow")
	start = node.pos()
	frontier = deque()
	path = {}
	visited = []
	frontier.append(start)
	path[start] = None
	visited.append(start)
	while len(frontier) > 0:
		node.setpos(frontier.popleft())
		current = node.pos()
		for next in find_neighbors(current):
			if next not in visited:
				visited.append(next)
				frontier.append(next)
				screen.tracer(0)
				
				if next[0] > current[0]:
					node.setheading(-180)
					dif = (20,0)
				if next[0] < current[0]:
					node.setheading(0)
					dif = (-20,0)
				if next[1] < current[1]:
					node.setheading(90)
					dif = (0,20)
				if next[1] > current[1]:
					node.setheading(-90)
					dif = (0,-20)
				# path is the problem 
				path[current] = current - next
				node.shape("classic")
				node.shapesize(0.8)
				node.goto(next)
				node.fillcolor("black")
				node.pencolor("black")
				node.stamp()
				screen.update()
				#time.sleep(2)
				#node.shape("circle")
				#node.fillcolor("red")
				#node.shapesize(0.5)
				#last_node =  path[start]
				#node.goto(last_node)
				#node.stamp()
				#screen.update()
				#time.sleep(2)

def click(x,y):
	node.clearstamps()
	x = int(tile_size * round(x/tile_size))
	y = int(tile_size * round(y/tile_size))
	if (x,y) in grid.grid_list and (x,y) not in grid.walls:
		node.setpos(x,y)
		print("start: ", (x,y))
		#start = node.pos()
		end = goal.pos()
		goal.setpos(-140,0)
		goal.fillcolor("red")
		goal.stamp()
		node.shape("square")
		node.shapesize(0.8)
		node.fillcolor("Blue")
		node.pencolor("black")
		node.stamp()
		bfs(node, end)


turtle.listen()
turtle.onscreenclick(click)
turtle.mainloop()
