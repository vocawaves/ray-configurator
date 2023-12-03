rmdir /s /q __pycache__ build dist
python version.py
pyinstaller "ray-configurator.spec"