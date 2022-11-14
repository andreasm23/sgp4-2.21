# Assignment A0

Please carefully read the [rules](rules/README.md). After reading this document, copy the [answer sheet](answer-sheet.md) to file `report.md` and provide your answers in the latter. Do not edit this document nor the [answer sheet](answer-sheet.md).


## Objectives

This assignment intends to help you setup basic tools that are going to be needed for later assignments in the course. Although we will grade this assignment, it will not be relevant to your final course grade. This assignment is, therefore, not mandatory. 

**However**, we strongly advise you to take it as seriously as any other assignment because it will lay the foundations for you to solve other assignments. In other words, if you will have to solve this assignment anyway later on, in one form or another.

It is also the prefect way for you to get acquainted with git, GitLab, the submission process and the general idea about solving the later assignments. You will be given general feedback on the lectures, and you will have the opportunity to ask questions to solve difficulties that you encountered now.

## Tasks

### 1 Pick a satellite 

Go to [celestrak](https://celestrak.org/satcat/search.php) and pick an Earth-orbiting objects of your choice under the following conditions:

- the last 3 digits of the NORAD Id must be the same as your student number
- the satellite must be active

If there are no satellites that meet this criteria, please post a request in Brightspace to have a NORAD Id assigned to you.


### 2 Retrieve the orbital elements 

Retrieve the TLE, which should look something like this:

```
DELFI-N3XT              
1 39428U 13066N   22278.36746881  .00006067  00000+0  92841-3 0  9991
2 39428  97.8159 208.0372 0114906 286.7293  72.1329 14.69680532474673
```

**Opportunity for Excellence**: use CLI tools to retrieve this data programmatically.


### 3 Implement the SGP4 propagator 

There are several implementations of the SGP4 orbit propagator:

- [Python](https://pypi.org/project/sgp4/)
- [Matlab](https://www.mathworks.com/matlabcentral/fileexchange/62013-sgp4)
- [C, C++, C#, FORTRAN 90, Java, JavaScript, LibreOffice Basic, Matlab/Octave, Python 2/3, R, Ruby, Rust, Swift from GitHub user *aholinch*](https://github.com/aholinch/sgp4)
- [C++, C#, Excel, FORTRAN, Java, MATLAB and Pascal from Vallado et al. (2006)](http://celestrak.org/publications/AIAA/2006-6753/)

Download/clone one SGP4 implementation, not necessarily from the choices above. Generally, the implementations of the SGP4 are in the form of a library, which means you will have to implement a program that:

- reads one file with TLE data
- generate a time domain, from specified start, stop and time step
- integrates the orbit over this time domain (i.e., call the relevant routine in the SGP4 library)
- write the time series of position and velocity to an output file.

For this to happen, you need to tell your program 5 parameters:

- input TLE data file
- start time
- time step
- end time
- output orbit data file

**Opportunity for Excellence**: the TLE data file can come in several formats, namely `KVN`, `XML`, `JSON` and `CSV`, most conveniently retrieved using [Celestrak's API](http://celestrak.org/NORAD/documentation/gp-data-formats.php). Implement (at least) one additional format that your program can read. You may use libraries for parsing these formats, e.g. Python's `json` package.

You have several options to implement passing information to your program:

**1: Use input arguments**, for example:

```
mysgp4.exe TLE.dat 0 1 1000 orbit.dat
```

... where `TLE.dat` is a file with TLE data in the current directory, the time span is from `0` to `1000` minutes with `1` minute step, and the resulting time series is written to `orbit.dat`. All programming languages have fairly obvious argument parsing capabilities. 

**2: Use a configuration file**, e.g. called `sgp4.config` which contains (e.g.):

```
TLE.dat
0
1
1000
orbit.dat
```

... and call your program as:

```
myspg4.exe spg4.config
```
 
You'll only have to parse one input argument (the name of the input configuration file), but you'll have to parse the contents of this file to retrieve the relevant information.

**3: Use `stdin` combined with input arguments**. This is a more advanced method, where the TLE data is read from the `sdtin`, and the time span is defined through input arguments. A natural way to handle the output (which was saved in `orbit.dat` in previous options) is to write it to `stdout` (the screen). It is then possible to [redirect](https://medium.com/hacker-toolbelt/bash-shell-redirecting-standard-input-and-output-8c4713a22ea5) the output of `stdout` to a file, using the '>' operator:

```
cat TLE.dat | mysgp4.exe 0 1 1000 > orbit.dat
```

As with parsing input arguments, reading/writing to `stdin`/`stdout` is well supported, generally this is accomplished by opening a "file" with a specific name (or file unit, in some languages), and reading/writing from/into it.

**Opportunity for Excellence**: implement 2 of the above methods to communicate the parameters with your SGP4 propagator.

### 4 Generate an orbit

Use the SGP4 propagator to generate position and velocity of your satellite for at least three orbital revolutions. You may pick the start/stop time and the time step, but be aware you will have to motivated your choice in the answer sheet.

### 5 Plot your orbit

Represent the orbit data you generated in Task 4 in a plot, with the x-axis showing time and the y-axis showing the value of the orbital positions along each coordinate axis. Plot all 3 coordinate components in the same plot.

There are multiple choices for plotting data:

- [matplotlib](https://matplotlib.org) for python
- the [plot](https://www.mathworks.com/help/matlab/ref/plot.html) command in matlab
- the excellent [gnuplot](http://www.gnuplot.info) program, made easy to use with wrappers like [plot-files.sh](https://github.com/jgte/plot-files)
- excel (not advised because makes automation very difficult)

Generally, the following steps are required to plot ASCII data:

- load the data from a file
- call the correct plotting function
- save the plot in a file, preferably `png`

In case of python's `matplotlib` or matlab's `plot`, you'll have to code these steps yourself. In case of excel, these steps involve some clicking and it is difficult to automate, imagine plotting data from dozens of files (using macros may make this batch task more practical).

**Opportunity for Excellence**: Automate the whole workflow. The purpose is for you to simplify the generation of an orbit and associated plot, so that you only need to call one single command, which would do the following:

1. download the TLE associated with the specified NORAD Id ([Task 2](#2-retrieve-the-orbital-elements)), 
2. compute the orbit associated with the specified time start, step and stop ([Task 4](#4-generate-an-orbit)), and 
3) plot the orbit ([Task 5](#5-Plot-your-orbit)).

In other words, instead of having multiple commands that you need to call in a certain sequence with certain input arguments, there is only one command that is called with all necessary input arguments (you need to figure out which ones). There will be input arguments for the intermediate steps that you do not need to specify, but you must resolve these dependent input arguments internally. For example, the file name with the orbit data is both:

- an output of your SGP4 propagator and
- in input to the plotting task.

If you hard-code the name of this file, consecutive runs with different input arguments will over-write this data, which is generally undesirable. Therefore, the best approach is for you to define yourself dynamic names for this files, which are function of the input arguments, so that you can keep the data. On the same line of thought, the plot file names should also be dynamic, so that you can keep the plots of several runs with different input arguments.

Note that solving the Opportunity for Excellence does not exclude you from implementing a solution for the individual steps, because you need to report those steps separately in the answer sheet.

## Final remarks

Don't forget to:

- report Assignment and Code Excellence
- report the time it took you to solve the assignment
- provide feedback on the assignment, namely how interesting you found it and how challenging it was to answer it.
