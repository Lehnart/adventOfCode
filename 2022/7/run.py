class File:

    def __init__(self, is_directory: bool, name: str, size=0, parent=None, children=None):
        if children is None:
            children = []
        self.children = children
        self.is_directory = is_directory
        self.parent = parent
        self.name = name
        self.size = size

    def absolute_path(self):
        abs_path = self.name
        parent = self.parent
        while parent:
            abs_path = parent.name + "/" + abs_path
            parent = parent.parent
        return abs_path

    def print(self):
        print(self.absolute_path())
        print(self.is_directory)
        print(self.children)
        print("size ", self.size)
        print()


files = {}
current_file = None
with open("input.txt") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        line.strip()
        if line.startswith("$"):
            cmd = line[2:4]

            if cmd == "cd":
                next_dir_name = line[4:].strip()
                if next_dir_name == "..":
                    current_file = current_file.parent
                else:
                    f = File(True, next_dir_name, 0, current_file)
                    if f.absolute_path() not in files:
                        files[f.absolute_path()] = f
                    current_file = files[f.absolute_path()]

            if cmd == "ls":
                continue

        if line.startswith("dir"):
            next_dir_name = line[4:].strip()
            f = File(True, next_dir_name, 0, current_file)
            if f.absolute_path() not in files:
                files[f.absolute_path()] = f
            current_file.children.append(f)

        if line[0] in "0123456789":
            size, file_name = line.strip().split(" ")
            f = File(False, file_name, int(size), current_file)
            if f.absolute_path() not in files:
                files[f.absolute_path()] = f
            current_file.children.append(f)

files_to_process = [files[filename] for filename in files if files[filename].children == []]
files_processed = []
while len(files_to_process) > 0:
    file_to_process = files_to_process.pop(0)
    files_processed.append(file_to_process)
    if not file_to_process.parent:
        continue

    parent_file = file_to_process.parent
    parent_file.size += file_to_process.size
    if all( child in files_processed for child in parent_file.children ):
        files_to_process.append(parent_file)

total_size = 0
for filename in files:
    file = files[filename]
    if file.size <= 100000 and file.is_directory:
        total_size += file.size
print(total_size)
root_file = files["/"]
memory_needed = 30000000 - (70000000 - root_file.size)
best_dir = None
best_size = 0
for filename in files:
    file = files[filename]
    if not file.is_directory:
        continue
    if file.size >= memory_needed and (best_size == 0 or best_size>file.size) :
        best_dir = file
        best_size = file.size
print(best_dir.size)