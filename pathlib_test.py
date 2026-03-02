from pathlib import Path

p = Path("..")
print(p.cwd())

for subdir in p.iterdir():
    if subdir.is_dir():
        print(subdir)

py_files = p.rglob("*.py")

for f in py_files:
    print(f)

sf = p / "users.db"
print(sf)
print("Is absolute? ", sf.is_absolute())
print("Is exist? ", sf.exists())
print("File name: ", sf.name)
print("Extensions: ", sf.suffix)
print("Parent directory: ", sf.parent)


# reading from a file
with (p / "banana.txt").open("w") as f:
    f.write("Welcome to My darkness")

with (p / "banana.txt").open("r") as f:
    print(f.read())
