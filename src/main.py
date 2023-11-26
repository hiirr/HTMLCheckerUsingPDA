import os

rules = {}
start_state = ""
start_stack = ""
current_state = ""
accept_state = ""
stack = []
inp = []
line_counter = 1

def check_html():
    global stack
    global current_state
    global inp
    global line_counter
    # print(current_state)
    # print(stack)
    if inp[0]=="/" and len(inp) > 1:
        line_counter+=1
        inp = inp[1:]
        check_html()
    else:
        found = False
        for rule in rules[current_state]:
            if stack[-1] == rule[1]:
                if inp[0] == rule[0] or (rule[0] == "any" and inp[0] != "<" and inp[0] != ">" and inp[0] != "--"):
                    found = True
                    break
        # print(rule)
        if found:
            stack.pop()
            new_stack = []
            for symbol in rule[2]:
                new_stack.append(symbol)
            while len(new_stack)>0:
                s = new_stack.pop()
                stack.append(s)
            stack = list(filter(None,stack))
            current_state = rule[3]
            if (len(inp) > 1):
                inp = inp[1:]
                check_html()
            else:
                inp = []

def get_pda():
    global start_state
    global start_stack
    global accept_state
    global rules

    pda = open("pda.txt", "r")

    lines = [line.strip() for line in pda]

    start_state = lines[3]

    start_stack = lines[4]

    accept_state = lines[5]

    for i in range (7, len(lines)):
        line = lines[i].split()

        rule = [(line[1], line[2], line[4], line[3])]

        if not line[0] in rules.keys():
            rules[line[0]] = []
        
        rule = [tuple(a if a != "eps" else "" for a in x) for x in rule]
        rules[line[0]].extend(rule)

def get_input(string):
    global inp
    word = ""
    inQuotes = False
    for c in string:
        if c == " " and not inQuotes:
            inp.append(word)
            word = ""
        else:
            if c == "<" or c==">":
                inp.append(word)
                word = ""
            word += c
            if word == "<" or word == ">":
                inp.append(word)
                word = ""
            elif word[-2:] == "=\"":
                inp.append(word[:-1])
                word = "\""
                inQuotes = True
            elif word[-1] == "\"" and inQuotes:
                inQuotes = False
                if len(word) > 2:
                    inp.append(word)
                word = ""
    inp = list(filter(None,inp))
    if inp[-1] == "/":
        inp.pop()

get_pda()
current_state = start_state
stack.append(start_stack)

file = input("\nTuliskan nama file yang akan di cek: ")
file_path = "../test/" + file
if (file[-5:] != ".html"):
    file_path += ".html"

while not os.path.exists(file_path):
    print("File tidak ditemukan. Silahkan input ulang.")
    file = input("Tuliskan nama file yang akan di cek: ")
    file_path = "./test/" + file
    if (file[-5:] != ".html"):
        file_path += ".html"

f = open(file_path, "r")
string = ""
for line in f:
    line = line.strip()
    string += line + " / "
f.close()
get_input(string)
# print(inp)
check_html()
# print(current_state)
# print(inp)
if current_state == accept_state and len(inp) == 0:
    print("Accepted")
else:
    print("Syntax Error")
    print("There is fault in line: ", line_counter)
    f = open(file_path, "r")
    for i in range(0, line_counter-1):
        f.readline()
    print(f.readline())
    print(inp[0], "doesn't meet the corresponding rule.")