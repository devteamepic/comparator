# -*- coding: utf-8 -*-
import sys
import single_dicipline_comparator as sdc


if __name__ == "__main__":
    print(str(sys.argv))
    options = {
        '-sd' : sdc.compare,
        '-md' : 'asdf',
        '-h' : 'asdffasfd'
    }
    options[sys.argv[1]]()
#    main()