rmdir /s /q __pycache__ build dist rayversion.txt
python version.py
pyinstaller --noconfirm --noconsole --onefile --clean --version-file="./rayversion.txt" --name "ray-configurator" "./ray_configurator/gui.py"