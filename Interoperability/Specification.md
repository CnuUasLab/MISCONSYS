# Interoperability

# Introduction

The Interoperability section is meant to be set up between different sections. The two main sections are the main class and the mission class.
We need to create others as well that are described in the specification. The Interoperability server's main purpose is
to control communication between the ground station and the competition server. There are several design specifications that
need to be taken care of.

# Use of Daemons

Python does have a multi-threading class. However, the multi-threader in python does not accomplish what it set out to accomplish
which is parallel processing of different tasks in the main computation of the program. There is simultaneous processing. However,
it isn't done in parallel. The reason why this is a problem is because the competition clearly states that there should be 
a minimum frequency that we post telemetry at. If we have a dedicated process, then this becomes simpler.

Daemons are how we can solve this issue. The main idea behind doing this is that we create a separate background process in
and of itself. By keeping track of the main process, we can control whether it's running or not, and make sure that it's not running on it's own.

# Design

This is the general design specification that is occuring in this program. There are a few things happening behind the scene that are not shown in the picture.

![alt text](https://github.com/CnuUasLab/MISCONSYS/blob/david.patch.spec/Interoperability/img/interop.jpg "Suggested Interop")

The image details connections between the main process, and other external programs. These main processes are serviced information
through an http server, were we serve nothing but a json object over an http server held on the central workstation. Since most
of this is happening over one system, a lot of the interoperability stuff will not need to be serviced outside the workstation
doing the processing.

Because of this there are a few tasks that are specfic to the system design.

Task | Description
--- | ---
main.py | Program that has a specific function of starting up all processes and serving information that is recieved through these processes.
mission.py | Program that interfaces with the competition server, and spawns a daemon that posts telemetry to the competition server
FELC.js | This is just a resemblence for the front end. All of the front end's information will be gained from the http server.
mav.py | This is a mavlink section of the code. It grabs information from the Plane, and it allows us to update telemetry.
config.json | This is a placeholder for all of the configuration stuff in the program.
Utils.py | Simple utility function that we can use to log information as we go along.

A lot of the code examples can be found in the POKEMON repository in the CnuUasLab to use as an example for this year's code.

# Interface

<b> main </b>
```python



```
