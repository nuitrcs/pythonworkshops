# Northwestern Research Computing Python Workshops

This repository contains materials for Python workshops taught by [Research
Computing Services](http://www.it.northwestern.edu/research/).

All Python files are written using Python 3.6.  We recommend the Anaconda
distribution of Python ([download](https://www.continuum.io/downloads)), which
includes many packages used by the scripts above, as well as Jupyter for running
notebooks.

You can preview Jupyter notebooks and Python scripts by clicking on the files
above. To download, click on the file, then click the raw button, and then save
the file. Or download the whole repository: see the green Clone or Download
button above.  (Cloning uses git; if you don't know git, just download the
repository as a .zip file.)

Some workshop materials are Python scripts (.py files) instead of Jupyter
notebooks.  We recommend the [PyCharm](https://www.jetbrains.com/pycharm/)
Python IDE for editing and running Python scripts.  Free [Student
licenses](https://www.jetbrains.com/student/) are available for academic use. 

## Creating Conda environments

[Conda](https://conda.io/docs/using/using.html), part of the Anaconda
distribution, is a utility that creates self-contained python environments. This
repository contains an environment definition file that can be used to create a
conda environment that has the necessary libraries for the workshops. To use it,
open an Anaconda prompt (on Windows, Start -> Anaconda3 -> Anaconda Prompt),
`cd` to the directory containing this repository, then create the environment
with

    conda env create -f environment.yml

This will create and activate a conda environment called "pythonworkshops" and
install the necessary libraries and tools. For Windows users, to activate the
environment again later, use this command:

    activate pythonworkshops

And on Linux or OS X, use this command:

    source activate pythonworkshops

**Note**: If you are using Anaconda, the default environment should already have
all of these libraries installed, so creating a separate environment is not
strictly necessary and you are free to use the default environment. Separate,
self-contained environments are useful if you work on multiple different
projects and need to keep their dependencies separate.

## More Resources

See [Resources](resources.md) for a listing of general Python resources,
tutorials, and reference materials.  Additional resources are linked in the
individual workshop directories.

## Note

This repository is still evolving and is not yet complete.