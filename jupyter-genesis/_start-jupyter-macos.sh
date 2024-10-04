# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

echo "--- starting "

venv_dir="$(dirname "$0")/python-dev-env/"  # set the name of the virtual environment directory

if [ -d "$venv_dir/bin/" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    echo "Creating virtual environment..."
    if ! python3 -m venv "$venv_dir"; then
        echo "Failed to create virtual environment. Exiting."
        exit 1
    fi
fi

echo "Virtual environment is ready."

source "$(dirname "$0")/python-dev-env/bin/activate"

EXPECTED_PYTHON="$(dirname "$0")/python-dev-env/bin/python"
CURRENT_PYTHON=$(which python)

if [ "$CURRENT_PYTHON" != "$EXPECTED_PYTHON" ]; then
    echo "ERROR: The Python executable in use ($CURRENT_PYTHON) does not match the expected path ($EXPECTED_PYTHON). Please activate the virtual environment before running this script."
    exit 1
fi 

# If the script reaches this point, it can assume that the correct virtual environment is active and proceed with its operations.

# Reading package names from requirements.txt
REQ_FILE="$(dirname "$0")/requirements.txt"

if [ ! -f "$REQ_FILE" ]; then
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
        echo ''
        echo ''
        echo ''
    else
        echo "$PACKAGE is not installed. Installing..."
        pip install "$PACKAGE"
        echo ''
        echo ''
        echo ''
    fi
done < "$REQ_FILE"

echo "--- starting jupyter lab"
jupyter lab --NotebookApp.iopub_data_rate_limit=1e10 --NotebookApp.token='dev' --notebook-dir="$(dirname "$0")/.."
