class File:
    def __init__(self, name):
        self.name = name
        self.content = ""

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.directories = {}

    def create_file(self, file_name):
        if file_name in self.files:
            print(f"File {file_name} already exists.")
        else:
            self.files[file_name] = File(file_name)
            print(f"File {file_name} created.")

    def write_file(self, file_name, content):
        if file_name in self.files:
            self.files[file_name].content = content
            print(f"Written to {file_name}.")
        else:
            print(f"File {file_name} does not exist.")

    def read_file(self, file_name):
        if file_name in self.files:
            print(f"Reading {file_name}:")
            print(self.files[file_name].content)
        else:
            print(f"File {file_name} does not exist.")

    def create_directory(self, dir_name):
        if dir_name in self.directories:
            print(f"Directory {dir_name} already exists.")
        else:
            self.directories[dir_name] = Directory(dir_name)
            print(f"Directory {dir_name} created.")

    def list_directory(self):
        print(f"Listing directory {self.name}:")
        for dir_name in self.directories:
            print(f"Directory: {dir_name}")
        for file_name in self.files:
            print(f"File: {file_name}")

class FileSystem:
    def __init__(self):
        self.root = Directory("root")
        self.current_directory = self.root

    def change_directory(self, dir_name):
        if dir_name == "..":
            if self.current_directory.name != "root":
                self.current_directory = self.root
            else:
                print("Already at root directory.")
        elif dir_name in self.current_directory.directories:
            self.current_directory = self.current_directory.directories[dir_name]
        else:
            print(f"Directory {dir_name} does not exist.")

# Example usage
fs = FileSystem()
fs.current_directory.create_file("file1.txt")
fs.current_directory.write_file("file1.txt", "Hello, Syllable OS!")
fs.current_directory.read_file("file1.txt")
fs.current_directory.create_directory("docs")
fs.current_directory.create_directory("photos")
fs.current_directory.list_directory()
fs.change_directory("docs")
fs.current_directory.create_file("doc1.txt")
fs.current_directory.write_file("doc1.txt", "This is a document.")
fs.current_directory.read_file("doc1.txt")
fs.change_directory("..")
fs.current_directory.list_directory()
