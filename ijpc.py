#/ijp python compiled
import subprocess, sys
from rich.console import Console
from rich.syntax import Syntax

# Get arguments
agrs = sys.argv
print(agrs)

try:
    filename = agrs[1]
    compile_py = agrs[2]
    print(filename, compile_py)

except Exception:
    print("""usage: IJP [-h] ijp_file compilation_py

VERSION INFO: Varson Alpha Next 1

positional arguments:
  ijp_file          What file to read IJP code from
  compilation_py    Compilation target, what file to compile to?

optional arguments:
  -h, --help    show this help message and exit
  -v --version  show version info
  -d --docs     load mkdocs server for documentation
  """)
    sys.exit()

# Read code
code = open(filename, "r")
codes = code.readlines()
imports = "from tkinter import *\nfrom tkinter import colorchooser\nfrom tkinter import messagebox\nfrom tkinter import filedialog\nfrom tkinter import ttk"

# Variables
variables = []
contents = []

"""
DIFFERENCES
!write("hello world") --> print("hello world")
!fun name(): --> def name():
#!imp --> import
#!fr --> from
#!write --> print

#!super root title geometry color

#/ijp python --> #/ijp python compiled
class --> hell
"""

lines = []
console = Console()

# Errors
class error:
    def __init__(self, type, line_num, content) -> None:
        self.type = type
        line_num = line_num
        self.content = content

    def invalidLangError(type, line_num, content):
        error_line = f"{type} on line {line_num}: {content}"

        console.rule(f"[italic blue]{type} + Tips")
        console.print(f"[red bold]{error_line}")
        console.print('[italic blue]You can use [italic green]#/ijp python[italic blue] [italic red](or "py" or "python" based on what the python command is on your laptop)[italic blue] to help you fix this error.')
        sys.exit()

    def MissingArgument(type, content):
        error_line = f"{type}: {content}"

        console.rule(f"[italic blue]{type} + Tips")
        console.print(f"[red bold]{error_line}")
        console.print('[italic blue]Please define a [italic green]variable name and "=" and content[italic blue] [italic red]for example: var name = "Joe"')
        sys.exit()

    def tksuper(type, content):
        error_line = f"{type}: {content}"

        console.rule(f"[italic blue]{type} + Tips")
        console.print(f"[red bold]{error_line}")
        console.print('[italic green]Example: tksuper root title geometry color')
        sys.exit()

# Check for space
def check_space(string):
    # counter
    count = 0
     
    # loop for search each index
    for i in range(0, len(string)):
         
        # Check each char
        # is blank or not
        if string[i] == " ":
            count += 1
         
    return count

