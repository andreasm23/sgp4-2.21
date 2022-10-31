# Introduction

The sections below relate directly to the tasks described in the [assignment text](README.md). In each one, you will find a short statement requesting you to give a short answer. Below that statement there are a few characters, for example `NORAD_CAT_ID`. Replace that string with your answer. 

Please remember:

- Do not edit anything else in this answer sheet.
- Do not use any kind of formatting, e.g. `something`.
- Only report what is asked, do not answer in a sentence:
    - wrong: "I selected NORAD Id 99999"
    - correct: "99999"
- You may use multiple lines to answer, if needed. 

# 1. Pick a satellite

Report the NORAD Id you selected.

NORAD_ID

# 2. Retrieve the orbital elements 

Report the TLE data you retrieved. If you retrieved TLE data in `KVN`, `XML`, `JSON` or `CSV` formats, report it in `TLE` format.

TLE_DATA

# 3. Retrieve the SGP4 propagator

Report the URL or GitHub repository of the SGP4 implementation you will be using.

SGP4_IMPL

Report the command that you use in the CLI to generate the orbit data.

SGP4_COM

# 4. Generate an orbit

Report the start time of your time domain.

ORB_START_T

Report the stop time of your time domain.

ORB_STOP_T

Report the time step in your time domain.

ORB_STEP_T

Report the motivation that led you to choose the values of the parameters above, i.e., start/stop times and time step.

ORB_JUST

Report the first data point, i.e. time, position x, y, z, velocity x, y, z, from the orbit data you generated with the SGP4 propagator.

ORB_FIRST

Report the last data point from the orbit data you generated with the SGP4 propagator.

ORB_LAST

### 5. Plot your orbit

Report the markdown code (see [this link](https://docs.gitlab.com/ee/user/markdown.html#images)) that adds your image to this document.

ORB_PLOT

Make three observations about the data you plotted.

ORB_OBS

Make two interpretations about the observations you reported above.

ORB_INT

Make one conclusions based on the observations and interpretations you reported above.

ORB_CON


### 6. Final remarks

Report the steps you have taken to address Code Excellence. Report "none" if relevant.

EXC_CODE

Report the steps you have taken to address Assignment Excellence. Report "none" if relevant.

- use CLI tools to retrieve this data programmatically:

EXC_ASSIGN_1

- implement parsing additional TLE format(s) in your program:

EXC_ASSIGN_2

- implement multiple methods to communicate the parameters with your SGP4 propagator:

EXC_ASSIGN_3

- automate the whole workflow:

EXC_ASSIGN_4
