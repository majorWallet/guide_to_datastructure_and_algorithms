class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char) is not None:
                currentNode = currentNode.children[char]
            else:
                return None

        return currentNode

    def insert(self, word):
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char) is not None:
                currentNode = currentNode.children[char]
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                currentNode = newNode
        currentNode.children["*"] = None

    def collectAllWords(self, node = None, word = "", words = []):
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)
        return words

    def autoComplete(self, prefix):
        currentNode = self.search(prefix)
        if currentNode is None:
            return None
        else:
            return self.collectAllWords(currentNode, prefix)

    def printAllKeys(self, node = None): #17-3 solution
        currentNode = node or self.root
        for key in currentNode.children.keys():
            print(key, end = '')
            if key == "*":
                return None
            else:
                self.printAllKeys(currentNode.children[key])

    def autoCorrect(self, word): #17-4 solution
        currentNode = self.root
        str = ""
        for char in word:
            if currentNode.children.get(char) is not None:
                currentNode = currentNode.children[char]
                str += char
            else:
                return self.collectAllWords(currentNode, str)


wordFinder = Trie()
wordFinder.insert("tag")
wordFinder.insert("tank")
wordFinder.insert("tap")
wordFinder.insert("tan")
wordFinder.insert("today")
wordFinder.insert("total")
wordFinder.insert("well")
wordFinder.insert("went")
wordFinder.insert("we")
#print(wordFinder.collectAllWords())
wordFinder.printAllKeys()
print()
#print(wordFinder.autoComplete("ta"))
print(wordFinder.autoCorrect("taxifjk"))