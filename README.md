# Discovery-Pipeline
We take care of the Discover phase of an envisioned ecosystem for managing the Big Data pipeline lifecycle on Computing Continuum. <br />
The Discover phase: The Big Data pipeline definition process starts by analysing a provider’s Dark Data that consists of various sources (static data and event streams). The goal is to discover the structure and properties of the Big Data pipelines and provide input to their definition.

This code provides two different servers communicating with eachother implemented using **Flask API** and Python footnote[^1], ( **backend.py** and **frontend.py** ) ; and an interface implemented in **html, css and javascript**. 
<br />
For the backend part, we have referred to: https://pm4py.fit.fraunhofer.de/
[^1]: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#setting-up .

## Requirements
Conda or Minicoda installed. 
This code has been implemented using:
**Python 3.8.12**
**conda 4.10.3**

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
1. Open two different terminals or Anaconda Prompts.
2. Change directory to go to the "api" folder downloaded.
3. Run: ```python backend.py``` in one terminal or prompt;
4. Run: ```python frontend.py``` in the other one.
5. Go to your browser on http://127.0.0.1/8080
