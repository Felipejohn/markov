import numpy as np

# Trump's speeches here: https://github.com/ryanmcdermott/trump-speeches
def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
def markovify(n_words):

    trump = open('speech.txt', encoding='utf8').read()
    
    corpus = trump.split()
    
    pairs = make_pairs(corpus)
    
    word_dict = {}
    
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
     
    first_word = np.random.choice(corpus)
    
    while first_word.islower():
        first_word = np.random.choice(corpus)
    
    chain = [first_word]
    
    
    
    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
    
    final = ' '.join(chain)
    print(final)

def main():
    
    
    executions = 20
    for i in range(executions):
        markovify(200)
        print("\n")
    
        



if __name__ == '__main__':
    main()