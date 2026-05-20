#!/bin/bash
# Find out the absolute path of this directory
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OS=$(uname -s)
if [ "$OS" = "Darwin" ]; then
	DIR_OS="MacOS"
else
	DIR_OS="Linux"
fi
