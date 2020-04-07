import sys,itertools

def filename(i): #ファイル命名
    return 'work/x'+chr(97+i//26)+chr(97+i%26)

def div_numlist(length,N): #何行ごとに区切るか
    return [length//N+1 if i < length%N else length//N for i in range(N)] #パターン1

args = sys.argv

if len(args) != 2: #error1
    print("usage : q016.py [number]")
elif not args[1].isdigit() or int(args[1]) <= 0: #error2
    print("usage : number is natural number")
else:
    with open("data/popular-names.txt","r") as text:
        lines = text.readlines() #メモリの浪費
        if(len(lines) < int(args[1])): #error3
            print("Number is too big.")
        else:
            ls = list(div_numlist(len(lines),int(args[1]))) #メモリの浪費2
            m = 0
            for i in range(int(args[1])):
                newfile = open(filename(i),"w") 
                newfile.writelines(lines[m:m+ls[i]])
                m += ls[i]
                newfile.close()