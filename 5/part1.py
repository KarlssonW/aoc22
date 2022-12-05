import re

def main():
    with open("./input.txt", "r") as puzzle_input:
        puzzle_input = puzzle_input.read().splitlines()
        
        stacks = []
        for i in range((len(puzzle_input[0])+1)//4):
            stacks.append([])
        
        while puzzle_input[0] != "":
            for n, i in enumerate(range(1,len(puzzle_input[0]), 4)):
                if puzzle_input[0][i] != ' ':
                    stacks[n].insert(0, puzzle_input[0][i])
            puzzle_input.pop(0)
        
        for stack in range(len(stacks)): stacks[stack] = stacks[stack][1:] 
        
        for instruction in puzzle_input[1:]:
            move = list(map(int, re.findall("[0-9]+", instruction)))
            for _ in range(move[0]):
                stacks[move[2]-1].append(stacks[move[1]-1].pop())
                
        out = ""
        for stack in stacks: out += stack[-1]
        print(out)

if __name__ == "__main__":
    main()