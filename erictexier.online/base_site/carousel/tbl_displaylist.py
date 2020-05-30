import json
import gzip

class TblDisplayList(object):
    ''' a list of TblDisplay
    '''
    def __init__(self, filename=""):
        self._data = list()
        self._filename = list()

    def is_valid(self):
        return os.path.exists(self_filename)

    def load_data(self):
        d = self.read()
        if 'posts' in self._data:
            self._data = 

    def save_data(self):
        d = dict()
        d.update({'posts': self._data})
        self.write(d)

    def write(self, d):
        f = None
        if self.isGz(self._filename) == True:
            f = self.OpenFileGz(self._filename, "w")
        else:
            f = self.OpenFile(self._filename, "w")
        if f != 0:
            f.write(d)
            f.close()
        return True

    def read(self):
        d = dict()
        if self.isGz(self._filename) == True:
            f = self.OpenFileGz(self._filename, "r")
            if f != 0:
                astr = f.read()
                d = json.loads(astr)
                f.close()
                return d
        else:
            if os.path.exists(self._filename):
                try:
                    f = self.OpenFile(self._filename, 'r')
                    astr = f.read()
                    f.close()
                    d = json.loads(astr)
                except:
                    return d
            else:
                return d
            return d
        return d

    def isGz(self,filename):
        return os.path.splitext(self._filename)[1] == ".gz" 

    def openFile(self, mode = "r"):
        try:
            fFile = open(self._filename, mode)
        except:
            print("Can't open %r" % self._filename)
            fFile = None

        return fFile

    def OpenFileGz(self, mode = "r"):
        fFile = None
        if mode == "r":
            try:
                fFile = gzip.open(self._filename, "rb")
            except IOError:
                # can't read the file
                print("Can't read %r" % afile)
                fFile = None
        else: ## for write
            try:
                fFile = gzip.open(self._filename, "wb")
            except IOError:
                print("Can't read %r" % afile)
                fFile = None
        return fFile

    @staticmethod
    def asDict(astr):
        return json.loads(astr)
