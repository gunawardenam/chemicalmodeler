# Morgan and MACCS Fingerprint Chemical Modeler 
This package can be used to train morgan and MACCS fingerprint models for different chemical species in order to predict lipophilicity data.

# Description
As previously mentioned, this package is set up in order to train simple models for morgan and MACCS key fingerprints given a certain chemical species, then make a comparison between the two to see which model has the best metrics. Models will be multilayer perceptron (MLP) Regressor models, and RMSE will be calculated for use in the comparison. Additionally, the code is designed so that you may first convert a given list of SMILES into the two fingerprint types.

# Project File Structure
chemicalmodeler
 -> working_packages_scripts
 -----> functions.py
 -----> Lipophilicity.csv
 -----> modeler.ipynb
 -> environment.yml
 -> License
 -> README.md

# Installation Instructions and Conda Environment Setup
Note that all dependencies can be found in the environment.yml file.

Here are some general instructions for getting started:
1) clone the repository
    'git clone https://github.com/gunawardenam/chemicalmodeler.git
    cd chemicalmodeler'
2) create and activate your conda environment
    'conda env create -f environment.yml'
3)  'conda activate chemicalmodeler'
4) run the jupyter notebook entitler 'modeler.ipynb'. Further instructions for the execution can be seen in the section below.

# Program Execution Instructions
To get started,download the package, review the license and environoment information, then open the "modeler.ipynb" file and review the code. This is the main body of working code to be used. For package development purposes, the "Lipophilicity.csv" has been used for applying functions and training the models. However, you will want to first replace that dataset with your dataset of interest.

From there, you can run the code to carry out the modeling and caluclation of metrics. The main steps executed by the code are the following:
1) Generating morgan fingerprints and MACCS keys based on the SMILES strings provided in your dataset
2) splitting the newly generated fingerprints inot test and training sets
3) Converting the fingerprints into numpy arrays in preparation for modeling
4) Visualizing the response values (in this case, lipophilicity values) and applying a standard scaler to the data based on its distribution. *Note you may wish to edit this scaler type used based on your response data.
5) training two MLP Regressor models, one using the morgan fingerprint data and the other using the MACCS keys
6) Calculating the RMSEs for each to be used as comparison metrics and printing out the results


# Author Information
Maddie Gunawardena
gunawardenam@vcu.edu

# License
License information can be found in the included LICENSE file.