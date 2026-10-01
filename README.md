# This file is actively being written. This repo is only visible so that it can be installed without a headache.

# Assorted Tools

This is a library of very small tools created for my personal use. They only exist to solve minor inconveniences I have come across from time to time. This repository exists because if I needed these tools, somebody else probably does too.

As for what each function does, in the absence of full documentation, each function has a docstring explaining it.

# Installation

Requires Python 3.13 or newer.

The ansiText color and style codes require a compatible terminal. If you're using a modern device and operating system, this will likely not be an issue.

## Short Instructions

Install in a venv via pip using
```
python -m pip install https://github.com/Probably-Artemis/assorted-python-tools/archive/refs/heads/main.zip
```
<sup>Outside of a venv, Mac and Linux users may need to use `python3` instead.</sup>

## Long Instructions

(For those who have no clue what the above command does)

### Step 1

You must have Python installed, at least version 3.13 or newer. The installation process varies by operating system.

Download Python from [python.org](https://www.python.org/downloads/).

If you are on Mac, you may already have Python installed, but it is likely too old.

If you are on linux, Python is preinstalled but may not be up to date enough. On Debian and Ubuntu, you'll need to run `sudo apt install python3-venv`.

To check your version, run:
```
python3 --version
```
or on Windows:
```
py --version
```

### Step 2 (VSCode route)

Install VSCode and its Python extension. Open your project's folder in VSCode. **Not just a single .py file, the entire folder.**

Press `Ctrl+Shift+P` to open the Command Palette, type in and run `Python: Create Environment`, choose `Venv`, and select your installed Python instance.

New terminals in VSCode should open in the venv, indicated by `(.venv)` being shown in the prompt. Preexisting terminals won't be in the venv, so close and reopen them.

<sup>This route also works if you're using the CS50 IDE, as that is just a version of VSCode.</sup>

### Step 2 (the other option)

Open your project folder in a terminal. Consult the table below for the commands to run for your given operating system.

| | Windows | Mac / Linux |
|---|---|---|
|Create|`py -m venv .venv`|`python3 -m venv .venv`|
|Activate|`.venv\Scripts\activate`|`source .venv/bin/activate`|

To create your venv, use the Create command for your specific operating system.

Each time you open a terminal to run your code, you must activate your venv, using the Activate command for your specific operating system.

#### A note for Windows users:

Sometimes, activating your venv may fail, as PowerShell will tell you "running scripts is disabled on this system". To fix this, run the following command to enable running scripts.
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 3

With your venv activated, run the installation command.
```
python -m pip install https://github.com/Probably-Artemis/assorted-python-tools/archive/refs/heads/main.zip
```
To update which version you have installed, simply append `--upgrade` to the end of the installation command.

If you use git, add `.venv/` to your .gitignore file.

### Step 4

At this point, you should be all set. Simply import the tools you want, and use them. For example:
```python
from assorted_tools.misc import clear, newsection
```
You may use a wildcard import to import everything a specific module provides, but this is not advised.

# Using these tools

[TODO]

# Contributing
If something is broken or badly written, open an issue! If you know how to fix it yourself, fork the repo, fix it, and open a pull request! If you have tools of your own you'd like to add, open a pull request!