# This script is only used to turn the main.py script into a windows executable, by running "python setup.py build"

from cx_Freeze import setup, Executable

files = []

target = Executable(
    script="main.py",
    base="Win32GUI"
)
setup(
    name="202020",
    version="1.0",
    author="ZiyadCodes, https://ziyadcodes.000webhostapp.com",
    executables=[target],
    options={'build.exe': {'include_files': files}},
    description="202020"
)
