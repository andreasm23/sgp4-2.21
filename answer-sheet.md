# Introduction

The sections below related directly to the tasks described in the [assignment text](README.md). In each one, you will find a short statement requesting you to give a short answer. Below that statement, there are the characters `<...>`, where you are expected to give your answer. There are two ways to report your answer:

- Single line:

SOME_NAME=<...>

- Multiple line, or a figure:

SOMETHING_START

<...>

SOMETHING_END

In both cases, you only need to replace `<...>` with your answer. Please do not edit anything else in this answer sheel, only replace `<...>` with your answer.

# 1. Pick a satellite

Report the NORAD Id you selected.

NORAD_CAT_ID=<...>

# 2. Retrieve the orbital elements 

Report the TLE data you retrieved.

TLE_BEGIN

<...>

TLE_END

Report the terminal command you used to retrieve the TLE data above. If you downloaded it manually, answer "manually".

TLE_DOWNLOAD_CMD=<...>

# 3. Retrieve the SGP4 propagator

Report the URL or GitHub repository of the SGP4 implementation you will be using.

SGP4_IMPL=<...>

Report the command that you use in the CLI to generate the orbit data.

SGP4_COM=<...>

# 4. Generate an orbit

Report the start time of your time domain.

ORB_START_T=<...>

Report the stop time of your time domain.

ORB_STOP_T=<...>

Report the time step in your time domain.

ORB_STEP_T=<...>

Report the motivation that led you to choose the values of the parameters above, i.e., start/stop times and time step.

ORB_JUST_T_BEGIN

<...>

ORB_JUST_T_END

Report the first data point from the orbit data you generated with the SGP4 propagator.

ORB_FIRST=<...>

Report the last data point from the orbit data you generated with the SGP4 propagator.

ORB_LAST=<...>

### 5. Plot your orbit

Report the markdown code (see [this link](https://docs.gitlab.com/ee/user/markdown.html#images)) that adds your image to this document.

ORB_PLOT_BEGIN

<...>

ORB_PLOT_END

