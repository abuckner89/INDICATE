##################################################################################
#	 PROGRAM TO IDENTIFY AND PLOT SIGNIFCANT INDEX VALUES 	#
##################################################################################

# Author: Anne Buckner
# Last modified: 24/05/2019

#import packages
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

############################################## 
# 	Open dataset Names File		# 
############################################## 
#dataset names list 
dataset_list=open('./dataset_params_3D.csv', 'r') 

#empty array 
dataset_name=[] 

#fill array 
for names in dataset_list: 	
	names = names.strip() 	
	columns_names = names.split(',') 	
	dataset_name.append(str(columns_names[0]))	


#iterate through datasets in list 
for dataset_id in range(0, len(dataset_name)): 	

	#dataset name 	
	filename=dataset_name[dataset_id] 
	
	print 'Dataset', filename 	

	############################################## 	
	#  Open dataset index file	# 	
	############################################## 	
	#open dataset and control field files 	
	file_dataset=open('./dataset_%s'%filename+'_indexvals.csv', 'r') 	

	
	#some empty arrays 	
	x_dat=[] 	
	y_dat=[] 
	z_dat=[] 		
	indexvals_dat=[] 	

	#fill arrays 	
	for line_dataset in file_dataset: 		
		line_dataset = line_dataset.strip() 		
		columns_dataset = line_dataset.split(',') 		
		x_dat.append(float(columns_dataset[0]))		
		y_dat.append(float(columns_dataset[1]))
		z_dat.append(float(columns_dataset[2]))
		indexvals_dat.append(float(columns_dataset[3]))

	file_dataset.close()
    
	############################################## 	
	#  Open random index file	# 	
	############################################## 	
	
	for i in range(1,101,1):
    	#open random and control field files 	
	    	file_random=open('./dataset_%s'%filename+'_random_%d'%i+'_indexvals.csv', 'r') 	
	    	
	    	#some empty arrays 	
	    	indexvals_ran=[] 	
	    
	    	#fill arrays 	
	    	for line_random in file_random: 		
	    		line_random = line_random.strip() 		
	    		columns_random = line_random.split(',') 		
	    		indexvals_ran.append(float(columns_random[3]))

		file_random.close()
		
	#check
	print 'size of dataset and random', len(indexvals_dat), len(indexvals_ran)
    
	############################################## 	
	#  	Significance threshold	# 	
	############################################## 	

	#mean I_{j,N} random
	mean_Iran=np.mean(indexvals_ran)

	#standard deviation I_{j,N} random
	std_Iran=np.std(indexvals_ran)


	sig_threshold=mean_Iran+(3.*std_Iran)

	print 'significance threshold:', sig_threshold


	############################################## 	
	#  	Identify clustered points	# 	
	############################################## 	

	x_clustered=[]
	y_clustered=[]
	z_clustered=[]
	indexvals_clustered=[]

	x_Nclustered=[]
	y_Nclustered=[]
	z_Nclustered=[]
	
	for i in range(0, len(x_dat)):

		x_i=x_dat[i]
		y_i=y_dat[i]
		z_i=z_dat[i]
		I_i=indexvals_dat[i]


		if(I_i>sig_threshold):
			x_clustered.append(x_i)
			y_clustered.append(y_i)
			z_clustered.append(z_i)
			indexvals_clustered.append(I_i)


		else:
			x_Nclustered.append(x_i)
			y_Nclustered.append(y_i)
			z_Nclustered.append(z_i)

	print 'number of signficantly clustered points:', len(x_clustered), '/', len(x_dat)


	fig=plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	ax.scatter(x_Nclustered, y_Nclustered, z_Nclustered, color='grey', s=0.5, marker='.', alpha=0.5)
	cb1=ax.scatter(x_clustered, y_clustered, z_clustered, c=indexvals_clustered, cmap='jet', marker='.', s=2.)
	cbar =plt.colorbar(cb1, ax=ax)
	cbar.set_label(r'$I_{N}$') # change N -> nearest neighbour number interger
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()
	plt.clf()

