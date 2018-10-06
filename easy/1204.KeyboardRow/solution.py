def solution(words_list):
    l1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    l2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    l3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    
    res = []
    for word in words_list:
        print word
        if (all(char.lower() in l1 for char in word) or
            all(char.lower() in l2 for char in word) or
            all(char.lower() in l3 for char in word)):
            res.append(word)
    return res

print solution(["Hello", "Alaska", "Dad", "Peace"])