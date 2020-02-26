import tetrino
import tempfile
import random
import math
import time

tshape = [0xf000,
        0xe200,
        0xe400,
        0xe800,
        0xcc00,
        0xc600,
        0xc440,
        0xc880,
        0x8E00,
        0x8c80,
        0x8c40,
        0x88c0,
        0x8888,
        0x6c00,
        0x4E00,
        0x4C80,
        0x44C0,
        0x4C40,
        0x2E00]
charline = ["....", "...#", "..#.", "..##",
            ".#..", ".#.#", ".##.", ".###",
            "#...", "#..#", "#.#.", "#.##",
            "##..", "##.#", "###.","####"]

class Tetrino(object):
    def __init__(self):
        self.data = []
        self.result = []

    def do_play(self):
        afile = tempfile.mkstemp()[1]
        f = open(afile,"w")
        if len(self.data) < 1:
            return
        for i in self.data:
            for s in i:
                f.write(s)
                f.write('\n')
            f.write('\n')
        f.close()
        start = time.time()
        result = tetrino.resolve(afile)
        self.delta = time.time() - start
        rep = len(result)
        sqa = int(math.sqrt(rep))
        self.result = map(lambda i: result[i:i+sqa], range(0,rep,sqa))

    def print_result(self):
        col = 4
        cdata = self.data[:]
        all = []
        line = []
        for i,d in enumerate(self.data):
            if i % col == 0:
                aline = []
                for j in range(col):
                    try:
                        x = cdata.pop(0)
                        aline.append(x)
                    except:
                        pass
                all.append(aline)

        #print(list(self.result))
        all_line = []
        for x in all:
            print(x)
            for i in range(4):
                aline = list()
                for xx in x:
                    aline.append(xx[i])
                all_line.append("   ".join(aline))
        print("\n".join(all_line))

    def build_random(self, nb_tetrino):
        self.data = []
        for i in range(nb_tetrino):
            self.data.append(Tetrino.as_char(tshape[random.randint(0,18)]))

    @staticmethod
    def as_char(shape):
        res = list()
        l1 = charline[(shape & 0xf000) >> 12]
        l2 = charline[(shape & 0x0f00) >> 8]
        l3 = charline[(shape & 0x00f0) >> 4]
        l4 = charline[shape & 0x000f]
        return [l1,l2,l3,l4]

if __name__ == '__main__':
    t = Tetrino()
    t.build_random(14)
    t.do_play()
    t.print_result()