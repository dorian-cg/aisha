# 🌷 A.I.S.H.A

AI Smart Home Assistant

## Project Requirements

1. [Python 3.12](https://www.python.org/downloads/release/python-31210/)
2. [VS Code](https://code.visualstudio.com/)
3. [Python Extensions for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
4. [Git](https://git-scm.com/downloads)

## Running the project in your PC

### 1. Go to a location in your computer where you want to save (or already saved) the project

```bash
cd C:/Users/MyUser/Desktop
```

### 2. Clone the project repository

This step is not necessary if you have already cloned the repo.

```bash
git clone https://github.com/dorian-cg/aisha
```

### 3. Go into the project folder

```bash
cd aisha
```

### 4. Create Python venv inside the project folder

This step is not necessary if you have already created the venv.

```bash
python -m venv ./venv
```

### 5. Activate Python venv for the project

```bash
./venv/Scripts/Activate.ps1
```

After successfully activating the venv you will noticed there is a green prefix `(venv)` with the name of the project in the terminal.

It looks something like this:

```ps
(venv) PS C:\Users\MyUser\Desktop\aisha>
```

### 6. Install dependencies (external libraries)

After making sure that the venv was activated successfully run this command to install the environment dependencies:

> This step is not needed if you already installed the dependencies before.

```bash
pip install -r requirements.txt
```

### 7. Define `.env` file
There is a `.env.template` at the root of the folder which has placeholder values, create a `.env` file with the same values and replace the placeholders with the actual values needed to connect to your Azure OpenAI model. 
> This step is not needed if you already created the `.env` file before.
```.env
AZ_OPENAI_ENDPOINT=put-your-endpoint-here
AZ_OPENAI_API_VERSION=2024-12-01-preview
AZ_OPENAI_DEPLOYMENT_NAME=gpt-5-nano
AZ_OPENAI_CHAT_COMPLETION_API_KEY=put-your-api-key-here
```

### 8. Execute the service in dev mode

Once the dependencies are available is time to run the service:

```bash
fastapi dev main.py
```
