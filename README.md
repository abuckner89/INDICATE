~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ABOUT INDICATE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The INDICATE tool was developed using the Anaconda distribution of Python v2.7
as part of the SFM Project. (For more info see: www.starformmapper.org/)

INDICATE is a local clustering statistic which quantifies the degree of 
association of each point in a 2+D discrete dataset through comparison 
to an evenly spaced control field of the same size. Arguably INDICATE’s 
greatest strength is that, unlike most established clustering tools, it 
requires no a priori knowledge of the size, shape or substructure present 
in a distribution.

When applied to a dataset of size S, INDICATE derives an index  I_{j,N}  for 
every data point using:

I_{j,N} = Nr / N

where N is the nearest neighbour number (a user-defined integer) and Nr
is the number of nearest neighbours to data point j within a radius of the 
mean Euclidean distance, r, of every data point to its Nth nearest neighbour
in the control field. The index is a unitless ratio with a value in the range  
0 ≤ I_{j,N} ≤ (S −1)/N such that the higher the value, the more spatially 
clustered a data point.

For each dataset the index is calibrated by the user so that significant values 
can be identified. A hundred realisations of a random distribution of the same 
size S, and in the same parameter space, as the dataset should be generated by 
the user. INDICATE is applied to the random samples to identify typical index 
values, I_{ran,N} of randomly distributed data points. Point j is considered 
spatially clustered if I_{j,N} >> I_{ran,N}.

Further details of the underlying concepts are described in 
Buckner et al. (2019a).


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RUNNING INDICATE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


INDICATE consists of three scripts that must be run in the
order:

1) generate_controlfield

2) calculate_index_values

3) find_significant_index_values


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Script: generate_controlfield
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AUTHOR: Anne S.M. Buckner
 
 
 
 
LAST MODIFIED: 

22/05/19 [2D version]

22/05/19 [3D version]




DESCRIPTION:

Generates the evenly spaced control field for the dataset. Scripts for 2D and 
3D scripts indicated with a suffix prior to ‘.py’ of ‘_2D’ and ‘_3D’ respectively. 





INPUT:

- ‘dataset_name.csv’

A CSV file containing the positions of the data points in dataset ‘name’. 
Each row  to contain the position of a single data point. Columns give position 
in each axis i.e.

|X| Y| Z [,if 3D]|  

- ‘dataset_params_[DIM]D.csv’

A CSV file containing the  parameters of the dataset. File should contain a 
single row per dataset with the following columns:

| Dataset Name | min(X) | max(X) |  min(Y) | max(Y) |  min(Z) [,if 3D]| 
max(Z) [,if 3D]| Surface Area or Volume|

Note, the surface area should be given as a unitless float for 2D datasets, and 
the volume for 3D datasets. Replace ‘[DIM]’ with 2 or 3, depending on dimensions 
of dataset e.g.  dataset_params_2D.csv.





OUTPUT:  

- ‘controlfield_name.csv’ 

A CSV file containing the positions of the control field data points for dataset 
‘name’. The control field has the same number of dimensions as the 
dataset_name.csv file. Each row contains the position of a single data 
point. Columns give position in each axis i.e.

|X| Y| Z [,if 3D]|

- ‘controlfield_name.jpg’

A plot of the control field for dataset ‘name’.





PACKAGE REQUIREMENTS: 

The following python packages must be installed to run this script:

    - matplotlib
    - numpy
    - mpl_toolkits




EXAMPLE RUN COMMAND:

python calculate_index_values_2D.py  [linux/ iOS]

python.exe C:\file_location\calculate_index_values_2D.py [Windows]



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Script: calculate_index_values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AUTHOR: Anne S.M. Buckner
 
 
 
 
LAST MODIFIED: 

22/05/19 [2D version]

22/05/19 [3D version]




DESCRIPTION:

Calculates the index value I_{j,N} for every data point. Default nearest neighbour
number is N=5.




INPUT

- ‘dataset_params_[DIM]D.csv’

A CSV file containing the  parameters of the dataset. File should contain a 
single row per dataset with the following columns:

| Dataset Name | min(X) | max(X) |  min(Y) | max(Y) |  min(Z) [,if 3D]| 
max(Z) [,if 3D]| Surface Area or Volume|

Note, the surface area should be given as a unitless float for 2D datasets, 
and the volume for 3D datasets. Replace ‘[DIM]’ with 2 or 3, depending on dimensions 
of dataset e.g.  dataset_params_2D.csv.


- ‘dataset_name.csv’

A CSV file containing the positions of the data points in dataset ‘name’. 
Each row  to contain the position of a single data point. Columns give position 
in each axis i.e.

|X| Y| Z [,if 3D]|  
 
- ‘controlfield_name.csv’

A CSV file containing the positions of the control field data points for dataset
‘name’. The control field has the same number of dimensions as the 
dataset_name.csv file. Each row contains the position of a single data point. 
Columns give position in each axis i.e.

|X| Y| Z [,if 3D]|



OUTPUT:

- dataset_indexvals.csv

A copy of the original dataset.csv file appended with an additional column 
containing the index values assigned to each data point i.e.

|X| Y| Z [,if 3D]| Index value|



PACKAGE RUN COMMANDS:

The following packages must be installed to run this script:

 - matplotlib
 - numpy
 - time
 - scipy




EXAMPLE RUN COMMAND:

python calculate_index_values_2D.py  [linux/ iOS]


python.exe C:\file_location\calculate_index_values_2D.py [Windows]



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Script: find_significant_index_values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AUTHOR: Anne S.M. Buckner
 
 
 
 
LAST MODIFIED: 

22/05/19 [2D version]

22/05/19 [3D version]




DESCRIPTION:

Identifies significant (spatially clustered) index values for dataset_name.


INPUT:

- ‘dataset_name_indexvals.csv’

Output of calculate_index_values.py. A CSV file of the dataset_name.csv 
file appended with an additional column containing the index values assigned 
to each data point i.e.

|X| Y| Z [,if 3D]| Index value|

- ‘dataset_name_random_[NUM]_indexvals.csv’

Output of calculate_index_values.py when applied to a randomly distributed 
dataset.  User should generate 100 randomly distributed dataset of the same 
size as dataset_name and in the same parameter space. The datafiles should 
following the following naming convention:

dataset_name_random_[NUM].csv

where [NUM] is an integer identifying the random dataset realisation 
number 1-100.  Run calculate_index_values_[DIM]D_random.py on the random 
datasets to produce dataset_name_randon_[NUM]_indexvals.csv. 


OUTPUT:

- terminal printout stating the ‘significance threshold’ i.e. the index value 
above which a data point in dataset_name is considered spatially clustered 
above random.

- interactive plot of dataset, with an overlay of significantly clustered points index 
values.


PACKAGE REQUIREMENTS:

The following packages must be installed to run this script:

   - matplotlib                
   - numpy  
   - mpl_toolkits

EXAMPLE RUN COMMAND:

python find_significant_index_values_2D.py  [linux/ iOS]


python.exe C:\file_location\find_significant_index_values_2D.py [Windows]
