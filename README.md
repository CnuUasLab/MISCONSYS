# MISCONSYS
<b>Mis</b>sion <b>Con</b>trol <b>Sys</b>tem for Ground Station Control

## Current Standing
[![Build Status](https://travis-ci.org/CnuUasLab/MISCONSYS.svg?branch=master)](https://travis-ci.org/CnuUasLab/MISCONSYS)



## Execution
There are a number of packages that must be installed. For the purposes of integration, python's
testing package must be installed to instantiate tests for all components of the system.
```bash
$ sudo apt-get install python-logilab-common
$ sudo apt-get install python-pip
$ git clone git@github.com:/CnuUasLab/MISCONSYS.git
```
If you do not have SSH recognition on your system for your github account type the following to clone the git repository.
```bash
$ git clone http://github.com/CnuUasLab/MISCONSYS.git
```

MISCONSYS is consisted of several individual systems meant for full integration of the system.
These systems work in tandem with one another.
<b>For a successful setup of the overall system run the following:</b>

```bash
$ # From the Root of the repository
$ git submodule update --init --recursive
$ sudo -H pip install -r ./Requirements.txt
```

#### IMG
From the root of the project:
```
$ cd ./img
$ python manage.py runserver 5001
```

#### Interoperability
From the root of the project:
```
$ cd ./Interoperability/src/
$ python main.py
```
