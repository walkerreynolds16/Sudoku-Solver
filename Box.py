class Box:

    def __init__(self, num, row, col):
        self.num = num
        self.row = row
        self.col = col

    def __str__(self):
        return "Num: " + str(self.num) + " Row: " + str(self.row) + " Col: " + str(self.col)

    def increase(self):
        if(self.num == 9):
            self.num = 0
        else:
            self.num += 1
