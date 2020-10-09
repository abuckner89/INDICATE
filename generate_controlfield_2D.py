##################################################################################
#	PROGRAM TO IDENTIFY GENERATE EVENLY-SPACED 2D CONTROL FIELD 	#
##################################################################################

# Author: Anne S.M. Buckner
# Last modified: 24/05/2019

#import packages
import matplotlib.pyplot as plt
import numpy as np

##############################################
# 	Load dataset parameters		#
##############################################

#datasets parameters
dataset_params=open('./dataset_params_2D.csv', 'r')

#empty arrays
dataset_name=[]
edge_x1=[]
edge_x2=[]
edge_y1=[]
edge_y2=[]
area_dataset=[]

#fill arrays
for names in dataset_params:
	names = names.strip()
	columns_names = names.split(',')
	dataset_name.append(str(columns_names[0]))	
	edge_x1.append(float(columns_names[1]))
	edge_x2.append(float(columns_names[2]))
	edge_y1.append(float(columns_names[3]))
	edge_y2.append(float(columns_names[4]))
	area_dataset.append(float(columns_names[5]))

#iterate through datasets in list
for dataset_id in range(0, len(dataset_name)):
	filename=dataset_name[dataset_id]
	left_edge=edge_x1[dataset_id]
	right_edge=edge_x2[dataset_id]
	bottom_edge=edge_y1[dataset_id]
	top_edge=edge_y2[dataset_id]

	print 'Dataset name:', filename


	##############################################
	# 	Read in dataset  #
	##############################################

	#open dataset position file
	file_dataset=open('./dataset_%s'%filename+'.csv', 'r')

	#some empty arrays
	x_dataset=[]
	y_dataset=[]

	#fill arrays
	for line_dataset in file_dataset:
		line_dataset = line_dataset.strip()
		#print line_dataset
		columns_dataset = line_dataset.split(',')
		x_dataset.append(float(columns_dataset[0]))	
		y_dataset.append(float(columns_dataset[1]))

	##############################################
	# 	Generate control field for the dataset  #
	##############################################


	#size of dataset
	num_members=len(x_dataset)


	print 'Size of dataset: ', num_members

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#define control field boundaries and properties


	#Square/Retangular area of dataset region
	area_dat=area_dataset[dataset_id]
	print 'Area: ', area_dataset



	#define square density of control field
	density=area_dat/num_members
	print 'density', density


	#square unit area width/height
	length_den_width_sq=np.sqrt(density)
	length_den_height_sq=np.sqrt(density)

	length_den_width=length_den_width_sq
	length_den_height=length_den_height_sq


	width=abs(left_edge-right_edge)
	height=abs(top_edge-bottom_edge)


	#check density of control region is the same as dataset region
	print '[pre-expansion] Density (dataset region,control region)', density,length_den_width*length_den_height
	print '[pre-expansion] Area (dataset region,control region)', area_dat,length_den_width*length_den_height*num_members

	#additional checks
	#print 'length_den_width', length_den_width
	#print 'length_den_height', length_den_height

	##############################################
	# 	   Populate control field           #
	##############################################

	#x-axis corridnates
	widths=[]
	x_current=(left_edge-0.5*width)+(0.5*length_den_width)
	x_stop=(right_edge+0.5*width)-(0.5*length_den_width)
	while (x_current <= x_stop):

		if ((x_current>=(left_edge-0.5*width)-length_den_width) and (x_current<=(right_edge+0.5*width)+length_den_width)):
			widths.append(x_current)
		x_current=x_current+length_den_width


	#y-ayis corridnates
	heights=[]
	y_current=(bottom_edge-0.5*height)+(0.5*length_den_height)
	y_stop=(top_edge+0.5*height)-(0.5*length_den_height)
	while (y_current <= y_stop):

		if ((y_current>=(bottom_edge-0.5*height)-length_den_height) and (y_current<=(top_edge+0.5*height)+length_den_height)):
			heights.append(y_current)
		y_current=y_current+length_den_height




	#some empty arrays
	control_x=[]
	control_y=[]


	#output file of control field dataset
	file_control=open('controlfield_%s'%filename+'.csv', 'w')

	#iterate to generate point positions
	for i in range (0,len(widths)):
		width_i=widths[i]

		for ii in range(0, len(heights)):
			height_i=heights[ii]

			control_x.append(width_i)
			control_y.append(height_i)
	
			file_control.write("%.5f,"%width_i+"%.5f \n"%height_i) #print point position to file

	file_control.close()

	##total number of dataset & control field points
	print 'total, len(control_x/dec)',num_members, len(control_x), len(control_y)


	#~~Additional Checks~~#
#	control_width=abs((max(widths)+0.5*length_den_width)-(min(widths)-0.5*length_den_width))
#	control_height=abs((max(heights)+0.5*length_den_height)-(min(heights)-0.5*length_den_height))
#
#	print 'control width', control_width
#	print 'control height', control_height
#	print 'control area', control_width*control_height
#	print 'increased area factor (wrt dataset)', (control_width*control_height)/area_dat
#	print 'size of control field', len(control_x)
#
#	#check density of control and dataset regions is ~=
#	print '[post expansion] density', density, (control_width*control_height)/len(control_x)


	#############################################
	# 		PLOT CONTROL FIELD	#
	#############################################

	plt.scatter(control_x, control_y, marker='+', s=2.5)
	#plt.xlim([min(x_dataset),max(x_dataset)])
	#plt.ylim([min(y_dataset),max(y_dataset)])
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.savefig('controlfield_%s'%filename+'.jpg')
	plt.clf()

##################################################################################
#				END OF PROGRAM					#
##################################################################################
