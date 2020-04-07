
import argparse,itertools

def len_iterable(iterable): #iterableの長さを返す
    return sum(1 for _ in iterable)

def parts_len(length,pieces):#何行ごとに区切るか,generator関数
    t = length//pieces
    return (t+1 if length%pieces else t for i in range(pieces)) #パターン2

def filename(i): #ファイル命名
    return 'work/x'+chr(97+i//26)+chr(97+i%26)

def main():
    length = len_iterable(args.file)
    args.file.seek(0)
    for i,n in enumerate(parts_len(length,args.pieces)):
        with open(filename(i),"w") as newfile:
            for line in itertools.islice(args.file,n):
                newfile.writelines(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Split a file into N pieces')
    parser.add_argument("file",
                        type=argparse.FileType('r'),
                        )
    parser.add_argument("-n","--pieces",
                        type=int,
                        default=3,
                       )
    args = parser.parse_args()
    
    main()