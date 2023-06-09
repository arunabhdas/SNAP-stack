# SNAP Stack

SNAP stack is a SvelteKit - Node - (fast)API - Postgres- stack toolkit for building, testing and deploying
fullstack CMS, CRM and Mobile SaaS applications

## Screenshots

<img src="https://raw.githubusercontent.com/arunabhdas/FAPS-stack/main/screenshots/screenshot_2_3.png" width="720"/>

<img src="https://raw.githubusercontent.com/arunabhdas/FAPS-stack/main/screenshots/screenshot_1.png" width="720"/>

<img src="https://raw.githubusercontent.com/arunabhdas/FAPS-stack/main/screenshots/screenshot_2.png" width="720"/>

## Steps for blog

```

==> python3 -m venv myvenv

==> source myvenv/bin/activate

pip install fastapi

pip install "uvicorn[standard]"

pip install pydantic

pip install --upgrade pip

==> python --version (should be 3.9 or higher)
Python 3.10.9

==> uvicorn --version
Running uvicorn 0.15.0 with CPython 3.10.9 on Darwin

pip install sqlalchemy

pip install passlib

pip install bcrypt

pip install sqladmin

```


## Run

```
cd SNAP-backend

uvicorn main:app --reload

```

