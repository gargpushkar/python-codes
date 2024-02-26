# import sys
# sys.setrecursionlimit(10**6) 
# Longest Common Subsequence
# Given two strings, find the length of longest subsequence present in both of them. Both the strings are in uppercase latin alphabets.

# Example 1:

# Input:
# A = 6, B = 6
# str1 = ABCDGH
# str2 = AEDFHR
# Output: 3
# Explanation: LCS for input strings “ABCDGH” and “AEDFHR” is “ADH” of length 3.

str1 = "RTCNBKHNRHDIOEKOSLMJCOKPIDBBARHDQHPJOIHSFTMSAAAFSDQCTJDOKILGTCPRSFRCNJIMPPNDSNNQCJOQKGPKCJIRSBDLSRMLKCQEIPMLLLCDHSIDLHETBOJDIJHFOAAFMFNCTAPKEDABQNECJEQDLQEIKGEGGNBEIEJFJFRDNERMFKFLIDNRLKOEHRIPDJIHGSPKFOFHFGCCEGTIFOJMNNTCEJJMBSDABMGSAHBORCAILESKMIPNLPIQMSFRTOTFBBQHORQEELSBKQREAKPECCLAIJKBKBRTHNMFSTCAKJHLSKCMGTBMRSGHARPGBJTKHJGORSHMJBJMHHJAGLFTKNHBTGPKFILOADCMKRDKDSHBEGIJLPDLBRARFIQGFCIHLFQBCISTQMNGRQITJBDNPREJIMRKCRFQHLILMTFTNTPLALJGKLJNIKSDBGSSADIKNQHDJPCCCIIPPGHGTFBPDHQMHMPFGDAFFMDIMDKPOSHQSCTOOCIHNIJEIEQMICJBCDBAKDGPBGFMKFDDHCMEBCNOABBHIPPGIGORTQMCJHLA"
str2 = "SGRFSJDDQIEQQDKSLGGHQQQEGRKQDJNALRPMOEHECGSMMHQNQHSFORBBMGONKIDTBDHMLGSDGIHDPERMFPLBBOTEEMGEERCTHKTMSTSIEHTJKHGCCJBISOIEDSJTFDAGSBFKHIBGJSLGQOQQEKEFJFHHEMOISSTNNFQMRDCTFRNOOPFODEBPFQTDQPPAPHBIJEQTRPENHRCIHOPMSJSNGOKJTODTPNEDKNNOOJNJAJHJABRFKNJQBPLJMRCMHASJPRTLRDEOANCFMKKLCCQACDCGQAEFKFJEEHSQRIBCGCNQFIEETKFNELLSGIREBGMCOLGKDRELCPSSIMCNMRKSEKOHHIRGTCTQFBHJHNNKRADCTFECGNJJJBTCSBRTFKKNMKFJMIBDPKLJKLGLJEBQMGGHABDKTEFLANFOLKGSDMKLBSMDERSMBDESBOARMLEAESBTDIRTGKQECDCDPNABPITCIQBSRMHBJSCBBFTFHJMEQNMLIDPGGEMQRREOFNOCPQBFMNKBHLQGJBGLMDDNALEAJDLBBFNDRAEIFF"
# str1 = "ABCDGH"
# str2 = "AEDFHR"
# str1 = "ABC"
# str2 = "AC"
n = len(str1)
m = len(str2)

# Brute Force -- Recursive
def LCS(str1, str2, n, m):
    if n == 0 or m == 0:
        return 0
    if str1[n-1] == str2[m-1]:
        return 1 + LCS(str1, str2, n-1, m-1)
    else:
        return max(LCS(str1, str2, n-1, m), LCS(str1, str2, n, m-1))

# print(LCS(str1, str2, n, m))

# Top Down -- Memoization
t = []
for _ in range(n+1):
    t.append([-1]*(m+1))

def LCS_memo(str1, str2, n, m):
    if n == 0 or m == 0:
        return 0
    if t[n][m] != -1:
        return t[n][m]
    if str1[n-1] == str2[m-1]:
        t[n][m] = 1 + LCS_memo(str1, str2, n-1, m-1)
    else:
        t[n][m] = max(LCS_memo(str1, str2, n-1, m), LCS_memo(str1, str2, n, m-1))
    return t[n][m]

# print(LCS_memo(str1, str2, n, m))

# Bottom Up
def LCS_Tablular(str1, str2, n, m):
    t = [[-1 for _ in range(m+1)] for __ in range(n+1)]
    for i in range(0, n+1):
        t[i][0] = 0
    for j in range(0, m+1):
        t[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    
    # Printing LCS
    i = n 
    j = m
    lcs = ""
    while(i > 0 and j > 0):
        if str1[i-1] == str2[j-1]:
            lcs += str1[i-1]
            i-=1
            j-=1
        else:
            if t[i-1][j] > t[i][j-1]:
                i-=1
            else:
                j-=1
        
    print(lcs[::-1])
    return t[n][m]

print(LCS_Tablular(str1, str2, n, m))