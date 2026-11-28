with open("file.txt", "w") as f:
    f.write("hello universe\n")
    f.write("my name is mohini\n")
    f.write("i am a student\n")
    f.write("i am learning python\n")
    f.write("i am hardworking\n")

f = open("file.txt", "r")
data = f.read()
print(data)

f.close()