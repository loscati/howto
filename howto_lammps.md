# Basic LAMMPS installation 

> WARNING: this guide refers to version Mar2020 of LAMMPS. It might be outdated

## LAMMPS building: notes and reminders

How I built LAMMPS with `CMake`:
```bash
cd lammps               
mkdir build; cd build    # create and use a build directory

# configuration of the CMake: no building is done in this phase
cmake -D PKG_NAMEPKG=yes ../cmake          
cmake --build .          # compilation (or type "make")
```
Add as many as packages as you want. Note that when building pacakges such as USER-MISC the syntax is `-D PKG_USER-MISC=yes`.

Important thing to know:
+ The `README.md` in the `cmake` directory in lammps is helpful
+ One can build LAMMPS from the same source code as many times as he/she wants. The building directory and the source one are separated things

## Examples:
### Build16Nov20
+ serial type of lmp
+ Command used for configuring CMake:
  ```bash
  cmake -D PKG_KSPACE=yes -D PKG_MOLECULE=yes -D PKG_USER-MISC=yes ../cmake
  ```
+ Packages: MOLECULE, KSPACE, USER-MISC
+ An `output_cmake.out` file with all details of the CMake configuration is stored in the build directory. This file tell us which packages, compilers, programs etc. were found by CMake
+ Executable: `lmp`


## How to use it
Other than use the `lmp_intel` in the build directory, one has to use a specific syntaxis in order to use styles and fixes of the INTEL package.

Two options:
1. when calling the `lmp_intel` executable one has to add the option `-sf intel` for example
```bash
/path/to/lmp_intel -sf intel -in input.lammps
```
2. or modify the input script adding at the top of the script: `package intel 1`

The first option is more flexible because one has to modify only the bash script which call the LAMMPS executable and all the other scripts remain unchanged.
