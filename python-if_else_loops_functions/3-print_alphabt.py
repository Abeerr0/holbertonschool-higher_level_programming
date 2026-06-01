#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) not in [101, 113]:  # 101 is 'e', 113 is 'q'
        print("{}".format(chr(i)), end="")
