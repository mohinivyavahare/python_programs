with open("practice.txt", "w") as f:
    f.write("hi everyone\nwe are learning file I/O\nusing programming in python.")

def check_for_word():
    word = "programming"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("not found")

def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()