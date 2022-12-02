
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

print("part 1:",score)

decide = {}
# rock
decide["A"] = {
    "X": 0+3, #lose, scissors
    "Y": 3+1, # draw, rock
    "Z": 6+2 # win, paper
    }
# paper
decide["B"] = {
    "X": 0+1, #lose, rock
    "Y": 3+2, # draw, paper
    "Z": 6+3 # win, scissors
    }

# scissors
decide["C"] = {
    "X": 0+2, #lose, paper
    "Y": 3+3, # draw, scissors
    "Z": 6+1 # win, rock
    }


with open("input.txt","r") as fd:

    lines = fd.readlines()
    score = 0
    for line in lines:
        line = line.strip()
        s = line.split(" ")
        score = score + decide[s[0]][s[1]]

print("part 2:",score)
        
