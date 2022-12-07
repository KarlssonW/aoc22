n = 14

def main():
    with open("./input.txt", "r") as stream:
        stream = stream.read()
        for i in range(len(stream)):
            if len(list(set(stream[i:i+n]))) >= n:
                print(i+n)
                return 0

if __name__ == "__main__":
    main()