import sys

def factorize_nums(numbers):
	factors = []
	for num in numbers:
		fact_bool = False
		for i in range(2, int(int(num) / 2) + 1):
			if int(num) % i == 0:
				factors.append((i, int(int(num) / i)))
				fact_bool = True
				break
		if not fact_bool:
			factors.append((1, num))
	return factors


def factorize_file():
	num_list = []
	file_name = sys.argv[1]
	with open(file_name) as file:
		data = file.readlines()
		for line in data:
			num_list.append(line.strip())

	results = factorize_nums(num_list)

	full = dict(zip(num_list, results))
	for k, v in full.items():
		print("{}={}*{}".format(k, v[0], v[1]))

factorize_file()
