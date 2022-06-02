import sys
print(sys.platform)

# windows
assert (sys.platform[0] in sys.platform), \
       'This code can only be executed under Windows'

# linux
assert ('linux' in sys.platform), \
       'This code can only be executed under Linux'
