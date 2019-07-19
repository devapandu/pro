from itertools import combinations
S,u=map(int,input().split())
l=len(str(S))
lst=list(combinations(str(S),l-u))
lst=sorted(lst)
print(*lst[0],sep='')
