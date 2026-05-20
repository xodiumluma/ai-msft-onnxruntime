#!/bin/bash
# Find out the absolute path of this directory
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OS=$(uname -s)
if [ "$OS" = "Darwin" ]; then
	DIR_OS="MacOS"
else
	DIR_OS="Linux"
fi

if [[ "$*" == *"--ios"* ]]; then
	DIR_OS="iOS"
elif [[ "$*" == *"--android"* ]]; then
	DIR_OS="Android"
fi
python3 "$DIR"/tools/ci_build/build.py --build_dir "$DIR"/build/$DIR_OS "$@"
