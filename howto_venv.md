# How to create a venv and live a happy life <!-- omit in toc -->

- [A note for Manjaro/Arch users](#a-note-for-manjaroarch-users)
  - [Best practice](#best-practice)
- [Create, activate, deactivate and destroy](#create-activate-deactivate-and-destroy)
- [Save a list of all dependences installed in a venv](#save-a-list-of-all-dependences-installed-in-a-venv)
- [Create a venv and use Jupyter Lab](#create-a-venv-and-use-jupyter-lab)

Here I summarize my knowledge, in a very brief form, about the creation, the usage and maintenance of a Virtual Environment for Python projects. 
Please note that creating a virtual environment is always a good practice to manage library dependency of ones project. You don't want an update to break you code, and you want to keep everything under control.

Here I use venv as a tool. I assume there are better and more flexible option, for now I stick with the basic because I don't need too overcomplicate things. 

## A note for Manjaro/Arch users
This Distros, and probably other ones, uses python packages provided by their repos. When you want to use Python globally, across multiple users, you want to install several packages globally. 
Moreover, these libraries from the repos are the one that are kept updated and managed by the package manager (such as `pacman`, `yay` or others). 
Therefore, do not mix up those global package with the one installed by `pip`.

### Best practice
If you want to install a package **globally**:
```
yay -Syu python-pkgname
```

If you want to install a package when you are inside a virtual env:
```
python -m pip install pkgname
```

Generally, using a virtual environment is better and will be the future of linux distros to set by default the second option. 

## Create, activate, deactivate and destroy

> requires python >= 3.3

Create a directory for the project and create a virtual env with:
```
mkdir testvenv
python -m venv testvenv
``` 
To activate the environment and begin to use it type:
```
source testvenv/bin/activate
```

Now, **all** the packages you install using pip, for example:
```
python -m pip install jupyterlab
```
will automatically install these packages inside `testvenv/lib/python3.x/site-packages` and **not** globally. 

To deactivate the environment and go back to the global python, use (no matter where you are):
```
deactivate
```

To **remove** the project and the venv just delete everything:
```
rm -rf testvenv
```

## Save a list of all dependences installed in a venv

Ones you create an envirnment and want to save the list of libraries, with their current version, to use it as a reference list for future venv you just need to activate your venv and use the command:
```
python -m pip freeze > requirements.txt 
```

This save a list of this kind:
```
anyio==3.3.3
argon2-cffi==21.1.0
attrs==21.2.0
Babel==2.9.1
backcall==0.2.0
biopython==1.79
bleach==4.1.0
certifi==2021.10.8
cffi==1.14.6
```
where all the installed packages are saved with the current version.

To use it in future environments or to distribute your code to someone else, once you created and activated your environment you can use the following:
```
python -m pip install -r requirements.txt
```

## Create a venv and use Jupyter Lab

One can create a virtual env and use from there the Jupyter Lab framework and everything it gives.

Once you have created your venv and activated it, just install `jupyterlab`:
```
python -m pip jupyterlab
```
and all its dependences, `ipython` kernel included, will be installed.

Then you can use it by typing:
```
jupyter lab 
```

>In order to use the proper `jupyterlab`, avoiding problem with the global one, you need to deactivate and reactivate the venv after the installation.
>
> To check if you are using the correct one, just check with `which jupyter`