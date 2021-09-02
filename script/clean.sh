#!/bin/bash

chmod 644 .dockerignore .gitignore .travis.yml
chmod 644 LICENSE MANIFEST.in README.md
chmod 644 requirements.txt setup.cfg setup.py stats.py tox.ini

find gerritstats tests -name "*.json" -exec chmod 644 {} \;
find gerritstats tests -name "*.py" -exec chmod 644 {} \;
find . -name "*.pyc" ! -path "*.venv*" -exec rm -rf {} \;
find . -name "*.sh" ! -path "*.venv*" -exec chmod 755 {} \;
find . -name "__pycache__" ! -path "*.venv*" -exec rm -rf {} \;
