#!/bin/bash

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

echo "--- starting"

venv_dir=$(realpath "$(dirname "$0")/python-dev-env/")

echo lol c est venv dire: ${venv_dir} et "$(dirname "$0")"
# Check if virtual environment directory exists
if [ -d "$venv_dir/bin" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    echo "Creating virtual environment..."
    # Attempt to create a virtual environment
    if ! python3 -m venv "$venv_dir"; then
        echo "Failed to create virtual environment. Exiting."
        exit 1
    fi
fi

echo "Virtual environment is ready."

# Activate the virtual environment
source "${venv_dir}bin/activate"

# Check if the correct Python is being used
REL_EXPECTED_PYTHON="${venv_dir}bin/python"
EXPECTED_PYTHON=$(realpath "$REL_EXPECTED_PYTHON")
CURRENT_PYTHON=$(which python)

if [ "$CURRENT_PYTHON" != "$EXPECTED_PYTHON" ]; then
    echo "ERROR: The Python executable in use ($CURRENT_PYTHON) does not match the expected path ($EXPECTED_PYTHON). Please activate the virtual environment before running this script."
    exit 1
fi

# Ensure pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip could not be found. Please ensure pip is installed."
    exit 1
fi

# Reading package names from requirements.txt
REQUIREMENTS_FILE="$(dirname "$0")/requirements.txt"
echo $REQUIREMENTS_FILE

if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "requirements.txt file not found. Exiting."
    exit 1
fi



# Updating pip
pip install --upgrade pip

# Get a list of installed packages
INSTALLED_PACKAGES=$(pip list --format=freeze)

# Install packages from requirements.txt
while IFS= read -r PACKAGE || [[ -n "$PACKAGE" ]]; do
    if echo "$INSTALLED_PACKAGES" | grep -q "^$PACKAGE=="; then
        echo "$PACKAGE is already installed."
    else
        echo "$PACKAGE is not installed. Installing..."
        pip install "$PACKAGE"
    fi
done < "$REQUIREMENTS_FILE"

echo "--- starting jupyter lab"
jupyter lab --NotebookApp.max_mem_rate=0.3 --NotebookApp.token='dev' --notebook-dir="$(dirname "$0")/.."
