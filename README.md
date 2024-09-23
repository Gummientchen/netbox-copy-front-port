# Netbox Copy Front Port

## Install

Create virtual enviroment (>= Python 3.11.5). Run this in the top folder of this repository folder:

```cmd
python -m venv .
```

Activate the virtual enviroment:

```cmd
.\Scripts\activate.ps1
```

Install requirements:

```cmd
pip install -r requirements.txt
```

## Using the script

Create a copy iof the ".env.example" file and name it ".env". Change the TOKEN to your API key from Netbox.

Activate the virtual enviroment:

```cmd
.\Scripts\activate.ps1
```

Run the script:

```cmd
python .\copy-front-port.py
```
