
play = {}
play["A"] = {
    "X":1+3, # rock, rock, draw
    "Y":2+6, # rock, paper, win
    "Z":3+0, # rock, scissors, loss
    }

play["B"] = {
    "X":1+0, # paper, rock, loss
    "Y":2+3, # paper, paper, draw
    "Z":3+6, # paper, scissors, win
    }


play["C"] = {
    "X":1+6, # scissors, rock, win
    "Y":2+0, # scissors, paper, loss
    "Z":3+3, # scissors, scissors, draw
    }

    

with open("input.txt","r") as fd:

    lines = fd.readlines()
    score = 0
    for line in lines:
        line = line.strip()
        s = line.split(" ")
        score = score + play[s[0]][s[1]]

print(score)
