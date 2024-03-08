#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
#
apt update 
apt upgrade
# Install MySQL server
apt update
apt install mysql-server

# Install python3-venv if not already installed
apt install python3-venv

# Set up virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install MySQL connector for Python
pip install mysql-connector-python

# Use pipx
pipx install mysql-connector-python
