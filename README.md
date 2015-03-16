# Exploring Data Structures in Python

## About

This repo is the skeleton for an exploratory, TDD-based course on Data Structures using Python. The series is based on [Dave Astels' DBC Deep Dives](https://github.com/dastels/dbc-deep-dives), and adapted for implementation in, and of, the Python language. 

I've done a bit of asking around, and attempted to adopt most commonly followed practices in the world of python testing. Tests are written using the built in unittest framework and run using [nose](https://nose.readthedocs.org/en/latest/). A few naming conventions might look different, because I've framed them around what I think is the best way to teach the material through TDD (and a bit of BDD).

## Using this Repo

### Dependencies

#### Here's a detailed breakdown is the software you'll need in order to work through these exercises:

- You'll need **git**, for cloning the repo:
	- First, double check to see if you already have it:
	```git --version```
	- If you don't, visit [this website](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for instructions.
- *Make sure you have python installed*, and check the version: this repo uses 2.x
	- ```python --version``` will check the version you're using
	- if you're using python 3.x, and you don't already have a tool like pyenv installed, go ahead and [install it](https://github.com/yyuu/pyenv). After it's installed, check out the docs for which commands will set up your environment.
		- don't forget #3 in the installation instructions. That's important.
		- try:
		```$: pyenv install 2.7.9
		$: pyenv shell 2.7.9```
- install [**nose**](https://nose.readthedocs.org/en/latest/):
	```pip install nose```

### Getting started

- First, clone the repo:
	```git clone git@github.com:celeen/PythonDataStructures.git```
- Then choose the Data Structure you're exploring- take, for example, Lists.
	- cd into the tests directory, and run ```nosetests list_tests.py```
		- confirm it runs, and that everything passes
	- Find the related file in the main package, and delete its contents.
		- run the tests again; confirm they run and that nothing passes.

**Happy Coding!**

## Feedback

Any feedback is welcome in the form of PRs, issues, or emails. This is a work in progress.	
