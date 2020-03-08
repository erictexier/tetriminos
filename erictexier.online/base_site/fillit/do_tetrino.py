# -*- coding: utf-8 -*-

import tempfile
import random
import math
import time
import datetime

try:
    import tetrino
except Exception as e:
    class TetrinoDump:
        @staticmethod
        def resolve(cmd):
            return "TETRINO NOT    ACCESSIBLE UNDER CONSTRUCTION ......."
    tetrino = TetrinoDump()

tshape = [
        0xf000,
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

randrgb = [[random.randint(60, 200),
            random.randint(80, 200),
            random.randint(120, 200)] for i in range(26)]
randcolor = ["#%x%x%x" % (x[0], x[1], x[2]) for x in randrgb]
cletter = ["%c" % (x + 65) for x in range(26)]
colormap = dict(zip(cletter, randcolor))
# for 3d we keep the color as 3 int to allow for alpha to be added easely
colormap3d = dict(zip(cletter, randrgb))
colormap[' '] = "#ffffff"
colormap['.'] = "#ffffff"


class Letterbox(object):
    """
        Quick map from letter to color, used in template
    """
    def __init__(self, c):
        self.letter = c
        if c in colormap:
            self.color = colormap[c]
        else:
            self.color = "#000000"


class Tetrino(object):
    """
        Wrapper around the tetrino module to manage interaction
    """
    def __init__(self):
        self.data = []
        self.result = []

    def do_play(self):
        ''' run tetrino module and save in temp area
        '''
        if len(self.data) < 1:
            return
        afile = tempfile.mkstemp(
            prefix='fillit-',
            suffix=datetime.datetime.utcnow().strftime("-%Y-%m-%d-%H-%M"))[1]
        tet = list()
        n = 65
        with open(afile, "w") as f:
            for i in self.data:
                letters = list()
                for s in i:
                    f.write(s)
                    letters.append(s.replace("#", "%c" % n))
                    f.write('\n')
                n += 1
                tet.append(letters)
                f.write('\n')
        self.data = tet
        start = time.time()
        result = tetrino.resolve(afile)
        self.delta = time.time() - start
        rep = len(result)
        self.sqa = int(math.sqrt(rep))
        self.stat = 0
        for x in result:
            if x == '.':
                self.stat += 1
        if rep > 0:
            self.stat = 100 - (self.stat * 100 / rep)
        self.result = list(map(lambda i: result[i:i + self.sqa],
                               range(0, rep, self.sqa)))
        with open(afile, "a+") as out:
            out.write("grid:\n")
            out.write('{}\nsec:{}-{}%'.format(
                                        '\n'.join(self.result),
                                        self.delta,
                                        self.stat))

    @staticmethod
    def wrap_box_result(aline):
        result = []
        for l in aline:
            result.append([Letterbox(x) for x in l])
        return result

    def show_in_line(self, col=4, color=True):
        """ Split the input to be display as line in html
        """
        cdata = self.data[:]
        all = []
        line = []
        for i, d in enumerate(self.data):
            if i % col == 0:
                aline = []
                for j in range(col):
                    try:
                        x = cdata.pop(0)
                        aline.append(x)
                    except:
                        pass
                all.append(aline)

        all_line = []
        for x in all:
            for i in range(4):
                aline = list()
                for xx in x:
                    aline.append(xx[i])
                all_line.append(" ".join(aline))
            if not color:
                all_line.append("-")
        if not color:
            all_line = all_line[:-1]
            return all_line
        return Tetrino.wrap_box_result(all_line)

    def build_random(self, nb_tetrino):
        """
            build a list of tetrino from random calls
        """
        global colormap3d
        global colormap
        randrgb = [[random.randint(60, 200),
                    random.randint(80, 200),
                    random.randint(120, 200)] for i in range(26)]
        randcolor = ["#%x%x%x" % (x[0], x[1], x[2]) for x in randrgb]
        cletter = ["%c" % (x + 65) for x in range(26)]
        colormap = dict(zip(cletter, randcolor))
        # for 3d we keep the color as 3 int to allow
        # for alpha to be added easely
        colormap3d = dict(zip(cletter, randrgb))
        colormap[' '] = "#ffffff"
        colormap['.'] = "#ffffff"

        self.data = []
        for i in range(nb_tetrino):
            self.data.append(Tetrino.as_char(tshape[random.randint(0, 18)]))

    @staticmethod
    def as_char(shape):
        """ remap the short int description of tetrimino to #'s and .'s
            result: return a list with 4 strings corresponding to each line
        """
        charline = ["....", "...#", "..#.", "..##",
                    ".#..", ".#.#", ".##.", ".###",
                    "#...", "#..#", "#.#.", "#.##",
                    "##..", "##.#", "###.", "####"]
        res = list()
        l1 = charline[(shape & 0xf000) >> 12]
        l2 = charline[(shape & 0x0f00) >> 8]
        l3 = charline[(shape & 0x00f0) >> 4]
        l4 = charline[shape & 0x000f]
        return [l1, l2, l3, l4]

    @staticmethod
    def lookup_letter(res, letter):
        result = list()
        offx = 0
        offy = 0
        destx = 0
        desty = 0
        for y, r in enumerate(res):
            for x, l in enumerate(r):
                if l == letter:
                    new_r = r[:x] + '.' + r[x+1:]
                    return res[:y] + [new_r] + res[y+1:], x, y
        return (result, destx, desty)

    def get_segment_anim(
                        self,
                        nb_col=4,
                        xspace=14,
                        yspace=14,
                        rmargin=10,
                        tmargin=10,
                        spacing=12,
                        for3d=False,
                        scalegame=0.):
        segments = list()
        res = self.result
        start = self.show_in_line(nb_col, color=False)
        table1offset = (tmargin + spacing + (yspace * len(start))) * scalegame
        sizex = ((nb_col + 2) * xspace) + rmargin

        for y, line in enumerate(start):
            for x, letter in enumerate(line):
                if letter not in [' ', '.', '-']:
                    res, destx, desty = self.lookup_letter(res, letter)
                    segments.append([[x, y], [destx, desty], letter])

        if for3d:
            segments = [[[(val[0][0] * xspace) + rmargin,
                          (val[0][1] * yspace) + tmargin],
                         [(val[1][0] * xspace) + rmargin + (sizex/4),
                          (val[1][1] * yspace) + table1offset],
                        colormap3d[val[2]]] for val in segments]
        else:
            segments = [[[(val[0][0] * xspace) + rmargin,
                          (val[0][1] * yspace) + tmargin],
                         [(val[1][0] * xspace) + rmargin + (sizex/4),
                          (val[1][1] * yspace) + table1offset],
                        colormap[val[2]]] for val in segments]
        return segments

if __name__ == '__main__':
    t = Tetrino()
    t.build_random(4)
    t.do_play()
    print(t.get_segment_anim())
