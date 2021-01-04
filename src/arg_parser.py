import argparse


def initialize_parser():
    """
    Initialize parser
    Returns a parser_args() object
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-root", "--root", help=r"Root destination -> C:\...\")
    return parser.parse_args()
