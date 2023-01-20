from collections import namedtuple

InfoDTO = namedtuple('InfoDTO', ['name', 'link', 'description'])

if __name__ == '__main__':
    bin = InfoDTO('bin', '/bin', 'description __')
    print(bin, bin.name, sep='\n')