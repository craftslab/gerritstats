#!/bin/bash

pip install -U pyinstaller
pip install -U pywin32
pip install -Ur requirements.txt

pyinstaller --clean --name gerritstats --upx-dir /usr/bin -F stats.py
