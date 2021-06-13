Graph Theory project - 
Ford-Fulkerson algorithm
========
[![python](https://img.shields.io/badge/language-python-%23306998)](https://www.python.org/)

## Table of Contents
* [Analytical part of the project (`analytical_part_graph.pdf` in main directory)](https://github.com/YgLK/graph-project/blob/main/algorithm_analysis.pdf)
* [Analysis and applications of algorithm  (`algorithm_analysis.pdf` in main directory)](https://github.com/YgLK/graph-project/blob/main/algorithm_analysis.pdf)
* [Technologies](#technologies)  
* [Prerequisites](#prerequisites)
* [Setup](#setup)


## Technologies

Python 3.8.5


#### Python libraries used in project:
 * NumPy version 1.20.0
 * NetworkX version 2.5.1
 * PyGraphviz version 1.7
 * Matplotlib version 3.4.2


## Prerequisites

Example of how to install necessary libraries to run the project:
  * Install from requierements.txt file:
```
pip install -r requirements.txt
```
  * Install with commands:
  ```
 pip install numpy
pip install networkx
sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config
pip install pygraphviz
pip install matplotlib
  ```
## Setup
In order to run the project from your command line:
 ```
 # Clone this repository
 git clone https://github.com/...
 
 # Go into the repository
 cd graph-project
 
 # Go into the project directory
 cd graph_theory_project
 
 # Run main.py and tests.py
 python main.py
 python tests.py     
 ```


## Example of graph.json file
File from which information are read

![graph_file_example](https://i.ibb.co/9Wd70NR/graph-file-example.png)

### Two executable files:
  * main.py - run algorithm on graph read from json file
  * tests.py - test algorithm on randomly picked graphs
                  
                  Both compares results with built-in Networkx maximum flow algorithm.
 
### To visualize and test custom graphs add .json file with your graph to directory of the project and make changes in  `main.py` file:
```
...
10  filename = 'graph.json'     # Change filename in order to run algorithm on different 
...                             # graph.json file e.g. filename = 'graph_template.json'
...
37  plt.savefig("graph.png")    # Enter the name of graph picture to be saved e.g. plt.savefig("graph_template.png")
...                             # Picture will appear in project directory

```
### Simple example of generated graph visualization

<p align="center"><kbd>
  <img width="460" height="460" src="https://i.ibb.co/HTqDC3W/graph.png">
</kbd></p>
