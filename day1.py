import os

def part1(filename):

    # TODO - implement the right thing

    # read file
    # file1 = open('data/day1.txt', 'r')
    with open(filename, 'r') as file1:
        depths = file1.read().splitlines()

        # work something out
    prev_depth = depths[0]
    count = 0
    # matches = []
    # matches_before = []
    for depth in depths[1:]:
        if float(depth) > float(prev_depth):
            count += 1
            # match = (prev_depth,depth)
            # matches.append(match)

        # if depth > prev_depth:
        #     count += 1
        #     match = (prev_depth,depth)
        #     matches_before.append(match)

        prev_depth = depth

    # difference = list(set(matches) - set(matches_before))
    print(count)
    return count




    # answer = 300
    # print(answer)
    # return answer