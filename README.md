# 🌷 A.I.S.H.A

AI Smart Home Assistant

## Project Requirements

1. [Python 3.12](https://www.python.org/downloads/release/python-31210/)
2. [VS Code](https://code.visualstudio.com/)
3. [Python Extensions for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
4. [Git](https://git-scm.com/downloads)

## Running the project in your PC

### 1. Go to a location in your computer where you want to save (or already saved) the project

```pwsh
cd C:/Users/MyUser/Desktop
```

### 2. Clone the project repository

This step is not necessary if you have already cloned the repo.

```pwsh
git clone https://github.com/dorian-cg/aisha
```

### 3. Go into the project folder

```pwsh
cd aisha
```

### 4. Create Python venv inside the project folder

This step is not necessary if you have already created the venv.

```pwsh
python -m venv ./venv
```

### 5. Activate Python venv for the project

```pwsh
./venv/Scripts/Activate.ps1
```

After successfully activating the venv you will noticed there is a green prefix `(venv)` with the name of the project in the terminal.

It looks something like this:

```pwsh
(venv) PS C:\Users\MyUser\Desktop\aisha>
```

### 6. Install dependencies (external libraries)

After making sure that the venv was activated successfully run this command to install the environment dependencies:

> This step is not needed if you already installed the dependencies before.

```pwsh
pip install -r requirements.txt
```

### 7. Execute the service in dev mode

Once the dependencies are available is time to run the service:

```pwsh
fastapi dev main.py
```
