#!/bin/bash

set -e

sudo mkdir -p /usr/local/bin	
sudo ln -s $(readlink -f void.py) /usr/local/bin/void