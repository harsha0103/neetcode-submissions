from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei= defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern =word[:j]+'*'+ word[j+1:]
                nei[pattern].append(word)
        
        visited=set([beginWord])
        q=deque([(beginWord,1)])

        while q:
            current_word,length=q.popleft()
            if current_word==endWord:
                return length
            
            for j in range(len(current_word)):
                pattern=current_word[:j]+'*'+ current_word[j+1:]
                for word in nei[pattern]:
                    if word not in visited:
                        q.append((word,length+1))
                        visited.add(word)
        return 0