# Parser
def parse(line):
    # remove whitespace at begining
    line_whitespace = line.lstrip()

    # print --> write
    if line_whitespace.startswith("write(") == True:
        if line.endswith(")") == True: line = line.replace(f"write", "print", 1)

    # def --> fun
    elif line_whitespace.startswith("fun ") == True:
        if line.endswith(":") == True: line = line.replace("fun ", "def ", 1)

    # class --> OOP
    elif line_whitespace.startswith("OOP") == True:
        if line.endswith(":") == True: line = line.replace("OOP", "class", 1)
    
    # print("") --> sp
    elif line_whitespace == "sepr":
        line = line.replace('sepr', "print('')")

    # Allow init
    elif line_whitespace.startswith("init(") == True:
        if line.endswith(":") == True: line = line.replace("init", "def __init__")

    # import --> imp
    elif line_whitespace.startswith("imp ") == True:
        if line == "imp tkall": line = line.replace(line, imports)

        line = line.replace("imp", "import", 1)

    # from --> fr
    elif line.startswith("fr ") == True:
        line = line.replace("fr", "from", 1)

    # strings
    elif line_whitespace.startswith("str") == True:
        # Convert line into list
        line_list = line.split(" ")

        try:
            # Check for type
            types = line_list[0]
            name = line_list[1]
            identifier = line_list[2]
            content = " ".join(line_list[3:])

            print(types, name, identifier, content)
            print(f"Type:{types}\nName:{name}\nIdentifier:{identifier}\nContent:{content}")

            prev = f"str {name} = {content}"
            new = f"{name} {identifier} str({content})"
            line = line.replace(prev, new, 1)
        except Exception:
            error.MissingArgument("Missing name, identifier, content", line)

    # integers
    elif line_whitespace.startswith("int") == True:
        # Convert line into list
        line_list = line.split(" ")

        try:
            # Check for type
            types = line_list[0]
            name = line_list[1]
            identifier = line_list[2]
            content = " ".join(line_list[3:])

            print(types, name, identifier, content)
            print(f"Type:{types}\nName:{name}\nIdentifier:{identifier}\nContent:{content}")

            prev = f"int {name} = {content}"
            new = f"{name} {identifier} int({content})"
            line = line.replace(prev, new, 1)
        except Exception:
            error.MissingArgument("Missing name, identifier, content", line)

    # floats
    elif line_whitespace.startswith("float") == True:
        # Convert line into list
        line_list = line.split(" ")

        try:
            # Check for type
            types = line_list[0]
            name = line_list[1]
            identifier = line_list[2]
            content = " ".join(line_list[3:])

            print(types, name, identifier, content)
            print(f"Type:{types}\nName:{name}\nIdentifier:{identifier}\nContent:{content}")

            prev = f"float {name} = {content}"
            new = f"{name} {identifier} float({content})"
            line = line.replace(prev, new, 1)
        except Exception:
            error.MissingArgument("Missing name, identifier, content", line)

    # bool
    elif line_whitespace.startswith("bool") == True:
        # Convert line into list
        line_list = line.split(" ")

        try:
            # Check for type
            types = line_list[0]
            name = line_list[1]
            identifier = line_list[2]
            content = " ".join(line_list[3:])

            print(types, name, identifier, content)
            print(f"Type:{types}\nName:{name}\nIdentifier:{identifier}\nContent:{content}")

            prev = f"bool {name} = {content}"
            new = f"{name} {identifier} bool({content})"
            line = line.replace(prev, new, 1)
        except Exception:
            error.MissingArgument("Missing name, identifier, content", line)

    # Check if /$ is in line
    elif line_whitespace.startswith("/$") == True: pass

    # Check if f"${varname}" in line
    elif f"$" in line:
        # Loop through variables
        for var in variables:
            # Loop through content
            for content in contents:
                # Replace varname with content
                line = line.replace(f"${var}", content, 1)

    #tksuper
    elif line.startswith("tksuper "):
        # Convert line to a list
        lists = line.split(" ")
        
        try:
            # get root, title, size, color
            var_root = lists[1]
            var_title = lists[2]
            var_size = lists[3]
            var_color = lists[4]

            line = f'''{var_root} = Tk()
root.title({var_title})
root.geometry({var_size})
root.configure(bg={var_color})'''
        except Exception:
            line_num = lists[0]
            error.TkSuper("Rw, WindowTitle, WindowSize, and WindowColor missing", line)

    line = line.replace("#/ijp python", "#/ijp python compiled")

    lines.append(line)
    #print(line)

# Loop through code
for line in codes:
    line = line.replace("\n", "")
    parse(line)

# Create new file in directory called compile_py.py
with open(compile_py, "w") as file:

    # Clear all text
    file.seek(0)
    file.truncate()
    file.close()

# Write to compile.property
for x in lines:
    files = open(compile_py, "a")
    files.write(f"{x}\n")

files.close()

# Print compiled code to terminal
my_code = open(compile_py, "r")
my_codes = my_code.read()
my_code.close()

# Output code
def output_code():
    syntax = Syntax(my_codes, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

# Run python compile.py
def run_code():
    subprocess.run(["python", compile_py])

if __name__ == '__main__':
    # Check first line
    if codes[0] == "#/ijp python\n": pass
    elif codes[0] != "#/ijp python\n":
        error.invalidLangError("Invalid IJP code", "1", codes[0])
        sys.exit()

    try:
        run_code()
        pass
    except Exception as pyerror:
        print(pyerror)
