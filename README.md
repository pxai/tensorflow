
# Start
Activate the project and install dependencies

```shell
source bin/activate
pip install -r requirements.txt
```

# Exit the env
```shell
deactivate
```

# Setting up
Creating a venv

```shell
python3 -m venv project_dir
```

# Add packages
```shell
pip install numpy==1.15.3
```
To see
```shell
pip list
```
Save installed packages in a file
```shell
pip freeze > requirements.txt
```
Reinstall dependencies:
```shell
pip install -r requirements.txt
```

