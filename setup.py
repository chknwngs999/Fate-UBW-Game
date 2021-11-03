import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Fate UBW Game",
    options={"build_exe": {"packages": ["pygame", "random"],
                           "include_files": ["assets"]}},
    executables=executables
)
