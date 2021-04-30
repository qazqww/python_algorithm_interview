from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        new_paragraph = ""

        for ch in paragraph:
            if ch.isalnum():
                new_paragraph += ch.lower()
            else:
                new_paragraph += ' '
        
        para_list = new_paragraph.split()
        # 이상의 과정은 정규표현식으로 더 깔끔하게 작성할 수 있다

        para_count = Counter(para for para in para_list if para not in banned)
        return para_count.most_common(1)[0][0]

print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))