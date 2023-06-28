#!/usr/bin/env python3
from watcher.watcher import Watcher
from handler.handler import MyHandler


def main():
    w = Watcher("/home/tyguy/Desktop", MyHandler())
    w.run()

if __name__=="__main__":
    main()
