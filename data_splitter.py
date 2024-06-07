with open("data") as file:
    s = file.read()

s = s.replace('{"result', '\n{"result')
print(s)
