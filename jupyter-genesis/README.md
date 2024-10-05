# JupyterGenesis

Your quickest route to launching a fully-prepared Jupyter environment for Python development. Optimized for simplicity and ease of use, **JupyterGenesis** provides dedicated scripts to set up your Python development environment with Jupyter Lab, tailored for macOS and Windows.

## Supported Operating Systems

- **macOS** (Bash)
- **Windows** (PowerShell script)

## Prerequisites

Before you begin, ensure you have Python 3.6 or later installed on your system. Python needs to be added to your system's PATH to ensure the scripts can invoke the Python interpreter.

- For **Windows**, Python can be installed from the [official website](https://www.python.org) or via package managers like [Chocolatey](https://chocolatey.org).
- **macOS** users can install Python using their respective package managers (such as [Homebrew](https://brew.sh) for macOS), or by downloading it from the [Python website](https://www.python.org) .

## Installation

1. **Clone the Repository**

   First, clone the **JupyterGenesis** repository to your local machine using Git:

   ```sh
   git clone https://github.com/MaloLM/JupyterGenesis
   cd JupyterGenesis
   ```

2. **Prepare the Script**

   - **macOS**: Make the script executable. For macOS users, navigate to the cloned directory and run:

     ```sh
     chmod +x _start-jupyter-macos.sh
     ```

   - **Windows**: Ensure that your system's execution policy allows running scripts. Open PowerShell as Administrator and run:

     ```powershell
     Set-ExecutionPolicy RemoteSigned
     ```

     Note: You can revert this change after running the setup script with `Set-ExecutionPolicy Restricted`.

3. **Run the Script**

   Execute the dedicated script for your OS.

   - **macOS**:

     ```sh
     ./_start-jupyter-macos.sh
     ```

     Or simply double click the script.

   - **Windows**:

     ```powershell
     .\_start-jupyter-windows.ps1
     ```

     Or simply double click the script.

> **Caution:**

- Ensure that requirements.txt file is at the same directory than the script.
- Ensure that requirements.txt file contains at least the `jupyterlab` package, else it could not work properly.

## Usage

The setup scripts prepare a Python virtual environment, install all required packages (in requirements.txt), including Jupyter Lab and finally start the jupyterlab server. If you wish to use the virtual environment without starting the Jupyter server, you can activate the environment manually (after one script execution):

- **macOS**:

  Open a terminal and navigate to the project directory. Activate the virtual environment by running:

  ```sh
  source python-dev-env/bin/activate
  ```

- **Windows**:

  Open PowerShell and navigate to the project directory. Activate the virtual environment by running:

  ```powershell
  .\python-dev-env\Scripts\Activate.ps1
  ```

To deactivate the virtual environment and return to your system's global Python environment, you can simply run the command `deactivate` in your terminal (macOS) or PowerShell (Windows).

## Customizing Script Icons

For those who wish to personalize the script icons to either a Python or Jupyter logo, detailed instructions are available to guide you through the process on macOS and Windows.

Please refer to the [Custom Icon Guide](/docs/CUSTOM_ICON.md) for step-by-step instructions on how to customize your script icons using the assets provided in the `/icons` directory of this repository.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.
