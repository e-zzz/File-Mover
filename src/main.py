from cmd import Cmd
from arg_parser import initialize_parser
import subprocess
import os


config = initialize_parser()

class Mover(Cmd):
    def do_exit(self, inp):
        print("Closing...")
        return True


    def do_config(self, inp):
        print("Current root directory is: {}".format(config.root))


    def do_move(self, inp):
        old = inp.split("--")[0]
        new = inp.split("--")[1]
        dest1 = "{}/{}".format(config.root, old)
        dest2 = "{}/{}".format(config.root, new)
        try:
            os.system(f'cd ../../../../../../../ & move "{dest1}" "{dest2}"')
            print("Moved file!")
        except Exception as error:
            print("Looks like there was an error: {}".format(error))
            pass


    def do_multi_move(self, inp):
        raw = inp.split("--")
        old_root = raw[0]
        new_dest = raw[-1]
        to_move_counter = (len(raw) - 2)
        moved = 0
        print(raw)
        for x in raw:
            if str(x) == str(old_root) or str(x) == str(new_dest):
                pass
            else:
                try:
                    dest1 = r"{}{}\{}".format(config.root, old_root, x)
                    dest2 = "{}{}".format(config.root, new_dest)
                    os.system(f'cd ../../../../../../../ & move "{dest1}" "{dest2}"')
                    moved += 1
                    print("Moved file {}/{}".format(moved, to_move_counter))
                except Exception as error:
                    print("Error while moving files {}".format(error))
                    continue
        print("Moved {} out of {} files!".format(moved, to_move_counter))