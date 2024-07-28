hovaten= input()
hovaten=hovaten.strip()
while "  " in hovaten:
    hovaten=hovaten.replace("  "," ")
hovaten=hovaten.title()
print(hovaten)