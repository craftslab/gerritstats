#!/bin/bash

if [ "$1" = "all" ]; then
  list="$(find tests/* -maxdepth 0 -type d | grep -v __pycache__)"
else
  list="tests/cmd tests/logger"
fi

coverage run --source=gerritstats,tests -m pytest -v --capture=no $list
