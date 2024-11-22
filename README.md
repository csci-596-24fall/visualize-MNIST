# README

## setup
Prerequisite:
- Python >= 3.3
- pip

1. create a virtual env (venv)
```sh
cd <PROJECT_ROOT>
python3 -m venv .venv
```

2. [activate venv](https://docs.python.org/3/library/venv.html#how-venvs-work)
```sh
# in project root
source .venv/bin/activate
```

3. install dependency
```sh
pip install -r ./requirements.txt
```

## run
### Method 1: by script
```sh
cd <PROJECT_ROOT>
./script/run.sh
```

### Method 2: manually
```sh
cd <PROJECT_ROOT>

# activate venv
source .venv/bin/activate

# run main file
python3 src/main.py
```


## train
Open `src/MNIST.ipynb` and run, highly recommend using Google Colab.
