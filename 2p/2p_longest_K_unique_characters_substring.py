# Longest K unique characters substring
# Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.

# Example 1:

# Input:
# S = "aabacbebebe", K = 3
# Output: 
# 7
# Explanation: 
# "cbebebe" is the longest substring with 3 distinct characters.

# s = "aabacbebebe"
# k = 3
s = "joizyglhbetjlvglzvvktxqsslufceppzpgogrifbeyuiblmgcqtkhhbimxigczvbtvrtsperlhunsyywgnttbwjgunjwjtqzqvrdumddtzaffcmjlakmfappoqqkvmfnevaabqxtzslodalgvtwvbsknohmjcumrrqktskvidbizexkprdonsjkbcoeplcafdalmvfaswnjkiqcwowhykczbdkankmkrrwsmcomaubfelnljztemcbmmoptndjodpqnikglvraezkvfxcphvgdgkouirhidbdtesjogrilbxhgtqprexyxptbqdxnwsuddzoiuumlbbgmhuzbgaslssvtexzlipsqfrfvxbkxmazocqvtaguvxmoqvhkfklucswkizrpatpakmuswqdsmxtnuujewtwtrnofowrgmxegwkxokotqhfodaegkmopjpdvpxzjrunwfqeldjhajnjzaargszgxakniopptsoakustvpbtocrovfceofpbeddqeidyvosbwbspesilldkdvocbfrbzthbgsnzaabjfbeanwoicritttjvkromyiodiazfgzktgkeqjmojamqrdusaibheiivnvmokacqudrcairqtisixcjxjsdubgusrcpleludvkjiabbeukbeadqruccuhwcrgosagtuyjfhnaniapxkrqdbmdsbxrzriyszsoguditxxpvdopzktljyrdzxunnybfzfqoezhizbustnwlpqypfqtgxapvwrcybnsjfrsdhyafsdglucczqtoazaycxybnlratmdqphtdwqsddhkrhvbgsytp"
k = 10

n = len(s)
i=0
j=0
ans = -1
hash_map = {}
while(j<n):
    # print(j, i, s[j], s[i], s[i:j+1], hash_map)
    if s[j] not in hash_map:
        hash_map[s[j]] = 0
    hash_map[s[j]] += 1
    if len(hash_map) < k:
        j+=1
    elif len(hash_map) == k:
        ans = max(ans, j-i+1)
        j+=1
    else:
        while(len(hash_map) > k):
            hash_map[s[i]] -= 1
            if not hash_map[s[i]]:
                hash_map.pop(s[i])
            i+=1
        j+=1
print(ans)
