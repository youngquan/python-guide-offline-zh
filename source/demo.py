with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

import sys
assert ('linux \n' in sys.paltform), \
        "hello"


def munge(input: str, output: int = 0, a=5) -> str:
    pass

def munge(input: str, output: int = 0, a=5):
    pass