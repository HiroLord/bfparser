import sys
code = ""
fname = sys.argv[1]
with open(fname) as f:
    content = f.readlines()
code = ''.join([x.strip() for x in content])

if len(sys.argv) > 2:
    fname2 = sys.argv[2]
    with open(fname2) as f:
        content = f.readlines()
    inp = ''.join([x for x in content])
    inpIndex = 0

def readInput():
    global inp
    global inpIndex
    out = inp[inpIndex]
    inpIndex += 1
    return ord(out)

class Bucket(object):
    
    def __init__(self):
        self.val = 0
        self.right = None
        self.left = None
        self.num = 1
    
    def moveRight(self):
        if self.right == None:
            self.right = Bucket()
            self.right.left = self
            self.right.num = self.num + 1
        return self.right

    def moveLeft(self):
        if self.left == None:
            self.left = Bucket()
            self.left.right = self
            self.left.num = self.num - 1
        return self.left

    def up(self):
        self.val += 1

    def down(self):
        self.val -= 1

    def printSelf(self):
        #sys.stdout.write(chr(self.val))
        print(chr(self.val), self.num)

bucket = Bucket()

index = 0

def loop(ind):
    global bucket
    global index
    print("start value", bucket.val)
    if bucket.val == 0:
        while code[index] != ']':
            index += 1
        return
    index += 1
    while parse(index):
        index += 1
        print(index)
    if bucket.val != 0:
        print("end value", bucket.val)
        index = ind
        loop(index)

def parse(ind):
    global bucket
    a = code[ind]

    if   a == '.':
        bucket.printSelf()
    elif a == '+':
        bucket.up()
    elif a == '-':
        bucket.down()
    elif a == '>':
        bucket = bucket.moveRight()
    elif a == '<':
        bucket = bucket.moveLeft()
    elif a == '[':
        loop(ind)
        #return False
    elif a == ',':
        bucket.val = readInput()
        print "Read in ", bucket.val
    elif a == ']':
        return False
    return True


while index < len(code):
    parse(index);
    index += 1

print ''
