# Project Template

This Python project template is designed to streamline the setup of new projects with a standard structure under the 
BSD-3 license.

## Structure

- `data/`: Data files like JSON.
- `examples/`: Example scripts and additional documentation.
- `tests/`: Unit tests for the project modules.
- `scripts/`: Entry point scripts for running the application.
- `src/`: Source code of the project.
- `LICENSE`: The BSD-3 license file.
- `pyproject.toml`: Project metadata and dependencies managed by Poetry.
- `README.md`: Information about the project and setup instructions.
- `.idea/`: Contains a PyCharm configuration file misc.xml that enables black.

## Installation

### Requirements

- Python 3.8 or higher
- Poetry for dependency management
- Black for code formatting
- Pytest as testing environment

### Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/project_template.git
cd project_template
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # On Unix/macOS
venv\Scripts\activate  # On Windows

# Install dependencies
poetry install
or 
pip install -e . 

# for linux version <=3.8, you should first update pip to deal with -e option
pip install --upgrade pip 
```

### Code Formatting

Format your code automatically using:
```bash
black .
```

If you use PyCharm, there is already a configuration file in .idea/misc.xlm that enables black if your IDE. 

### Usage

Run the main application:

```bash
python -m scripts.main_template
```

### Testing

Execute tests using:

```bash
pytest tests/test_template.py
```

### Contributing

Contributions to this project are welcome. Please ensure that all contributions adhere to the BSD-3 License guidelines.
License

This project is licensed under the BSD-3 License - see the LICENSE file for details.
