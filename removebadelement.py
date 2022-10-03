for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split(' ')))
    d={}
    for i in a:
        d[i]=a.count(i)
    d=dict(sorted(d.items(), key=lambda item: item[1]))
    p=max(d,key=lambda x:d[x])
    ans=0
    for k,v in d.items():
        if k!=p:
            ans+=v
    print(ans)
