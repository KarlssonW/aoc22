def main():
    f = open("./input.txt", "r")

    sum = 0
    maxsum = 0

    for l in f:
        if l == "\n":
            maxsum = max(sum, maxsum)
            sum = 0
        else:
            sum += int(l)

    print(maxsum)

if __name__ == "__main__":
    main()