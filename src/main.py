from cmd import Cmd
from arg_parser import initialize_parser
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
            with open("./last.txt", "w") as f:
                f.write("{}**SINGLE".format(inp))
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
        with open("./last.txt", "w") as f:
            f.write("{}**MULTI".format(inp))
        print("Moved {} out of {} files!".format(moved, to_move_counter))


    def do_revert(self, inp):
        with open("./last.txt", "r") as f:
            last = f.read()
        move_type = last.split("**")[-1]
        if move_type == "MULTI":
            raw = last.split("**")[0].split("--")
            old_root = raw[0]
            new_dest = raw[-1]
            actual = []
            for x in raw:
                if str(x) == str(old_root) or str(x) == str(new_dest):
                    pass
                else:
                    try:
                        actual.append(x)
                        dest1 = r"{}{}\{}".format(config.root, new_dest, x)
                        dest2 = "{}{}".format(config.root, old_root)
                        os.system(f'cd ../../../../../../../ & move "{dest1}" "{dest2}"')
                    except Exception as error:
                        print("Error while moving files {}".format(error))
                        continue
            print("Reverted last move -> type: multi-move")
            sp = "{}--{}--{}".format(new_dest, "--".join(actual), old_root)
            with open("./last.txt", "w") as f3:
                f3.write("{}**MULTI".format(sp))
        elif move_type == "SINGLE":
            old_raw = last.split("**")[0].split("--")[0].split("\\")
            old_raw.pop()
            old = "\\".join([y for y in old_raw])
            file = last.split("**")[0].split("--")[0].split("\\")[-1]
            new = last.split("**")[0].split("--")[1]
            real_file = file.split("\\")[-1]
            dest1 = "{}{}\{}".format(config.root, new, real_file)
            dest2 = "{}{}".format(config.root, old)
            string = "{}\{}--{}".format(new, real_file, old)
            try:
                os.system(f'cd ../../../../../../../ & move "{dest1}" "{dest2}"')
                print("Reverted last move -> type: single-move")
                with open("./last.txt", "w") as f2:
                    f2.write("{}**SINGLE".format(string))
            except Exception as error:
                print("Looks like there was an error: {}".format(error))
                pass
