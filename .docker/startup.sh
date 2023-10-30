#!/bin/bash

pip3 install --upgrade pip
pip3 install --no-cache-dir awscli
pip install pipenv
pipenv install
pipenv run python onoff.py