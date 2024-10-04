# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

Write-Output "--- starting"

# Define the virtual environment directory relative to this script
$scriptPath = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
$venvDir = Join-Path -Path $scriptPath -ChildPath "python-dev-env"

# Check if the virtual environment already exists
if (Test-Path -Path "$venvDir\Scripts") {
    Write-Output "Virtual environment already exists. Skipping creation."
} else {
    Write-Output "Creating virtual environment..."
    $creationResult = python -m venv $venvDir
    if (-not $?) {
        Write-Output "Failed to create virtual environment. Exiting."
        exit 1
    }
}

Write-Output "Virtual environment is ready."

# Activate the virtual environment
$activateScript = Join-Path -Path $venvDir -ChildPath "Scripts\Activate.ps1"
. $activateScript

# Update pip
pip install --upgrade pip

# Reading package names from requirements.txt
$reqFile = Join-Path -Path $scriptPath -ChildPath "requirements.txt"

if (-not (Test-Path -Path $reqFile)) {
    Write-Output "requirements.txt file not found. Exiting."
    exit 1
}

# Get a list of installed packages
$installedPackages = pip list --format=freeze

# Install packages from requirements.txt
Get-Content $reqFile | ForEach-Object {
    $package = $_
    if ($installedPackages -match "^$package==") {
        Write-Output "$package is already installed."
    } else {
        Write-Output "$package is not installed. Installing..."
        pip install $package
    }
}

Write-Output "--- starting jupyter lab"
jupyter lab --NotebookApp.max_mem_rate=0.3 --NotebookApp.token='dev' --notebook-dir=$scriptPath
