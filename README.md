# Discovery-Pipeline
1) Discover: The Big Data pipeline definition process starts by analysing a provider’s Dark Data that consists of various sources (static data and event streams). The goal is to discover the structure and properties of the Big Data pipelines and provide input to their definition.

## Requirements
Conda or Minicoda installed. 

### To install conda or miniconda
Follow this link: 
<br />
Conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
<br />
Miniconda: https://docs.conda.io/en/latest/miniconda.html

## Set Up
After downloading the file, use the terminal or an Anaconda Prompt for the following steps:

1. Create the environment from the environment.yml file:

```
conda env create -f environment.yml
```
The first line of the yml file sets the new environment's name.
<br />
2. Activate the new environment: 
```
conda activate pm4py_env
```

3. Verify that the new environment was installed correctly:

```
conda env list
```
or 
```
conda info --envs.
```
## To use the code
1. Open two different terminals or Anaconda Prompts
2. Go to the "api" folder
3. Run: ```python backend.py``` in one terminal or prompt
4. Run: ```python frontend.py``` in the other one.
5. Go to your browser on http://127.0.0.1/8080
