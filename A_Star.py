#Made by Jason Melnik

def A_star(cords1, cords2):

    #creates the list that holds all possible or not paths to cords2
    biglist = []

    #adding the first point to the biglist
    list1 = [cords1]
    biglist.append(list1)

    #This will hold the shortest distance
    final_list = []

    #This will make sure we get the lowest path
    min = 1000000

    for i in range(6):
        for i in range(len(biglist)):
            temp = biglist[i]
            #So basicly it copy the list that we are on (biglist[i]) then
            list1 = biglist[i].copy()
            #We create the next cord witch could be any of the 8 directions but this one is in the x direction
            cord1 = (biglist[i][-1][0] + 1, biglist[i][-1][1])
            #then we add the cord to the list1 making a new path that is different from the rest
            list1.append(cord1)

            list2 = biglist[i].copy()
            cord2 = (biglist[i][-1][0] - 1, biglist[i][-1][1])
            list2.append(cord2)

            list3 = biglist[i].copy()
            cord3 = (biglist[i][-1][0], biglist[i][-1][1] + 1)
            list3.append(cord3)

            list4 = biglist[i].copy()
            cord4 = (biglist[i][-1][0], biglist[i][-1][1] - 1)
            list4.append(cord4)

            list5 = biglist[i].copy()
            cord5 = (biglist[i][-1][0] + 1, biglist[i][-1][1] + 1)
            list5.append(cord5)

            list6 = biglist[i].copy()
            cord6 = (biglist[i][-1][0] + 1, biglist[i][-1][1] - 1)
            list6.append(cord6)

            list7 = biglist[i].copy()
            cord7 = (biglist[i][-1][0] - 1, biglist[i][-1][1] - 1)
            list7.append(cord7)

            list8 = biglist[i].copy()
            cord8 = (biglist[i][-1][0] - 1, biglist[i][-1][1] + 1)
            list8.append(cord8)

            #this will make sure we dont get duplicates
            cord1Bool = False
            cord2Bool = False
            cord3Bool = False
            cord4Bool = False
            cord5Bool = False
            cord6Bool = False
            cord7Bool = False
            cord8Bool = False

            #This will test if the cord is allowed or not
            for i in range(len(canttouch)):
                if cord1 == canttouch[i]:
                    cord1Bool = True
                if cord2 == canttouch[i]:
                    cord2Bool = True
                if cord3 == canttouch[i]:
                    cord3Bool = True
                if cord4 == canttouch[i]:
                    cord4Bool = True
                if cord5 == canttouch[i]:
                    cord5Bool = True
                if cord6 == canttouch[i]:
                    cord6Bool = True
                if cord7 == canttouch[i]:
                    cord7Bool = True
                if cord8 == canttouch[i]:
                    cord8Bool = True

            #Now if a cord is allowed to enter the biglist this is where it gets added. So now the biglist has all
            #eight new paths
            if cord1Bool == False:
                biglist.append(list(list1))
            if cord2Bool == False:
                biglist.append(list(list2))
            if cord3Bool == False:
                biglist.append(list(list3))
            if cord4Bool == False:
                biglist.append(list(list4))
            if cord5Bool == False:
                biglist.append(list(list5))
            if cord6Bool == False:
                biglist.append(list(list6))
            if cord7Bool == False:
                biglist.append(list(list7))
            if cord8Bool == False:
                biglist.append(list(list8))

            #Then we remove the old list from the biglist to prevent overflow
            biglist.remove(temp)

            #Now we will test if that cord we determined on top is the one we need.
            #we also tests its length to determine a new minimum and add it to the final list if its
            #smaller that the other paths
            if cord1 == cords2 and len(list1) < min:
                min = len(list1)
                final_list = []
                final_list.append(list1)
            if cord2 == cords2 and len(list2) < min:
                min = len(list2)
                final_list = []
                final_list.append(list2)
            if cord3 == cords2 and len(list3) < min:
                min = len(list3)
                final_list = []
                final_list.append(list3)
            if cord4 == cords2 and len(list4) < min:
                min = len(list4)
                final_list = []
                final_list.append(list4)
            if cord5 == cords2 and len(list5) < min:
                min = len(list5)
                final_list = []
                final_list.append(list5)
            if cord6 == cords2 and len(list6) < min:
                min = len(list6)
                final_list = []
                final_list.append(list6)
            if cord7 == cords2 and len(list7) < min:
                min = len(list7)
                final_list = []
                final_list.append(list7)
            if cord8 == cords2 and len(list8) < min:
                min = len(list8)
                final_list = []
                final_list.append(list8)
    #returns the shortest path :)
    return (final_list)

#These are the variables we want our path to go around
canttouch = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]#These cords show a verticle line

print ("Running program...")

print("Going around a verticle line:")
print (A_star((0, 2), (2, 2)))

canttouch = [(-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1)]#These cords show a horizontal line
print("Going around a horizontal line:")
print (A_star((0, 0), (0, 2)))


