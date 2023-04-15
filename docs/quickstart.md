# learn-python Guide

## Installing Python

#### **Windows**
 1. Download python installer for windows from https://python.org/
 2. Install from python installer exe/msi

#### **macOS**
 1. install via [Homebrew](https://brew.sh), run `$ brew install python3`
 2. You can replace `python3` with your version, like `python@3.9`

#### **Linux**

Universal **(source method)**
 1. Download python source release from https://python.org/
 2. Download prerequisites, run `sudo apt -y update && sudo apt -y install git build-essential`
 3. Compile python, run:
     - `./configure`
     - `make`
     - `make install`
 4. Install python, run `altinstall`

**Ubuntu** (Debian)
 1. Update first, run `sudo apt update`
 2. Download the python package, run `sudo apt install python3`

 > Select specfic version of python, run `sudo apt search python`