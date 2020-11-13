# Simple en and decryption script

You have to run `pip3 install -U PyCryptodome coverage` first.

## How to use

usage: main.py [-h] -f PATH -p PASSWORD [-d]

Encrypt and decrypt files

optional arguments:
  -h, --help   show this help message and exit
  -f PATH      path to file
  -p PASSWORD  password
  -d           should decrypt otherwise encrypt

### Examples:

python3 encryption.py -p pa$$w0rd -f ./test.json
python3 encryption.py -p pa$$w0rd -f ./test.json.enc -d



```bash
python3 -m unittest discover
coverage run -m unittest discover && coverage report && coverage html
```


https://www.codementor.io/@ajayagrawal295/how-to-publish-your-own-python-package-12tbhi20tf

```
python3 setup.py sdist bdist_wheel
python3 setup.py develop
python setup.py develop --uninstall
```