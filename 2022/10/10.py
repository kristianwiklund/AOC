def draw(c,x):

    c = (c)%40

    if not c%40:
        print("")
    
    if c==x:
        print("#",end="")
    elif c==(x+1):
        print("#",end="")
    elif c==(x-1):
        print("#",end="")
    else:
        print(".",end="")



with open("input.txt","r") as fd:

    lines = [x.strip() for x in fd.readlines()]

    c=1
    p=1
    x=1
    score = 0
    
    for line in lines:
        l =line.split(" ")
        op = l[0]
        draw(p,x)
        p+=1

        if op == "noop":
            c+=1
                        
        elif op == "addx":
            c+=1
            if c==20 or ((c-20)%40) == 0:
                #print (c, x, (c)*x)
                score+=(c)*x
            x+=int(l[1])
            c+=1
            draw(p,x)
            p+=1
            
        if c==20 or (c-20)%40 == 0:
            #print (c, x, c*x)
            score+=c*x
print("")
print("Part 1:", score)

        
        
