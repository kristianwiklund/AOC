x = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with  open("input.txt","r") as fd:
    lines = fd.readlines()

    score=0
    for string in lines:
        string = string.strip()
        p0, p1 = string[:len(string)//2], string[len(string)//2:]

        a = set(p0)
        b = set(p1)
        score=score+x.index("".join(b.intersection(a)))

    print("part 1",score)


def r3(fd):
    a = set(fd.readline().strip())
    b = set(fd.readline().strip())
    c = set(fd.readline().strip())

    p = a.intersection(b.intersection(c))
    return (x.index("".join(p)))
    
with open("input.txt","r") as fd:

    sum=0
    while True:
        g = r3(fd)
        if g>0:
            sum=sum+g
        else:
            break
            
    print("part 2",sum)
            
