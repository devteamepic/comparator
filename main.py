# -*- coding: utf-8 -*-
import sys
import single_discipline_comparator as sdc

def main():
    print(str(sys.argv))
    options = {
        '-sd' : sdc.compare,
        '-md' : 'asdf',
        '-h' : 'asdffasfd'
    }
    options[sys.argv[1]]()


if __name__ == "__main__":
    main()
