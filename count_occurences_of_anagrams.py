# Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

# Example 1:

# Input:
# txt = forxxorfxdofr
# pat = for
# Output: 3
# Explanation: for, orf and ofr appears
# in the txt, hence answer is 3.


def search(pat, txt):
    pat_dict = {}
    for i in pat:
        if i not in pat_dict:
            pat_dict[i] = 0
        pat_dict[i] += 1
    text_dict = {}
    k = len(pat)
    n = len(txt)
    ans = 0
    i=0
    j=0
    while(j<n):
        if txt[j] not in text_dict:
            text_dict[txt[j]] = 0
        text_dict[txt[j]] += 1
        if j-i+1 < k:
            j+=1
        elif j-i+1==k:
            flag = True
            for pat_c in pat_dict:
                if pat_c not in text_dict or pat_dict[pat_c] != text_dict[pat_c]:
                    flag = False
            if flag:
                ans +=1
            if text_dict[txt[i]]:
                text_dict[txt[i]] -= 1
            j+=1
            i+=1
    return ans


print(search("abc", "abcferhabc"))