# This script is only used to turn the main.py script into a windows executable, by running `python setup.py build`

from cx_Freeze import setup, Executable
import pkgutil

files = ["StopApp.bat", "RunOnStartup.bat", "DontRunOnStartup.bat", "Resources"]
includes = ["encodings", "collections", "importlib", "pygame", "win32com", "os", "time"]
excludes = [i.name for i in list(pkgutil.iter_modules()) if i.ispkg and i.name not in includes]

target = Executable(
    target_name="TwentyTwentyTwenty.exe",
    script="main.py",
    base="Win32GUI"
)
setup(
    name="20-20-20",
    version="1.0",
    author="ZiyadCodes, https://ziyadcodes.000webhostapp.com",
    executables=[target],
    options={"build_exe": {"include_files": files, "excludes": excludes, "optimize": 1}},  # Try optimize 2 first
    description="20-20-20"
)
