import argparse
from app import config
from appfly.app import app
from appfly.server import Server

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="Start your API in debug mode. [1/0]")
args = parser.parse_args()

config["debug"] = args.debug

if __name__ == '__main__':
    srv = Server(app)
    srv.start(config)