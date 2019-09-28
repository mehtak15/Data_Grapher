#!/bin/python3
import math
import random

num = 100
inc = 3
arr = [float(i) for i in range(1,num)]
key = ["temp", "press", "time", "alt", "vel", "acc"]
val = {
	"temp" : [math.sin(i) for i in arr],
	"press" : [math.cos(i) for i in arr],
	"time" : [(i+1)/2 for i in arr],
	"alt" : [i*2 for i in arr],
	"vel" : [100-i for i in arr],
	"acc" : [100-i**2 for i in arr]
}
chip = ["BMP", "UNO", "MPU", "GPS"]

with open("test.txt", "w") as file:
	for itr in range(1,len(arr)):
		fail = bool(10 == random.randint(1,10))
		random.shuffle(key)
		file.write("$%s" % (chip[random.randint(0,3)]))
		for k in key:
			if fail and k == key[0]:
				continue
			file.write(",%s,%.2f" % (k, val[k][itr]))
		file.write("\n")