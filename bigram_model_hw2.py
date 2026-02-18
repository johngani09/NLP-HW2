
from collections import defaultdict

corpus = [
"<s> I love NLP </s>",
"<s> I love deep learning </s>",
"<s> deep learning is fun </s>"
]

unigrams = defaultdict(int)
bigrams = defaultdict(int)

for sent in corpus:
    words = sent.split()
    for w in words:
        unigrams[w] += 1
    for i in range(len(words)-1):
        bigrams[(words[i],words[i+1])] += 1

def bigram_prob(w1,w2):
    return bigrams[(w1,w2)] / unigrams[w1]

def sentence_prob(sentence):
    words = sentence.split()
    prob = 1.0
    for i in range(len(words)-1):
        prob *= bigram_prob(words[i],words[i+1])
    return prob

s1 = "<s> I love NLP </s>"
s2 = "<s> I love deep learning </s>"

p1 = sentence_prob(s1)
p2 = sentence_prob(s2)

print("P(S1) =", p1)
print("P(S2) =", p2)

if p1 > p2:
    print("Model prefers S1")
else:
    print("Model prefers S2")
