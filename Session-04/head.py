from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console

header = file_contents.split("\n")

print("First line of the RNU6_269P.txt file:", header[0])