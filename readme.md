# README for pycronjob

## Overview
You have some PROJECT which does TASK for REASONS. You want it to run automatically.

This is a template for doing that.

A virtualenv is created so that you run with a stable isolated set of libraries.

## Usage
### Prerequisites
Redhat-based packages:
```
$ sudo dnf install python3 python3-pip ansible
```

Debian-based packages:
```
$ sudo apt update && sudo apt upgrade
$ sudo apt install python3 python3-pip ansible
```


### Deployment
Deploy:
```
$ ansible-playbook -vv install_pycronjob.pb.yml
```

### Un-deployment
Erase:
```
$ ansible-playbook -vv uninstall_pycronjob.pb.yml
```


### Using pycronjob with your scripts
* Put your python project in `deploy/`
* Write a shim script at `deploy/cronjob_main.py` to act as an entrypoint for automated running.
* Put any python packages required in `deploy/requirements.txt`

* If you have secrets, add them to a gitignored file.