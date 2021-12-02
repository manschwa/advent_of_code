print("                      *                      ")
print("                    *****                    ")
print("                  *********                  ")
print("                *************                ")
print("             Advent of Code 2021             ")
print("           ***********************           ")
print("         **  Day 01: Sonar Sweep  **         ")
print("       *******************************       ")
print("     ***********************************     ")
print("                     ***                     ")
print("                     ***                     ")

filename = "01.input"
increase_cnt = -1
decrease_cnt = 0
previous_val = 0

with open(filename) as file:
    for line in file:
        if(int(line) > previous_val):
            increase_cnt += 1
        elif(int(line) < previous_val):
            decrease_cnt += 1
        previous_val = int(line)

print()
print("Seafloor increased {} and decreased {} times".format(increase_cnt, decrease_cnt))
print()

STEPS = 3
step_cnt = 0    # list index
increase_cnt = -3
decrease_cnt = 0
cluster_values = [0, 0, 0]

# 0  199  A                 [0, 199, 199],   cnt =-2, [199, 199, 199]
# 1  200  A B               [199, 199, 399], cnt =-1, [399, 200, 399]
# 2  208  A B C             [607, 200, 399], cnt = 0, [607, 408, 208]
# 0  210    B C A           [607, 618, 208], cnt = 1, [210, 618, 418]
# 1  200      C A B         [210, 618, 618], ------ , [410, 200, 618]
# 2  207        A B C       [617, 200, 618], ------ , [617, 407, 207]
# 0  240          B C A     [617, 647, 207], cnt = 2, [240, 647, 447]
# 1  269            C A B   [240, 647, 716], cnt = 3, [509, 269, 716]
# 2  260              A B   [769, 269, 716], cnt = 4, [769, 529, 260]
# 0  263                B   [769, 792, 260], cnt = 5, [263, 792, 523]

with open(filename) as file:
    for line in file:
        step = step_cnt % STEPS
        match step:
            case 0:
                cluster_values[1] += int(line)
                if(cluster_values[1] > cluster_values[0]):
                    increase_cnt += 1
                elif(cluster_values[1] < cluster_values[0]):
                    decrease_cnt += 1
                cluster_values[2] += int(line)
                cluster_values[0] = 0
                cluster_values[0] += int(line)
            case 1:
                cluster_values[2] += int(line)
                if(cluster_values[2] > cluster_values[1]):
                    increase_cnt += 1
                elif(cluster_values[2] < cluster_values[1]):
                    decrease_cnt += 1
                cluster_values[0] += int(line)
                cluster_values[1] = 0
                cluster_values[1] += int(line)
            case 2:
                cluster_values[0] += int(line)
                if(cluster_values[0] > cluster_values[2]):
                    increase_cnt += 1
                elif(cluster_values[0] < cluster_values[2]):
                    decrease_cnt += 1
                cluster_values[1] += int(line)
                cluster_values[2] = 0
                cluster_values[2] += int(line)
        step_cnt += 1

print("{}-step cluster: Seafloor increased {} and decreased {} times".format(STEPS, increase_cnt, decrease_cnt))
print()
