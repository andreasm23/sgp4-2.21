# Assignment A0

## Objectives

This assignment intends to help you setup basic tools that are going to be needed for later assignments in the course. This assignment in not graded and, therefore, not mandatory. **However**, we strongly advise you to take it as seriously as any other assignment because it will lay the foundations for you to solve other assignments. In other words, if you will have to solve this assignment anyway later on, in one form or another.

It is also the prefect way for you to get acquainted with git, gitlab, the submission process and the general idea about solving the later assignments. You will be given general feedback on the lectures, and you will have the opportunity to ask questions to solve difficulties that you encountered now.

## Tasks

### 1. Pick a satellite

Go to [celestrak](https://celestrak.org/satcat/search.php) and pick an Earth-orbiting objects of your choice under the following conditions:

- the last 3 digits of the NORAD Id must be the same as your student number
- the satellite must be active

If there are no satellites that meet this criteria, please post a request in Brightspace to have a NORAD Id assigned to you.


### 2. Retrieve the orbital elements 

Retrieve the TLE, which should look something like this:

```
DELFI-N3XT              
1 39428U 13066N   22278.36746881  .00006067  00000+0  92841-3 0  9991
2 39428  97.8159 208.0372 0114906 286.7293  72.1329 14.69680532474673
```

Feel free to use CLI tools to retrieve this data programmatically.


### 3. Implement the SGP4 propagator

There are several implementations of the SGP4 orbit propagator:

- [Python](https://pypi.org/project/sgp4/)
- [Matlab](https://www.mathworks.com/matlabcentral/fileexchange/62013-sgp4)
- [C, C++, C#, FORTRAN 90, Java, JavaScript, LibreOffice Basic, Matlab/Octave, Python 2/3, R, Ruby, Rust, Swift from GitHub user *aholinch*](https://github.com/aholinch/sgp4)
- [C++, C#, Excel, FORTRAN, Java, MATLAB and Pascal from Vallado et al. (2006)](http://celestrak.org/publications/AIAA/2006-6753/)

Download/clone one SGP4 implementation, not necessarily from the choices above. Generally, the implementations of the SGP4 are in the form of a library, which means you will have to implement a program that:

- reads one file with TLE data
- generate a time domain, from specified start, stop and time step
- integrates the orbit over this time domain (i.e., call the relevant routine in the SGP4 library)
- write the time series of position and velocity to an output file

For this to happen, you need to tell your program 5 parameters:

- input TLE data file
- start time
- time steo
- end time
- output orbit data file

**One option** to tell this information to your program is to use input arguments, for example:

```
mysgp4.exe TLE.dat 0 1 1000 orbit.dat
```

... where `TLE.dat` is a file with TLE data in the current directory, the time span is from `0` to `1000` minutes with `1` minute step, and the resulting time series is written to `orbit.dat`. All programming languages have fairly obvious argument parsing capabilities. 


**Another option** is to define all these parameters in a configuration file, e.g. called `sgp4.config` which contains (e.g.):

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
 
You'll only have to parse one input argument (the name of the input config file), but you'll have to parse the contents of this file to retrieve the relevant information.

**Finally**, a more advanced method is to read the TLE data from the `sdtin`, define the time span through input arguments and write the orbit data to `stdout`:

```
cat TLE.dat | mysgp4.exe 0 1 1000 > orbit.dat
```

As with parsing input arguments, reading/writing to `stdin`/`stdout` is well supported, generally this is accomplished by opening a "file" with a specific name (or file unit, in some languages), and reading/writing from/into it.

### 4. Generate an orbit

Use the SGP4 propagator to generate position and velocity of your satellite for at least three orbital revolutions. You may pick the start/stop time and the time step, but be aware you will have to motivated your choice in the answe sheet.

### 5. Plot your orbit

Represent the orbit data you generated above in a plot, with the x-axis showing time and the y-axis showing the value of the orbital positions along each coordinate axis. Plot all 3 coordinate components in the same plot.

There are multiple choices for plotting data:

- [matplotlib](https://matplotlib.org) for python
- the [plot](https://www.mathworks.com/help/matlab/ref/plot.html) command in matlab
- the excellent [gnuplot](http://www.gnuplot.info) program, made easy to use with wrappers like [plot-files.sh](https://github.com/jgte/plot-files)
- excel

Generally, the following steps are required to plot ASCII data:

- load the data from a file
- call the correct plotting function
- save the plot in a file, preferably `png`

In case of python's `matplotlib` or matlab's `plot`, you'll have to code these steps yourself. In case of excel, these steps involve some clicking and it is difficult to automate, imagine plotting data from dozens of files (using macros may make this batch task more practical).
