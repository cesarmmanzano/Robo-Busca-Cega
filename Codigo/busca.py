def readFile():

	with open('index.txt', 'r') as f:
		ws, hs = [int(x) for x in next(f).split(',')]
		we, he = [int(x) for x in next(f).split(',')]
		start = [ws,hs]
		end = [we,he]
		l = [[int(num) for num in line.split(',')] for line in f]
		
	result = []
	result.append(start)
	result.append(end)
	result.append(l)

	return result

def main(win, width):

	file = readFile()
	initialPosition = file[0]
	finalPosition = file[1]
	
main()