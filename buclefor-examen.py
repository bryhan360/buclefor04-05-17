#!/usr/bin/python
# coding: utf8

for fil in xrange(1,6,1):
	print ""
	for col in xrange(1,5,1):
		if fil == 1:
			if col ==2:
				print "A",
				
			else:
				if col ==3:
					print "B",
				else:
					if col==4:
						print "C",
					else:
						print "-",
		else: 
			print "-",
		
		if col==1: 
			if not(fil == 1):
				print fil -1,
		
		if (fil==3 and col==3) or (fil ==4 and col==2):
			print "*",
