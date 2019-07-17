loop  = int(input())
for i in range(loop):
    inp = input()
    leng = len(inp)
    if inp == inp[::-1]:
        print(-1)
    else:
        for i in range(len(inp)//2+1):
            if inp[(leng-1)-i]!= inp[i]:
                if inp[:i]+inp[i+1:] == (inp[:i]+inp[i+1:])[::-1]:
                    print(i)
                    break
                elif inp[:(leng-1)-i]+inp[(leng-1)-i+1:] == (inp[:(leng-1)-i]+inp[(leng-1)-i+1:])[::-1]:
                    print((leng-1)-i)
                    break
                else:
                    print(-1)
                    break