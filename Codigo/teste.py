with open('index.txt', 'r') as f:
    ws, hs = [int(x) for x in next(f).split(',')]
    we, he = [int(x) for x in next(f).split(',')]
    start = [ws,hs]
    end = [we,he]
    l = [[int(num) for num in line.split(',')] for line in f]

print(start)
print(end)
print(l)