n = int(input())
schedules = [list(input().split()) for _ in range(n)]
schedules = sorted(schedules, key=lambda x: (int(x[1]), int(x[2]), int(x[3]), x[0]))
for i in schedules:
    print(i[0])