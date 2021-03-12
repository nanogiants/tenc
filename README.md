# (t)iny (enc)ryption

Simple en- and decryption script
You have to run `pip3 install -U PyCryptodome coverage` first.

## How to use

usage: main.py [-h] -f PATH -p PASSWORD [-d]

Encrypt and decrypt files

optional arguments:
-h, --help show this help message and exit
-f PATH path to file
-p PASSWORD password
-d should decrypt otherwise encrypt

### Examples:

tenc -p 5a04ec902686fb05a6b7a338b6e07760 -f ./test.json
tenc -p 5a04ec902686fb05a6b7a338b6e07760 -f ./test.json.enc -d

### Tests

```bash
python3 -m unittest discover
coverage run -m unittest discover && coverage report && coverage html
```

### Publish

```bash
python3 setup.py sdist bdist_wheel
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

python3 setup.py develop
python setup.py develop --uninstall
```

### Docs

```bash
# docs
sphinx-apidoc -o source/ ../tenc
cd docs
make clean && make html

python -m compileall .
```
