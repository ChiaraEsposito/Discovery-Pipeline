# Discovery-Pipeline
We take care of the Discover phase of an envisioned ecosystem for managing the Big Data pipeline lifecycle on Computing Continuum. <br />
The Discover phase: The Big Data pipeline definition process starts by analysing a provider’s Dark Data that consists of various sources (static data and event streams). The goal is to discover the structure and properties of the Big Data pipelines and provide input to their definition.

This code consists of:
- two Web APIs implemented using Python and **Flask**[^1]:
  - **backend.py**: uses the PM4PY library[^2] and Process Discovery algorithms to find a suitable process model that describes the order of events/activities of a given event log. In particular, for Process Discovery it has been used the DFG[^3] algorithm, that, together with some input parameters, returns a Digraph in DOT language format.  
  - **frontend.py**: exposes a web application implemented using **html, css and javascript** and communicates with **backend.py** to receive the results of Process Discovery on the base of user inputs. In particular, it uses the Viz.js[^4] library to represents the DOT language format. 

[^1]: For further information how to create Web APIs with Python and Flask, please refer to the following link: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#setting-up .
[^2]: https://pm4py.fit.fraunhofer.de/ .
[^3]: Directly-Follows graphs are graphs where the nodes represent the events/activities in the log and directed edges are present between nodes if there is at least a trace in the log where the source event/activity is followed by the target event/activity. On top of these directed edges, it is easy to represent metrics like frequency (counting the number of times the source event/activity is followed by the target event/activity) and performance (some aggregation, for example, the mean, of time inter-lapsed between the two events/activities).
[^4]: https://unpkg.com/viz.js@1.8.0/viz.js .

## Requirements
The code has been tested using **Python 3.8.12** and **conda 4.10.3**. Other versions are not guaranteed to work correctly.

### To install conda
Follow this links: 
<br />
https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
<br />
Or go directly to Miniconda: https://docs.conda.io/en/latest/miniconda.html

It should work also on Anaconda: https://docs.anaconda.com/anaconda/install/index.html

## Set Up before using the code
It is really suggested to use the already existing environment.
<br /> 
After downloading the file "environment.yml", open the terminal or an Anaconda Prompt, change directory to go to the location where the file is located and do the following steps:

1. Create the environment from the environment.yml file:

```
conda env create -f environment.yml
```
The first line of the yml file sets the new environment's name, in this case "pm4py_env"
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
2. Activate "pm4py_env" in both of them.
3. Change directory to go in the "api" folder downloaded.
4. Run: ```python backend.py``` in one terminal or prompt;
5. Run: ```python frontend.py``` in the other one.
6. Go to your browser on http://127.0.0.1:8080/

## NOTE
If there is an error saying <br />
```from graphviz.dot import Digraph ImportError: cannot import name 'Digraph' from 'graphviz.dot' ``` 
<br /> try changing the line 21 of file "gview.py" through path <br /> 
``` C:\Users\<username>\<miniconda3|anaconda3>\envs\pm4py_env\Lib\site-packages\pm4py\visualization\common\gview.py```
<br />with this line  
<br /> ```from graphviz import Digraph```
