import random
import statistics

l = [2,4,5,6,8,9]
print('Mean :', statistics.mean(l))
print('Std Dev :', statistics.stdev(l))
print()
gen = ([random.choice(l) for i in range(len(l))] for j in range(10000))

lst = []
for sample in gen:
    lst.append(format(sum(sample)/len(sample), '.2f'))

sample_means = list(map(float, lst))
# print('Sample Means :', sample_means)
print('Mean of means:', statistics.mean(sample_means))
print('Std error (std dev of means) :', statistics.stdev(sample_means))