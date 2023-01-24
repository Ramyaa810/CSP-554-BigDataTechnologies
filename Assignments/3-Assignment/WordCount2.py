from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")
alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n'}
a_n_count = 0
other_count = 0

class MRWordCount(MRJob):   

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            if any(word.startswith(firstletter) for firstletter in alphabet):
                yield 'count of words starts with a-n', 1
            else:
                yield 'count of words starts with other letters', 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)
             
   
if __name__ == '__main__':
    MRWordCount.run()


