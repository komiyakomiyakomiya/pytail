# _*_ coding: utf-8 _*_
import sys
import os.path


def tail_main(argv):
    if __name__ == "__main__":
        rFile = sys.argv[1]
        wCnt = 0
        fileSize = 0

        while 1:
            if fileSize != os.path.getsize(rFile):
                f = open(rFile, 'r')

                idx = 0
                for row in f:
                    if idx <= wCnt:
                        pass
                    else:
                        print(row)
                        wcnt += 1
                    idx += 1

                f.close()
                fileSize = os.path.getsize(rFile)
