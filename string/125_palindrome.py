class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = list()

        for ch in s:
            # ch.isalnum()으로 대체할 수 있다
            if 'a' <= ch <= 'z' or '0' <= ch <= '9':
                new_str.append(ch)

        print(new_str)

        for i in range(int(len(new_str) / 2)):
            if new_str[i] != new_str[len(new_str) - 1 - i]:
                return False
        return True
        # => return new_str == new_str[::-1]
        # 문자열 슬라이싱은 내부적으로 C로 구현되어있어 속도가 빠르다.

print(Solution().isPalindrome('A man, a plan, a canal: Panama'))


# 수정 전 코드의 문제점 : 조건에 맞는 ch를 없애면서 계속 s가 갱신되기 때문에 시간이 매우 오래 걸리는듯
'''
def pelindrome(s) -> bool:
    s = s.lower()

    for ch in s:
        if not ('a' <= ch <= 'z' or '0' <= ch <= '9'):
            s = s.replace(ch, '')

    print(s)

    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True
'''