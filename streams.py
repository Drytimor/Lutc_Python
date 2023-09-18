class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'converter must be defined'


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


import sys
obj = Uppercase(open('datafile.txt'), sys.stdout)
obj.process()


class HTMLize:
    def write(self, line):
        print(f'<PRE>{line.strip()}</PRE>')


Uppercase(open('datafile.txt'), HTMLize()).process()