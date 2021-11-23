A POC using the python api of google cloud to provision networks , firewalls , routers and hosts

## steps to get started

:warning: **Have all the secrets in place before proceeding**
:warning: **Make sure that everything under the below directory tree is under .gitignore to avoid accidentaly publishig sensitive data**

```bash
secrets
├── credentials.example.json
└── ssh-keys
    ├── key.example
    └── public-key.example.json
```

```bash
git clone https://github.com/sr-vishnu/potential-octo-guide.git
cd potential-octo-guide
pipenv shell
pipenv install

python3 ./scripts/provision/main.py
```