# Assignment A0

[[TOC]]

## Rules

This document contains the assignment text. We provide the [answer sheet](answer-sheet.md), where you fill-in the answers to the [tasks](#tasks) listed below. We call *report* to the edited answer sheet, after you fill-in your answers. Any modification to the assignment text (this file), will be ignored.

### What do you need to submit

In addition to your report, you must submit all code and data that you used to find the answers to the assignment. This is important because:

- it legitimises your answers (we will check if your code really provides the answers you gave) and
- allows us to evaluate the approach you have taken.

### Assessment

You will be given points for your correct answers; wrong answers receive a fraction of the total points or none. Each task has a pre-defined set of points, reported below. 

**Please note**:

- all answers must be given. If your answer sheet is not complete, you automatically fail.
- your report is individual, which means:
  - you must use your code to find the answers you provide in the answer sheet, and
  - the code you submit must be of your authorship.
- we encourage you to cooperate with your colleagues at the **conceptual** level, so that you are safely within the requirements for an individual report mentioned above.

Referring to the [rubrics](https://brightspace.tudelft.nl/d2l/le/content/498874/viewContent/2663586/View), the grade is split according to:

- 20% Clarity
- 40% Approach
- 40% Content



### Types of answers

You can expect to provide the following types of answers:

- **numeric**, which are assessed by numeric comparison with our own solution, and fall in *Approach* item of the rubrics;
- **plots**, which are assessed visually, and fall in *Clarity* and *Approach* items of the rubrics
- **open text**, related to answering questions on observations, interpretations and conclusions, generally from plot(s), which are assessed according to the *Content* and *Clarity* items of the rubrics.

An additional type of "answer" is the code you submit. It is assessed according to the *Approach* rubric item.

The table below illustrates how each type of "answer" relates to the rubrics items.

| Answer type   | Clarity | Approach | Content | Total |
| ---           | ---     | ---      | ---     | ---   |  
| all           | 20%     | 40%      | 40%     |       |  
| numeric       |         | 1/2      |         | 20%   |
| plots         |  1/2    | 1/4      |         | 20%   |
| open text     |  1/2    |          | 1       | 50%   |
| code          |         | 1/4      |         | 10%   |

### Excellence

If you address all assignments tasks correctly, your final grade is 8. To get a higher grade, you have several opportunities to show excellence. There are two types of Excellence:

- Assignment excellence, which is indicated in the assignment text, and
- [Coding excellence](#codingexcellence)

There is no specific formula for how much each excellence item is worth, because there are simply too many. Each one will be assessed individually.

We want to reward your efforts by being relatively liberal when grading Excellence. For example, you should get a 10 if your report is completely correct and you successfully address:

-  all Assignment Excellence items,
-  all Coding Excellence items, or
-  a comprehensive mix of Coding and Assignment excellence.

#### Coding excellence

In addition to opportunities for excellence specific to this assignment, there are the following (non-exhaustive list of) coding opportunities for excellence:

- improved execution efficiency,
- elements of automation,
- non-obvious, creative and/or innovative algorithmics, and
- unit testing. 

You must report the opportunities for Excellence that you have addressed in your answer sheet in order for them to be assessed.


## Objectives

This assignment intends to help you setup basic tools that are going to be needed for later assignments in the course. Although we will grade this assignment, it will not be relevant to your final course grade. This assignment is, therefore, not mandatory. 

**However**, we strongly advise you to take it as seriously as any other assignment because it will lay the foundations for you to solve other assignments. In other words, if you will have to solve this assignment anyway later on, in one form or another.

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

**Opportunity for Excellence**: use CLI tools to retrieve this data programmatically.


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
- write the time series of position and velocity to an output file.

For this to happen, you need to tell your program 5 parameters:

- input TLE data file
- start time
- time step
- end time
- output orbit data file

**Opportunity for Excellence**: the TLE data file can come in several formats, namely `KVN`, `XML`, `JSON` and `CSV`. Implement (at least) one additional format that your program can read. You may use libraries for parsing these formats, e.g. Python's `json` package.

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
 
You'll only have to parse one input argument (the name of the input config file), but you'll have to parse the contents of this file to retrieve the relevant information.

**3: Use `stdin` combined with input arguments**. This is a more advanced method, where the TLE data is read from the `sdtin`, and the time span is defined through input arguments. A natural way to handle the output (which was saved in `orbit.dat` in previous options) is to write it to `stdout` (the screen). It is then possible to [redirect](https://medium.com/hacker-toolbelt/bash-shell-redirecting-standard-input-and-output-8c4713a22ea5) the output of `stdout` to a file, using the '>' operator:

```
cat TLE.dat | mysgp4.exe 0 1 1000 > orbit.dat
```

As with parsing input arguments, reading/writing to `stdin`/`stdout` is well supported, generally this is accomplished by opening a "file" with a specific name (or file unit, in some languages), and reading/writing from/into it.

**Opportunity for Excellence**: implement 2 of the above methods to communicate the parameters with your SGP4 propagator.

### 4. Generate an orbit

Use the SGP4 propagator to generate position and velocity of your satellite for at least three orbital revolutions. You may pick the start/stop time and the time step, but be aware you will have to motivated your choice in the answer sheet.

### 5. Plot your orbit

Represent the orbit data you generated above in a plot, with the x-axis showing time and the y-axis showing the value of the orbital positions along each coordinate axis. Plot all 3 coordinate components in the same plot.

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

**Opportunity for Excellence**: Automate the whole workflow, i.e., by calling one single command 1) download the TLE associated with the specified NORAD Id, 2) compute the orbit associated with the specified time start, step and stop, and 3) plot the orbit. This does not exclude you from implementing a solution for the individual steps, because you need to report those steps separately in the answer sheet.

### 6. Final remarks

Don't forget to:

- report Assignment and Code Excellence
- report the time it took you to solve the assignment
- provide feedback on the assignment, namely how interesting you found it and how challenging it was to answer it.
