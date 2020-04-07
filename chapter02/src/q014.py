import sys
args = sys.argv

if len(args) != 2: #error1
    print("usage : q014.py [number]")
elif not args[1].isdigit() or int(args[1]) <= 0: #error2
    print("usage : number is natural number")
else:
    with open("data/popular-names.txt","r") as text: 
        lines = text.readlines()
        for line in lines[:int(args[1])]:
            print(line,end="")