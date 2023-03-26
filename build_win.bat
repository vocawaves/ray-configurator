rmdir /s /q __pycache__ build dist
del *.spec

pyinstaller --noconfirm --noconsole --onefile --clean --name "ray-configurator" "./ray_configurator/gui.py"