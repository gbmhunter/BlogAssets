# Exit immediately if any command returns non-zero exit code
set -e

# Install cmake_example project
pip install .

# Run test script which uses cmake_example
python test/main.py