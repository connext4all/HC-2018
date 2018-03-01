#!/usr/bin/env python
# -*- coding: utf-8 -*-

class maps:

	def __init__(self, filename="datasets/a_example.in"):

		file = open(filename, "r")
		lines = file.read().splitlines()
		values = lines[0]
		#print lines;
		self.rows 	  = values[0]
		self.columns  = values[1]
		self.n_veh	  = values[2]
		self.n_rides  = values[3]
		self.bonus	  = values[4]
		self.map_steps= values[5]
		self.rides 	  = rides(lines[1:])
	
class rides:
	def __init__(self,lines):
		self.rides_list = []
		i=0
		for line in lines:
			line = line.split(" ")
			ride_params = {"init_pos":(line[0],line[1]),"finish_pos":(line[2],line[3]),"first_step":line[4],"deadline":line[5]}
			self.rides_list.append(ride_params)

	def print_list(self):
		print self.rides_list

class vehicle:
	def __init__(self,id_v,pos=(0,0)):
		self.id = id_v
		self.trips = []
		self.pos = pos
		self.steps = 9
		self.finish_pos = (0,0)

	def set_pos(self,pos=(0,0)):
		self.pos = pos

	def set_finish_pos(self,f_pos=(0,0)):
		self.finish_pos = f_pos


def calc_distance(init_pos=(0,0), finish_pos=(0,0)):
	a,b = self.init_pos
	x,y = self.finish_pos
	return abs(a-x) + abs(b-y)


if __name__ == "__main__":
	
	#file_w = open("output/salida1","w")
	map = maps()
	
	#for pos in map.rides.rides_list:
		 



