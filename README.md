# Repository Structure

- `README.md` - repo info and setup isntructions
- `requirements.txt` - python packages for repository
- `tutorials/` - folder containing all tutorials

# Setup

Setup script

1. Make sure to have Python 3.8 installed on your computer
2. Make sure to have the venv package installed with Python3.8  
    - `python3.8 -m pip install virtualenv`

### Initialize a virtual environment
```
python3.8 -m venv .venv
```

If you run `ls -a` in your terminal, you should see a directory `.venv`.

### Setup the virtual environment
```
source .venv/bin/activate
```

```
python3.8 -m pip install -r requirements.txt
```
