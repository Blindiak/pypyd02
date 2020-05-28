class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0,
                 skip_bottom=0):
        self.bad = False
        self.header = header
        f = open(filename, 'r')
        self.f = f
        size = 0
        self.data = []
        self.sep = sep
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        read_data = f.readline()
        read_data = read_data[:-1]
        split = read_data.split(sep)
        self.data += [split]
        self.size = len(split)
        for line in f:
            if line == "":
                break
            line = line[:-1]
            split = line.split(self.sep)
            self.data += [split]
            if self.size != len(split):
                self.bad = True
                break

    def __enter__(self):
        if self.bad:
            return None
        return self

    def __exit__(self, *args):
        self.f.close()

    def getdata(self):
        if self.header:
            self.skip_top += 1
        return self.data[self.skip_top: len(self.data) - self.skip_bottom]

    def getheader(self):
        if self.header:
            return self.data[0]
        return None


if __name__ == "__main__":
    with CsvReader('good.csv', ',', True, 1, 1) as file:
        data = file.getdata()
        header = file.getheader()
        print(header, data)
