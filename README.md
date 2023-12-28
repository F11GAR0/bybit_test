![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/F11GAR0/bybit_test/python-app.yml) ![Static Badge](https://img.shields.io/badge/contributors-1-blue)

## Example to withdraw for Rudolf

#### Config
Create *config.py* and place in this:
```py
BYBIT_API_KEY="Place your api key here"
BYBIT_API_SECRET="Place your api secret here"
```

#### Create virtual environment
Linux / Windows / macOS:
```sh
python -m venv venv
```
#### Activate virual environment
Linux:
```sh
source venv/bin/activate
```
Windows:
```sh
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

#### Install requirements
```sh
pip install -r requirements.txt
```

#### Build docker if need
```sh
docker build --pull --rm -f "Dockerfile" -t bybittest:latest "."
```
#### Run with docker
```sh
docker container run bybittest:latest python /app/main.py
```
#### Run vanila
```sh
python main.py
```
#### Run with docker but using script
```sh
/bin/bash deploynrun.sh
```