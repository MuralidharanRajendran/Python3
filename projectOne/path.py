from pathlib import Path

path = Path()
# To find files Eg. Excel, py file etc the below can be used
for files in path.glob('*.py'):
    print(files)