# Topology files: from LAMMPS `.data` file to `.psf` format

## Generate a topology `.psf` using VMD
The type of file I found to faithfully reproduce a "movie" of the folding protein is `.dcd`. This file can be dumped from lammps using the command

```bash
dump test all dcd nsteps prot_name.dcd
```

This file contains *only* coordinates and it is not sufficient by itself, one needs also a topology file such as the `.psf` file.

How to generate the `.psf` file: this process needs a snapshot of the initial state of the simulation, something that is provided by `write_data`. Therefore, at the beginning of the simulation save a `.data` file with the command:

```bash
write_data prot_name_init.data nocoeff
```

`nocoeff` does not save the force filed.

Now with have a `.dcd` and a `.data` files, we need to transform the `.data` into a `.psf`. This is done by mean of VMD.
Go to the terminal (inside the *data* folder) and open VMD with `vmd`. These are the commands in order to create the topology file:

```bash
topo readlammpsdata prot_name.data -style molecular
```
```bash
animate write psf prot_name.psf
```

The `.data` file will be loaded into VMD but this is not important.
Right after that, you need to load the `.dcd` file and you will have the movie.

An useful *drawing method* to visualize the polypetide chain is *bonds*.

## Topology file `.psf` using VMD script

The idea is to put the last two commands into a `to_psf.tlc` file and from terminal run the following:
```bash
vmd -eofexit < to_psf.tlc
```
The `-eofexit` option closes VMD after executing the script. Note that we need to run VMD in its graphical form in order to use the `topo` command; run something like `vmd -dispdev text` does not allow to compute the topology file.