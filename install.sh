#!/bin/bash

venv_name=".venv"

# create the virtual env
if [ -d "$venv_name" ]; then
    echo "Virtual environment '$venv_name' already exists. Activate it with 'source $venv_name/bin/activate'."
fi

python3 -m venv "$venv_name"
source "$venv_name/bin/activate"
pip install -r requirements.txt

echo "Virtual environment '$venv_name' created and dependencies installed."
