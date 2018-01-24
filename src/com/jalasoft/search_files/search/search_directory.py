import os
for file in os.listdir("c://"):
    if file.endswith(".txt"):
        print(os.path.join("c://", file))