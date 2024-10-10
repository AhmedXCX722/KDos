# KDos - The Strongest DDoS Tool

KDos is a Python-based Distributed Denial of Service (DDoS) tool designed to stress test networks by sending a large number of UDP packets to a target server using multiple threads. It features a customizable and user-friendly interface, with colored prompts and output.

## Features

- **Multithreading**: Uses 100 threads to maximize the attack intensity.
- **Customizable Inputs**: Users can specify the target IP, port, packet size, and attack duration.
- **Graceful Exit**: The tool handles `Ctrl + C` interrupts and prints a custom message on exit.
- **Colorful UI**: Features ANSI color-coded input prompts and output messages for a more visually appealing interface.

## Requirements

- Python 3.x
- Required libraries (install with `requirements.txt`):
    - `socket`
    - `threading`
    - `random`
    - `signal`
    - `sys`

## Installation

1. Clone or download this repository.
2. Install the required libraries using `pip`:

   ```bash
   pip install -r requirements.txt
