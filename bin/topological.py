def topological_sort(graf, prec):
    in_edge = prec
    result_in_one_line = []
    result_by_semester = []

    def sort():
        remove = []
        semester = []
        for i in in_edge:
            if(in_edge[i] == 0):
                result_in_one_line.append(i)
                remove.append(i)
                semester.append(i)
                for j in graf.getedge():
                    if(j[0] == i):
                            in_edge[j[1]] -= 1
                        
        for k in remove:
            del in_edge[k]

        result_by_semester.append(semester)
        return

    while(in_edge) : sort()
    return result_in_one_line, result_by_semester

def printSchedule(schedule):
    print("Rencana Kuliah : ")
    print("-----------------")
    for semester in range(len(schedule)):
        print("Semester " + str(semester) + " : ", end='')
        for course in range(len(schedule[semester])):
            print(schedule[semester][course], end='')
            if(course != len(schedule[semester])-1):
                print(", ", end='')

        print()
    print("-----------------")

    return
