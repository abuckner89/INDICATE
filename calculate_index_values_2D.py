##################################################################################
#	PROGRAM TO CALCULATE INDICATE INDEX VALUES FOR 2D DATASETS		#
##################################################################################

# Author: Anne Buckner
# Last modified: 24/05/2019

#import packages
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.spatial.distance import cdist


##############################################
# 	Open dataset Names File		#
##############################################

#dataset names list
dataset_list=open('./dataset_params_2D.csv', 'r')

#empty array
dataset_name=[]

#fill array
for names in dataset_list:
	names = names.strip()
	columns_names = names.split(',')
	dataset_name.append(str(columns_names[0]))	


#iterate through datasets in list
for dataset_id in range(0, len(dataset_name)):
	start_time = time.time()

	#dataset name
	filename=dataset_name[dataset_id]

	print 'Dataset:', filename

	##############################################
	#  Open dataset file	#
	##############################################

	#open dataset and control field files
	file_dataset=open('./dataset_%s'%filename+'.csv', 'r')

	print 'Opening...', file_dataset

	#some empty arrays
	xy_dataset=[]

	#fill arrays
	for line_dataset in file_dataset:
		line_dataset = line_dataset.strip()
		columns_dataset = line_dataset.split(',')
		x_dat=float(columns_dataset[0])	
		y_dat=float(columns_dataset[1])
		xy_dataset.append([x_dat, y_dat])

	file_dataset.close()

	##############################################
	#  Open control field file	#
	##############################################

	file_control=open('./controlfield_%s'%filename+'.csv', 'r')

	#some empty arrays
	xy_control=[]

	for line_control in file_control:
		line_control = line_control.strip()
		columns_control = line_control.split(',')
		x_control=float(columns_control[0])	
		y_control=float(columns_control[1])
		xy_control.append([x_control, y_control])

	file_control.close()
	###################################################################
	# 		Determine Member Structure Indexs #
	###################################################################

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#determine distance from dataset point i to every control field point j

	#nearest neighbour number
	NN=5

	dist_array1 = cdist(xy_dataset, xy_control, 'euclidean')

	nth_dist=[]

	for i in range(0, len(dist_array1)):
		dist_control=dist_array1[i]

		sorted_control=sorted(dist_control) #sort dist_control small->large

		distance_NN=sorted_control[NN-1] # distance to Nth nearest neigbour = Nth in sorted list

		nth_dist.append(distance_NN) #NN distance

	ndist=np.mean(nth_dist)
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#determine distance from dataset point i to every other dataset point j

	dataset_index=[]

	dist_array2 = cdist(xy_dataset, xy_dataset, 'euclidean')

	for i in range(0, len(dist_array2)):
		dist_dataset=dist_array2[i]

		neighbours= [i for i in dist_dataset if i <= ndist]
		count_ndataset=len(neighbours)-1 # exclude distance to itself
		P_i=float(count_ndataset)/float(NN) # calculate index for point i
		dataset_index.append(P_i) #put index in an array


	file_index=open('./dataset_%s'%filename+'_indexvals.csv','w')


	for item in range(0, len(xy_dataset)):

		x_item=xy_dataset[item][0]
		y_item=xy_dataset[item][1]
		index_item=dataset_index[item]
	
		file_index.write('%f,'%x_item+'%f,'%y_item+'%f\n'%index_item)

	elapsed_time = time.time() - start_time

	print 'file: ', filename,'Time taken: ', elapsed_time

	file_index.close()



##################################################################################
#				END OF PROGRAM					#
##################################################################################