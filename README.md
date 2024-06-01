

# Installation

* Install pyenv or [pyenv-win](https://github.com/pyenv-win/pyenv-win) (Windows). 
```bash
pyenv update
pyenv install 3.12.3
pyenv local 3.12.3
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
# Add 'C:\Users\<username>\AppData\Roaming\Python\Scripts' to PATH variable
poetry --version
poetry env use 3.12.3
poetry install
```

