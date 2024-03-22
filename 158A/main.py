def I():
    return list(map(int, input().split()))

a, b = I()

ans = 0

score = I()

for idx, i in enumerate(score):

    if idx > b-1 and i > 0:
        if i < score[b-1]:
            # print('*')
            print(ans)
            break
        else:
            ans += 1

    else:
        if i > 0:
            ans += 1
        else:
            # print('**')
            print(ans)
            break
else:
    # print('***')
    print(ans)