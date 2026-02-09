#!/bin/bash

echo "Activating virtual environment"
source venv/Scripts/activate

echo "Executing the test suite"
python -m pytest
echo $?
exit $?