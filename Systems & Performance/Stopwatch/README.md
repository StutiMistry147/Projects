# Stopwatch Prototype 
## Overview
- This project involves developing a formal prototype of a StopWatch System using Promela and the SPIN Model Checker. The system is designed as a Synchronous Reactive System, meaning it operates in discrete "macro-steps" or clock ticks.
- The primary challenge of this project was correctly modeling a Synchronous Global Clock to ensure that multiple concurrent processes (Timer, Logic, Display, and Inputs) stay in perfect "lock-step" synchronization within every second .

## Specification 
The StopWatch operates in two primary modes: Stop and Go
- <ins>Go Mode</ins>: Time is continuously measured and displayed in minutes and seconds.
- <ins>Stop Mode</ins>: Time counting is paused; initially, both minutes and seconds are set to zero.

## User Interface And Control
The system features two main control inputs: 
- <ins>Input S (Switch)</ins>: Toggles the operation mode between Stop and Go.
- <ins>Input R (Restart)</ins>: If activated alone, the system enters Stop mode and resets time to zero.
- <ins>Simultaneous S & R</ins>: If both signals are present in the same instant, the system enters Go mode with the time initialized to zero.

## Architecture :
1. <ins>Mode Process</ins>: Determines the operation mode (Go/Stop) by updating object M when signal S is present.
2. <ins>Restart Process</ins>: Monitors signal R to trigger time resets and mode initialization.
3. <ins>CountSecs Process</ins>: Increases the second counter when the system is in Go mode.
4. <ins>CountMinsDisp Process</ins>: Monitors the second counter; when it reaches 60, it resets seconds to zero, increments minutes, and draws the output to the screen.
5. <ins>ClockTick Process</ins>: Acts as the master orchestrator, representing the global synchronous clock and ensuring all processes execute in atomic steps .

## Execution :
1. <ins>Simulation</ins>: Run a random simulation to see the StopWatch responses.
```spin stopwatch.pml```
2. <ins>Exhaustive Verification</ins>: Generate the verifier to check for logic errors.
```
spin -a stopwatch.pml
gcc -o pan pan.c
./pan
```
