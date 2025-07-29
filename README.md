# CHILI GraFx Documentation

Welcome to the CHILI GraFx Documentation! This project is designed to assist developers and designers new to CHILI GraFx and its applications.

## Getting Started with Contributing

We welcome contributions from the community! To get started, please familiarize yourself with our contribution guidelines by reading the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Setting Up the Documentation Environment

The CHILI GraFx documentation is built using [MkDocs](https://www.mkdocs.org/), a static site generator that's geared towards project documentation. 

If you are looking to just make a small change, such as editing a single page, you probably don't need to set up a documentation environment. Please see [CONTRIBUTING.md](CONTRIBUTING.md).

However, if you are going to be making many changes you will need to setup a documentation environment. You can set up your documentation environment using one of the following methods:

### Option 1: Using Docker with Codespaces

For a quick and easy setup, you can use Docker in conjunction with [GitHub Codespaces](https://github.com/features/codespaces).

**Steps:**

1. **Select a Branch**: Go to the GitHub repository, select a branch, and click on the `Code` button. Then, choose `Codespaces`. You can either continue with an existing Codespace or create a new one for your selected branch.

2. **Create and Access Codespace**: Click on "Create codespace on [branch name]". This will set up a new Codespace and open an online version of VSCode in a new tab.

3. **Terminal Operations**: In the VSCode terminal, wait for the Python installation to complete, or switch to `Bash` for immediate access.

4. **Start Documentation Server**: Type `docker-compose up` in the terminal. The server initialization might take a short while. Once ready, a notification will allow you to open the documentation site in a new tab.

### Option 2: Using Docker Locally

If you have [Docker Desktop](https://docs.docker.com/desktop/) (for Windows, Mac, or Linux) or [Docker](https://docs.docker.com/engine/) and [Docker-Compose](https://docs.docker.com/compose/) (for Linux) installed on your machine, setting up the documentation locally is straightforward.

**Steps:**

1. **Ensure Docker is Running**: For Mac and Windows, Docker can be managed via the GUI. On Linux, use `sudo systemctl start docker`.

2. **Launch the Server**: Navigate to the documentation project folder in the terminal and execute `sudo docker-compose up`. The documentation site will be hosted locally on `http://localhost:8000`.

### Option 3: Using Python Locally

If you prefer not to use Docker, you can set up the environment with Python.

**Prerequisites:**

Ensure that the latest version of Python 3 is installed on your system. You can download it from [Python's official site](https://www.python.org/downloads/).

**Steps:**
1. **Go To Project Folder**: Navigate to the documentation project folder in your terminal.

2. **Install Requirements**: Run `pip install -r requirements.txt` to install all necessary dependencies.

3. **Start the Server**: Launch the local development server by executing `mkdocs serve`. Access the documentation site at `http://localhost:8000`.

## Conclusion

Choose the setup that works best for you and start contributing to the CHILI GraFx documentation. Your contributions are valuable to the community and help in making our project more accessible and user-friendly. 

Happy Documenting!