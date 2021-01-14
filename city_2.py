import re

def read_file_dfs(file, a, b):
    b_found = False
    distance = 0
    match_a = str(a)
    match_b = str(b)
    second = ""
    i = 0
    with open(file) as open_file:

        # Store contents of file in Dictionary
        d = {}
        for line in open_file:
            x = line.split()
            if len(x) < 3:
                continue
            (key, val, aa) = line.split()
            d[int(key)] = [int(val), int(aa)]


        def dfs(r, c):
            pass




        #f = open_file.readlines()
        """
        while i < 100000 and  a != b:
            print("a: ", a, "b: ", d[a], "dist: ", d[a][1])
            distance += d[a][1]
            a = d[a][0]
            print(a,b)
            #print(distance, a)
            i += 1   
        print(distance)
        """


        #for key, value in d.items():
        #    print(key, value[1]))

        #print(d[876500321][1])





class 


if __name__ == '__main__':
    read_file_dfs("citymapper-coding-test-graph.dat", 876500321, 1524235806)