#!/bin/bash

pip3 install -U pywin32
pip3 install -U pyinstaller
pip3 install -Ur requirements.txt

pyinstaller --clean --name gerritstats --upx-dir /path/to/upx -F stats.py
