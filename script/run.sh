#!/bin/bash

python3 stats.py \
    --config-file config.json \
    --gerrit-query "since:2020-03-29 until:2020-03-30" \
    --output-file output.json
