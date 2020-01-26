import glob, os

path = 'target/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.lua' in file:
            files.append(os.path.join(r, file))

for f in files:
    os.system("py __main__.py --input " + f + " --output " + f + " --level 2 --dontcopy")