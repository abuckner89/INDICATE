##################################################################################
#	PROGRAM TO IDENTIFY GENERATE EVENLY-SPACED 3D CONTROL FIELD 	#
##################################################################################

# Author: Anne Buckner
# Last modified: 24/05/2019

#import packages
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

##############################################
# 	Load dataset parameters		#
##############################################

#dataset names list
dataset_list=open('./dataset_params_3D.csv', 'r')

#empty array
dataset_name=[]
edge_x1=[]
edge_x2=[]
edge_y1=[]
edge_y2=[]
edge_z1=[]
edge_z2=[]
volume_dataset=[]

#fill array
for names in dataset_list:
	names = names.strip()
	columns_names = names.split(',')
	dataset_name.append(str(columns_names[0]))	
	edge_x1.append(float(columns_names[1]))
	edge_x2.append(float(columns_names[2]))
	edge_y1.append(float(columns_names[3]))
	edge_y2.append(float(columns_names[4]))
	edge_z1.append(float(columns_names[5]))
	edge_z2.append(float(columns_names[6]))
	volume_dataset.append(float(columns_names[7]))

#iterate through datasets in list
for dataset_id in range(0, len(dataset_name)):
	filename=dataset_name[dataset_id]

	
	xmin_edge=edge_x1[dataset_id]
	xmax_edge=edge_x2[dataset_id]
	ymin_edge=edge_y1[dataset_id]
	ymax_edge=edge_y2[dataset_id]
	zmin_edge=edge_z1[dataset_id]
	zmax_edge=edge_z2[dataset_id]
	volume_dat=volume_dataset[dataset_id]

	print 'Dataset name:', filename

	############################################## 	
	# 	Read in dataset  # 	
	############################################## 	

	#open dataset position file 	
	file_dataset=open('./dataset_%s'%filename+'.csv', 'r')
 	
	#some empty arrays 	
	x_dataset=[] 	
	y_dataset=[] 
	z_dataset=[]
	
	#fill arrays 	
	for line_dataset in file_dataset: 		
		line_dataset = line_dataset.strip() 		
		#print line_dataset 		
		columns_dataset = line_dataset.split(',') 		
		x_dataset.append(float(columns_dataset[0]))			
		y_dataset.append(float(columns_dataset[1]))
		z_dataset.append(float(columns_dataset[2]))

	############################################## 	
	# 	Generate control field for the dataset  # 	
	############################################## 	

	#size of dataset 	
	num_members=len(x_dataset) 	
	print 'Size of dataset: ', num_members 	
	
	#density of dataset
	density=volume_dat/num_members 	
	print 'density', density


	#cube unit volume width/height/depth
	length_den_width=density**(1./3.)
	length_den_height=density**(1./3.)
	length_den_depth=density**(1./3.)


	width=abs(xmax_edge-xmin_edge)
	height=abs(ymax_edge-ymin_edge)
	depth=abs(zmax_edge-zmin_edge)

	#check density of control region is the same as dataset region
	print '[pre-expansion] Density (dataset region,control region)', density,length_den_width*length_den_height*length_den_depth
	print '[pre-expansion] Volume (dataset region,control region)', volume_dat,length_den_width*length_den_height*length_den_depth*num_members

	#additional checks
	#print 'length_den_width', length_den_width
	#print 'length_den_height', length_den_height
	#print 'length_den_depth', length_den_depth
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	#fill control field with points

	#x-axis corridnates
	widths=[]
	x_current=(xmin_edge-0.5*width)+(0.5*length_den_width)
	x_stop=(xmax_edge+0.5*width)-(0.5*length_den_width)
	while (x_current <= x_stop):
		if ((x_current>=(xmin_edge-0.5*width)-length_den_width) and (x_current<=(xmax_edge+0.5*width)+length_den_width)):
			widths.append(x_current)
		x_current=x_current+length_den_width


	#y-axis corridnates
	heights=[]
	y_current=(ymin_edge-0.5*height)+(0.5*length_den_height)
	y_stop=(ymax_edge+0.5*height)-(0.5*length_den_height)
	while (y_current <= y_stop):
		if ((y_current>=(ymin_edge-0.5*height)-length_den_height) and (y_current<=(ymax_edge+0.5*height)+length_den_height)):
			heights.append(y_current)
		y_current=y_current+length_den_height


	#z-axis corridnates
	depths=[]
	z_current=(zmin_edge-0.5*depth)+(0.5*length_den_depth)
	z_stop=(zmax_edge+0.5*depth)-(0.5*length_den_depth)
	while (z_current <= z_stop):
		if ((z_current>=(zmin_edge-0.5*depth)-length_den_depth) and (z_current<=(zmax_edge+0.5*depth)+length_den_depth)):
			depths.append(z_current)
		z_current=z_current+length_den_depth

	#generate distrbution for all width/height/depth positions

	#some empty arrays
	control_x=[]
	control_y=[]
	control_z=[]

	#output file of control field dataset
	file_control=open('controlfield_%s'%filename+'.csv', 'w')

	#iterate to generate point positions
	for i in range (0,len(widths)):
		width_i=widths[i]

		for ii in range(0, len(heights)):
			height_i=heights[ii]

			for iii in range(0, len(depths)):
				depth_i=depths[iii]

				control_x.append(width_i)
				control_y.append(height_i)
				control_z.append(depth_i)
	
				file_control.write("%.5f,"%width_i+"%.5f,"%height_i+"%.5f"%depth_i+"\n") #print point position to file

	file_control.close()

	##total number of dataset & control field points
	print 'total, len(control_x/dec)',num_members, len(control_x), len(control_y)


	#~~Additional Checks~~#
#	control_width=abs((max(widths)+0.5*length_den_width)-(min(widths)-0.5*length_den_width))
#	control_height=abs((max(heights)+0.5*length_den_height)-(min(heights)-0.5*length_den_height))
#	control_depth=abs((max(depths)+0.5*length_den_depth)-(min(depths)-0.5*length_den_depth))
#
#	print 'control width', control_width
#	print 'control height', control_height
#	print 'control depth', control_depth
#	print 'control volume', control_width*control_height*control_depth
#	print 'increased volume factor (wrt dataset)', (control_width*control_height*control_depth)/volume_dat
#	print 'size of control field', len(control_x)
#
#	#check density of control and dataset regions is ~=
#	print '[post expansion] density', density, (control_width*control_height*control_depth)/len(control_x)


	#############################################
	# 		PLOT CONTROL FIELD	#
	#############################################


	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	ax.scatter(control_x, control_y, control_z, marker='.')
	#ax.set_xlim(min(x_dataset),max(x_dataset))
	#ax.set_ylim(min(y_dataset),max(y_dataset)) 
	#ax.set_zlim(min(z_dataset),max(z_dataset)) 
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.savefig('controlfield_%s'%filename+'.jpg')
	plt.clf()

##################################################################################
#				END OF PROGRAM					#
##################################################################################
