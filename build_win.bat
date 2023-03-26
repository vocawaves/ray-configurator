rmdir /s /q __pycache__ build dist
del *.spec

pyinstaller --noconfirm --noconsole --onefile --clean --collect-data sv_ttk --name "ray-configurator" "./ray_configurator/gui.py"