import Techniovision


def inside_contest(faculty, file_name):
    f = open(file_name, 'r')
    votes = []
    for line in f:
        splitted_line = line.split()
        if splitted_line[0] == 'staff' and splitted_line[-1] == faculty:
            splitted_line = splitted_line[2:-1]
            for e in splitted_line:
                votes.append([e, 0])
            votes[0][1] = 20
            break
    students = []
    f.close()
    f = open(file_name, 'r')
    for line in f:
        splitted_line = line.split()
        if splitted_line[0] == 'inside' and splitted_line[-1] == faculty:
            if splitted_line[2] in students:
                students.append(splitted_line[2])
                for e in votes:
                    if e[0] == splitted_line[3]:
                        e[1] += 1
                        break
    f.close()
    index = 0
    for i, e in enumerate(votes):
        if e[1] > votes[index][1]:
            index = i
    return votes[index][0]


file = open('input.txt', 'r')
contest_list = []
for line in file:
    splitted_line = line.split()
    if splitted_line[0] == 'staff':
        program = inside_contest(splitted_line[-1], 'input.txt')
        contest_list.append([splitted_line[-1], program])
t = Techniovision.TechniovisionCreate()
file.close()
file = open('input.txt', 'r')
for line in file:
    splitted_line = line.split()
    if splitted_line[0] == 'techniovision':
        for e in contest_list:
            if e[1] == splitted_line[2]:
                Techniovision.TechniovisionStudentVotes(t, int(splitted_line[1]), str(splitted_line[-1]), str(e[0]))
                break
Techniovision.TechniovisionWinningFaculty(t)
Techniovision.TechniovisionDestroy(t)
file.close()

















