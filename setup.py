
#!/usr/bin/env python

from setuptools import setup

setup(name='tenc',
      version='1.0',
      description='A small package to de- and encrypt strings',
      author='Philip Stapelfeldt',
      author_email='me@ph1p.dev',
      packages=['tenc'],
      entry_points={
              'console_scripts': [
                  'tenc = tenc.cli:main',
              ],
      },
      )
