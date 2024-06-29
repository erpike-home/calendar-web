import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Run a ChurchApp backend application.')
    parser.add_argument("--reload", action="store_true", help="reload app on code update")
    return parser.parse_args()
