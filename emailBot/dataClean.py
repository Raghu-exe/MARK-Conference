with open("swatNames.txt", "r") as f:
    nameLines = f.readlines()

for i in range(len(nameLines)):
    if "," in nameLines[i]:
        nameLines[i] = nameLines[i].strip().replace(",", "")
    if "@" in nameLines[i]:
        nameLines[i] = nameLines[i].strip()
    elif '.' in nameLines[i]:
        nameLines[i] = nameLines[i].strip() + "@rutgers.edu"
    else:
        nameLines[i] = nameLines[i].strip() + "@scarletmail.rutgers.edu" 

for i in range(len(nameLines)):
    nameLines[i] = nameLines[i].replace("edu", "edu\n")

with open("cleanedSwatNames.txt", "w") as f:
    f.writelines(nameLines)

print("File updated successfully.")