#!/bin/bash

pip install -Ur requirements.txt

rm -rf buid dist gerritstats.egg-info/

python setup.py sdist bdist_wheel
python -m twine upload dist/*
