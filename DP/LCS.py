

def LCS(A,B):
    if len(A) <= 0 or len(B) <= 0:
        return 0
    else:
        if A[0] == B[0]:
            return 1 + LCS(A[1:],B[1:])
        else:
            subseq = max( LCS(A[1:],B) , LCS(A,B[1:]) )
            return subseq
    

A = "ABCBDAB"
B = "BDCABA"
print(LCS(A,B))