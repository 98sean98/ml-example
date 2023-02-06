#!/bin/bash

zip -r Archive.zip . -x '*.venv*' -x '*.git*' -x '*__pycache__*' -x '*.DS_Store*'
