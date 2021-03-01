# MADE BY : 16519045 / M. Reyhanullah Budiaman
#
# This is a simple program for solving topological sort 
# for making course schedule

def readfile(file_name):
    cd_file = open(("../test/" + file_name), 'r')
    matkul = cd_file.readlines()
    arr_of_course = []

    for i in range(len(matkul)):
        arr_of_course.append(matkul[i].replace("\n", "").replace(".","").replace(" ",""))

    return arr_of_course

def getPrecDict(course):
    '''Get all preRec from course and returning it with dictionary representation.'''
    prec = {}
    
    for i in range(len(course)):
        deskripsi = course[i].split(",")
        key = deskripsi[0]
        deskripsi.remove(key)
        prec[key] = deskripsi
        
    return prec

def create_graf(prec):
    graf = {}
    for course in prec:
        graf[course] = []

    in_node = {}
    for course in prec:
        for i in prec[course]:
            graf[i].append(course)
        in_node[course] = len(prec[course])


    return graf, in_node

VISITED, UNVISITED = 1, 0

def topological_alt(graf1):
    graf, in_node = create_graf(graf1)
    res = []

    def sort():
        remove = []
        for i in in_node:
            if(in_node[i] == 0):
                res.append(i)
                remove.append(i)
                for j in graf[i]:
                    in_node[j] -= 1
                        
        for k in remove:
            del in_node[k]

        return
    
    while(in_node) : sort()
    return res
    

'''
def topological_sort(graf):
    result = []
    path = set(graf)
    state = {}

    def search_end_node(node):
        state[node] = VISITED
        if(graf[node] != []):
            for i in graf[node]:
                print(graf[node])
                if(state.get(i, None) == VISITED):
                    raise ValueError("Terbentuk Sirkuit")
                else:
                    path.discard(i)
                    print(i, "---------" ,path)
                    search_end_node(i)
        #reach deepest node/no exit edge left
        if((node in result) == False):
            result.append(node)
        state[node] = UNVISITED

    while path:
        search_end_node(path.pop())
    return result[::-1]
''' 
    
# BELOW HERE IS FOR TESTING PURPOSE
tess = readfile("contoh2.txt")
tst1 = create_graf(getPrecDict(tess))
tst2 = getPrecDict(tess)
print(topological_alt(tst2))
#try:
 #   print(topological_sort(tst1))
#except ValueError:
 #   print("Tidak dapat dibuat jadwal matakuliah")

# {'C1': ['C2', 'C4'], 'C2': ['C5'], 'C3': ['C1', 'C4'], 'C4': ['C2', 'C5'], 'C5': []}

# ALTERNATIF SOLUSI
# ['C3', 'C1', 'C4', 'C2', 'C5']
