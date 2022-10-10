import sys

def checkSumPair(numbers, total_sum):
    i = 0
    for n in numbers:
        sum_result = {total_sum - n}
        v1 = set(numbers).intersection(sum_result)
        if v1:
            numbers.pop(i)
            numbers.remove(*v1)
            print(n, *v1)
        i+=1

if __name__ == "__main__":

    try:
        numbers = [ int(x) for x in sys.argv[1].split(",")]
        total_sum = int(sys.argv[2])
        checkSumPair(numbers, total_sum)
    except ValueError:
        print("Please, enter only non-equal integers...")