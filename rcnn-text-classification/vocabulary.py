class EnglishVocabulary:
    """description of class"""
    def __init__(self, fname):
        self.fname = fname
        self.l2i = {}
        self.i2l = []
        if not fname is None:
            self.load_vocab()
    def stoi(self, letter):
        if letter in self.l2i:
            return self.l2i[letter]
        return self.l2i['<unk>']
    def itos(self, id):
        if id < len(self.i2l):
            return self.i2l[id]
        return '<unk>'
            
    def append_letter(self, l):
        if l in self.l2i:
            return
        self.i2l.append(l)
        id = len(self.i2l) -1
        self.l2i[l] = id
    def load_vocab(self):
        self.append_letter('<unk>')
        self.append_letter('<s>')
        self.append_letter('</s>')
        with open(self.fname, encoding='utf8') as f:
            for line in f:
                nlines = line.split('\t')
                nline = nlines[0]
                for l in nline.split(' '):
                    self.append_letter(l)

    def save_vocab(self, filename):
        with open(filename, 'w', encoding='utf8') as f:
            for l in self.i2l:
                f.write(l + "\n")
    @staticmethod
    def load_from_file(filename):
        vocab = Vocabulary(None)
        with open(filename, encoding='utf8') as f:
            for l in f:
                l = l[:-1]
                vocab.append_letter(l)
        return vocab

class Vocabulary:
    def __init__(self, fname):
        self.fname = fname
        self.l2i = {}
        self.i2l = []
        if not fname is None:
            self.load_vocab()
    def stoi(self, letter):
        if letter in self.l2i:
            return self.l2i[letter]
        return self.l2i['<unk>']
    def itos(self, id):
        if id < len(self.i2l):
            return self.i2l[id]
        return '<unk>'
            
    def append_letter(self, l):
        if l in self.l2i:
            return
        self.i2l.append(l)
        id = len(self.i2l) -1
        self.l2i[l] = id
    def load_vocab(self):
        self.append_letter('<unk>')
        self.append_letter('<s>')
        self.append_letter('</s>')
        with open(self.fname, encoding='utf8') as f:
            for line in f:
                nline = line[:-3]
                for l in nline:
                    self.append_letter(l)

    def save_vocab(self, filename):
        with open(filename, 'w', encoding='utf8') as f:
            for l in self.i2l:
                f.write(l + "\n")
    @staticmethod
    def load_from_file(filename):
        vocab = Vocabulary(None)
        with open(filename, encoding='utf8') as f:
            for l in f:
                l = l[:-1]
                vocab.append_letter(l)
        return vocab
