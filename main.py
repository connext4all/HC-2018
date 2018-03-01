#!/usr/bin/env python
# -*- coding: utf-8 -*-

class maps:

	def __init__(self, filename="datasets/a_example.in"):

		file = open(filename, "r")
		lines = file.read().splitlines()
		values = lines[0].split(" ")

		self.rows 	  = values[0]
		self.columns  = values[1]
		self.n_veh	  = values[2]
		self.n_rides  = values[3]
		self.bonus	  = values[4]
		self.map_steps= int(values[5])
		self.rides_ 	  = rides(lines[1:])
		self.vehicles_list = []
		for x in range(int(self.n_veh)):
			v = vehicle(id_v=(x+1))
			self.vehicles_list.append(v)


	def assign_ride(self,v):
		dist_min = 99999999
		id_ride_min = None
		pos_del = None
		for pos in self.rides_.rides_list:
			dist = calc_distance(v.pos,pos["init_pos"])
			if dist < dist_min:
				dist_min = dist
				id_ride_min = pos["id_ride"]
				pos_del = pos
		if id_ride_min is not None: v.assigned_rides.append(id_ride_min)
		v.steps = dist_min

		if pos_del is not None: self.rides_.rides_list.remove(pos_del)
		
	
class rides:
	def __init__(self,lines):
		self.rides_list = []
		i=0
		for line in lines:
			line = line.split(" ")
			ride_params = {"id_ride":i,"init_pos":(int(line[0]),int(line[1])),"finish_pos":(int(line[2]),int(line[3])),"first_step":int(line[4]),"deadline":int(line[5])}
			self.rides_list.append(ride_params)
			i = i+1

	def print_list(self):
		print self.rides_list

class vehicle:
	def __init__(self,id_v,pos=(0,0)):
		self.id = id_v
		self.trips = []
		self.pos = pos
		self.steps = 0
		self.finish_pos = (0,0)
		self.assigned_rides = []
	def set_pos(self,pos=(0,0)):
		self.pos = pos

	def set_finish_pos(self,f_pos=(0,0)):
		self.finish_pos = f_pos


def calc_distance(init_pos=(0,0), finish_pos=(0,0)):
	a,b = init_pos
	x,y = finish_pos
	return abs(a-x) + abs(b-y)


if __name__ == "__main__":
	
	#file_w = open("output/salida1","w")
	map_ = maps("datasets/e_high_bonus.in")
	file_w = open("output/output_e.txt","w") 

	for i in xrange(0,map_.map_steps):
		for v in map_.vehicles_list:
			if v.steps == 0:
				map_.assign_ride(v)
			v.steps=v.steps-1
	
	for v in map_.vehicles_list:
		print str(v.id) + str(v.assigned_rides)
		file_w.write(str(v.id))
		for a in v.assigned_rides:
			file_w.write(" " + str(a))
		file_w.write("\n")

		




		 



