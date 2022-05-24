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
except Exception as e:
    # If there is nothing
    print("""usage: IJP [-h] ijp_file compilation_py

VERSION INFO: Varson Alpha Next 1

positional arguments:
  ijp_file          What file to read IJP code from
  compilation_py    Compilation target, what file to compile to?

optional arguments:
  -h, --help  show this help message and exit""")
    sys.exit()


# Read code
code = open(filename, "r")
codes = code.readlines()
imports = "from tkinter import *\nfrom tkinter import colorchooser\nfrom tkinter import messagebox\nfrom tkinter import filedialog\nfrom tkinter import ttk"

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
    if line_whitespace.startswith("!write(") == True:
        if line.endswith(")") == True:

            line = line.replace(f"!write", "print", 1)
        else: pass

    # print(RED+TEXT+DEAFULT) --> write.red
    elif line_whitespace.startswith("!write.red(") == True:
        if line.endswith(")") == True:
            line = line.replace(f"!write.red", "print", 1)
        else: pass

    # "#/ijp colortext" replace "from colorama import *"
    elif line_whitespace.startswith("#/ijp colortext") == True:
        line = line.replace("#/ijp colortext", "from colorama import *", 1)

    # def --> fun
    elif "!fun" in line_whitespace:
        if line.endswith(":") == True:
            line = line.replace("!fun", "def", 1)
        else: pass

    # class --> hell
    elif "!hell" in line_whitespace:
        if line.endswith(":") == True:
            line = line.replace(line[0:5], "class", 1)
        else: pass

    # import --> imp
    elif line_whitespace.startswith("#!imp ") == True:
        if line == "#!imp tkall":
            line = line.replace(line, imports)
        else:
            pass

        line = line.replace(line[0:5], "import", 1)

    # from --> fr
    elif line.startswith("#!fr ") == True:
        line = line.replace(line[0:8], "from", 1)

    else: pass

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
    console = Console()
    console.print(syntax)

# Run python compile.py
def run_code():
    subprocess.run(["python", compile_py])

if __name__ == '__main__':
    # Check first line
    if codes[0] == "#/ijp python\n": pass
    elif codes[0] != "#/ijp python\n":
        print("Initalization Error: First line must be #/ijp python when writing IJP (its just python) code")
        sys.exit()

    try:
        run_code()
        pass
    except Exception as pyerror:
        print(pyerror)
