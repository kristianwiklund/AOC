
with open("input.txt","r") as fd:

    program = [int(x) for x in fd.readlines()]

    pc = 0
    cnt = 0
    
    while pc >-1 and pc < len(program):

        newpc = pc + program[pc]
        program[pc] += 1
        pc = newpc
        cnt+=1

    print("Part 1:",cnt)
        
