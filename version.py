import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile(
    output_file="rayversion.txt",
    version="1.0.0",
    company_name="davidcralph",
    file_description="A GUI configurator for ray-mmd",
    internal_name="ray-configurator",
    legal_copyright="© David Ralph.",
    original_filename="ray-configurator.exe",
    product_name="Ray Configurator"
)
