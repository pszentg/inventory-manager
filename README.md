# Inventory manager

## Setup
Run `source install.sh` from the project root. It will set up the virtual environment and install the required dependencies. If you want to run either the project or the tests, don't forget to export the root directory in your python path: `export PYTHONPATH=$PYTHONPATH:$(pwd)` and activate the virtual environment: `source .venv/bin/activate`

## Run
You can run the project using `python main.py -i <your_instructions_file> -v <arm_version>`. The parser looks for the file in the `/resources` folder, if it doesn't find it, it will  try to parse the parameter as an absolute path. Arm version is an integer, it indicates which version of the arm to use.

### Run the tests
You can run the tests from the project root with the following command: `python -m unittest discover -s tests`. This will discover the tests in the `tests/` directory.

## Input restrictions
You can find an example input set in `resources/instruction_set_01.txt`. Your initial stack state allows for labels that are only 1 character long and contains only alphabets.

## Contribution
If you want to contribute to this project, run `pre-commit install` in the project root. It will initialize pre-commit with a basic config that will run before every commit.

## Further improvements
* Dockerize
* Allow non-alphabetical labeling for the boxes
* Set up Github Actions to run tests and pre-commit on PRs
