VISITED, UNVISITED = 1, 0

def topological_sort(graf, prec):
    in_edge = prec
    result_in_one_line = []
    result_by_semester = []

    def sort():
        state = {}
        remove = []
        semester = []
        for i in in_edge:
            if(in_edge[i] == 0 and (i not in state)):
                result_in_one_line.append(i)
                remove.append(i)
                semester.append(i)
                for j in graf.getedge():
                    if(j[0] == i):
                            in_edge[j[1]] -= 1
                            state[j[1]] = VISITED
                        
        for k in remove:
            del in_edge[k]

        result_by_semester.append(semester)
        return

    while(has_zero(in_edge)) :
        sort()
    
    return result_in_one_line, result_by_semester

def has_zero(prec):
    for i in prec:
        if(prec[i] == 0):
            return True
    else: return False

def printSchedule(schedule):
    print("Rencana Kuliah : ")
    print("-----------------")
    if(schedule != []):
        for semester in range(len(schedule)):
            if(semester > 8):
                break
            print("Semester " + str(semester + 1) + " : ", end='')
            for course in range(len(schedule[semester])):
                print(schedule[semester][course], end='')
                if(course != len(schedule[semester])-1):
                    print(", ", end='')

            print()
    print("-----------------")
    return
