
import re





def read_file(file, a, b):
    b_found = False
    distance = 0
    match_a = str(a)
    match_b = str(b)
    second = ""
    i = 0
    with open(file) as open_file:
        f = open_file.readlines()
        while i < len(f):
            
            if f[i].startswith(match_a):
                #print("this is f[i]", f[i])
                splitter = f[i].split()
                #print(splitter)
                if len(splitter) < 3:
                    i += 1
                    continue
                #match_a = splitter[0]
                match_a = splitter[1]
                distance += int(splitter[2])
                print("a: ", match_a, "second: ", second, "distance: ", distance)
            i += 1
        print("Final Distance: ", distance)


        """
        for line in open_file:
            splitter = line.split()
            if line.startswith(match_a):
                
                if len(splitter) < 3:
                    continue
                a = splitter[0]
                second = splitter[1]
                distance += int(splitter[2])
            elif line.startswith(second):
                b_found = True
                break
        """
                






if __name__ == '__main__':
    read_file("citymapper-coding-test-graph.dat", 876500321, 1524235806)



# regex
                #print(splitter)
                #for i in splitter:
                #    print(i)
                #print(splitter[1])
                #search = re.search(r'\s+', line)

            #    search_for_b = re.search(r'\s+([^ -.]*)', line)
            #    print(search_for_b)
            #    if search_for_b == str(b):
            #        b_found = True