from constants import *
from main import Mover

def init():
    print(title + "\n" + line + "\n" + r"Use -- as a seperator, e.g. for a multi move" + "\n" + r"multi_move Desktop\dest2--test.txt--test2.txt--test3.txt--Desktop\dest1" + "\n" + "\n" + r"Single Move Example:" + "\n" + r"move Desktop\dest2\test.txt--Desktop\dest1" + "\n" + line + "\n" + cmds + "\n" + line)
    Mover().cmdloop()