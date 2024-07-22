class WordsFinder:

    def __init__(self, *file_names):
        self.file_names= file_names


    def get_all_words(self):
       self.all_words = {}
       self.words = []
       self.pun = [',', '.', '=', '!', '?', ';', ':', ' - ']
       for f in self.file_names:
        with open(f, encoding = 'utf-8') as file:
            for i in file:
                i = i.lower()
                for sim in self.pun:
                    if sim != ' - ':
                        i = i.replace(sim,'')
                    else:
                        i = i.replace(sim,' ')
                self.words.extend(i.split())
       self.all_words = {self.file_names[0] : self.words}
       return self.all_words

    def find(self, word):
        word = word.lower()
        new_all_words = {}
        for i,j in self.get_all_words().items():
            if word in j:
                new_all_words = {self.file_names[0]:j.index(word)+1}
        return new_all_words

    def count(self,word):
        new_all_words = {}
        word = word.lower()
        cnt = []
        for i, j in self.get_all_words().items():
            cnt.extend(j)
        new_all_words = {self.file_names[0]: cnt.count(word)}
        return new_all_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего