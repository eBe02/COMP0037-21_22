# COMP0037-21_22
Repository for the source code for COMP0037 Academic year 2021-2022


The code in this repository will be progressively updated during the term.

We will only be using a single branch. The different activities will appear as subdirectories.

# Lab exercises for COMP0037 Robotic Systems

## Introduction


* Apply for a student licence on JetBrain to download [PyCharm](https://www.jetbrains.com/shop/eform/students)
* Install [PyCharm Professional ID](https://www.jetbrains.com/pycharm/download/#section=windows) (free for students)
* Install [Python 3](https://www.python.org/downloads/) (if you don't already have it - avoid Python 3.10)
* Download the material from the Moodle page of the module: [COMP0037 Robotic Systems](https://moodle.ucl.ac.uk/course/view.php?id=1392&section=0) and put the lab material in a folder named "comp0037-labs"
* Open the folder "comp0037-labs" in PyCharm
* Create and activate a virtual environment:
    ```
    cd comp0037-labs
    python -m venv .venv
    # On Unix/MacOS:
    source .venv/bin/activate
    # On Windows:
    .venv\Scripts\activate.bat
    ```
* Install Python package requirements:
    ```sh
    pip install -r requirements.txt
    ```
* Read the week's lab exercises document `COMP0037_Lab_N.pdf`
* Add your code to the script `Lab_1.py`
* Run the script either from the command line to see your code in action:
    ```sh
    python Lab_N.py
    ```
  or directly using the play button in the notebook. 

## About

This repository contains lab exercises for the [COMP0037 Robotic Systems](https://moodle.ucl.ac.uk/course/view.php?id=1392&section=0) module for taught MSc students at UCL, delivered in Spring 2022. Exercises are designed to be attempted in the on-campus lab sessions on Friday afternoon, though you are free to do additional work in your own time if you wish.

Lab attendance will be monitored, but the exercises are **not graded**. You are welcome to discuss and help each other with these tasks and to ask for assistance and clarification from the TAs, but there is nothing to be gained by simply copying each others' work.

### Contents

Exercises for week *N* are specified in document `COMP0037_Lab_N.pdf`. Skeleton code for the exercises is provided in the script `Lab_N.py`. You should add your solution code to this file. The script can be run at the command line like this:
```sh
python Lab_N.py
```

In addition to the spec and script for each week, there are a few other files in the repo:

* `README.md`: this file.
* `requirements.txt`: a list of additional Python packages to install.
* `LICENSE`: text of the MIT License that applies to all code and documentation in this repository. (Summary: in the unlikely event that you have any reason to do so, you are free to reuse this material for any purpose you like.)


## Python Setup

The exercises require a local installation of Python 3, along with a number of additional packages for numerical programming, plotting and machine learning. We suggest using the latest stable release of Python 3.9 (currently 3.9.7) from [python.org](https://www.python.org/downloads/). (Python 3.10 has recently been released but many students have had issues with PyPI dependencies not yet being up to date, so install this version with caution.). Although we recommend a more recent Python, the code has also been tested on Python 3.6.8, which is the version currently installed on some of the CS lab machines. It is possible, albeit suboptimal, to set up and run the exercises on one of those machines via SSH.

### Virtual Environments

The package requirements for the lab exercises are pretty vanilla, but we strongly recommend working in a dedicated [virtual environment](https://docs.python.org/3/tutorial/venv.html) in order to avoid any conflicts or compatibility issues with any other Python work you may be doing.

There are several options for how and where to set up such a virtual environment. If you already have experience doing so then feel free to use any configuration you are comfortable with. If you haven't done this before and/or would rather not think about it, follow the default setup instructions below.

#### Default virtual environment setup

A straightforward way to configure your virtual environment is to store it in a hidden subdirectory of your working directory (ie, the directory containing the folder comp0037-labs). 
```sh
cd comp0037-labs
```
Initialise a new virtual environment:
```sh
python -m venv .venv
```
(The name `.venv` is a reasonably common convention that should be recognised by Python-aware editors such as VSCode and PyCharm, but you can use a different and more informative name if you wish. In that case, also replace `.venv` with your chosen name in the commands below.)

**Make the virtual environment active**. This mean it will be used for any python commands or scripts you execute in the current shell. Activation occurs only for the specific terminal window you do the activation in, and it ends when you close the window (or issue the comment `deactivate`). So you'll need to do this every time you open a new terminal that you want to run lab scripts from.

The command you use to activate the environment varies depending on your operating system and terminal provided in PyCharm.

On Unix-esque systems (Linux and MacOS) 
```sh
source .venv/bin/activate
```

On Windows systems:
```sh
.venv\Scripts\activate.bat
```
When the virtual environment is active, your commmand prompt will be modified with the prefix `(.venv)`.

### Installing Required Packages

With your virtual environment active, you should be able to install all required packages using `pip`, like this:
```sh
pip install -r requirements.txt 
```

## Feedback

Please post questions, comments, issues or bug reports to the [COMP0037 Moodle forum](https://moodle.ucl.ac.uk/course/view.php?id=1392&section=1#tabs-tree-start) or raise them with the TAs during your lab sessions.
