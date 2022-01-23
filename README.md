# Discovery-Pipeline
1) Discover: The Big Data pipeline definition process starts by analysing a provider’s Dark Data that consists of various sources (static data and event streams). The goal is to discover the structure and properties of the Big Data pipelines and provide input to their definition.

# Requirements
Conda or Minicoda installed. 
## To install conda or miniconda
Follow this link: 
Conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
Miniconda: https://docs.conda.io/en/latest/miniconda.html

# Set Up
After downloading the file, use the terminal or an Anaconda Prompt for the following steps:

Create the environment from the environment.yml file:

'''
conda env create -f environment.yml
'''
The first line of the yml file sets the new environment's name.

Activate the new environment: 
'''
conda activate pm4py_env
'''

Verify that the new environment was installed correctly:

'''
conda env list
''' 
or 
'''
conda info --envs.
'''
