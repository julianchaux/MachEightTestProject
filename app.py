import sys

def checkSumPair(numbers, total_sum):
    d = {}
    result = []

    for i in range(len(numbers)):
        if total_sum - numbers[i] in d.keys():
            result.append((numbers[d[total_sum - numbers[i]]], numbers[i]))

        d[numbers[i]] = i
    return result

if __name__ == "__main__":
    try:
        numbers = [int(x) for x in sys.argv[1].split(",")]
        total_sum = int(sys.argv[2])
        output = checkSumPair(numbers, total_sum)
        print(output)
    except ValueError:
        print("Please, enter only non-equal integers...")