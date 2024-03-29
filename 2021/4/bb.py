class BB:

    def rapl(self, fd):
        l = next(fd).strip()
#        print(">",l)
        n = l.split(" ")
        n = list(filter(lambda x:x!="",n))
        n = list(map(lambda x:int(x),n))
        self.board.append(n)

    def __repr__(self):
        s = "------------------\n"
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                s = s + str(self.board[i][j]) + " "
            s = s + "\n"
        s = s + "------------------\n"
        return s
        
    def __init__(self, fd):
#        print("---")
        self.board = []

        self.rapl(fd)
        self.rapl(fd)
        self.rapl(fd)
        self.rapl(fd)
        self.rapl(fd)

    def check(self):

        for i in self.board:
            if sum([x=='x' for x in i])==5:
                return True
                
        for i in range(len(self.board)):
            score = 0
            for j in self.board:
                if j[i] == 'x':
                    score = score + 1
            if score==5:
                return True
        return False

    def score(self):
        x = [sum(list(filter(lambda x:x!='x',t))) for t in [y for y in self.board]]
        return sum(x)
        
    def draw(self, number):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                if self.board[i][j] == number:
                    self.board[i][j] = 'x'

        return(self.check())


        
