# problem : 2

def slot_consideration(givne_interval):

    givne_interval.sort()

    result = []

    for first_time, last_time in givne_interval:

        if not result or first_time > result[-1][1]:
            result.append([first_time, last_time])

        else:
            result[-1][1] = max(result[-1][1], last_time)

    return result


n = int(input())

givne_interval = []

for i in range(n):
    start, end = map(int, input().split())
    givne_interval.append([start, end])


result = slot_consideration(givne_interval)



for start, end in result:
    print(start, end)
