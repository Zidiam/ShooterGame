#Made by Jason Melnik
import pygame, os, random, math, time
#Player Object:
def A_star(cords1, cords2):
    canttouch = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]  # These cords show a verticle line
    for i in range(len(canttouch)):
        Dot_List.add(Dot(canttouch[i], (0, 0, 0)))
    Color = (150, 0, 150)
    #creates the list that holds all possible or not paths to cords2
    biglist1 = []

    #adding the first point to the biglist
    list1 = [cords1]
    biglist1.append(list1)

    #This will hold the shortest distance
    final_list = []

    #This will make sure we get the lowest path
    min = 1000000

    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 500, 500))
    pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 500))
    pygame.draw.line(screen, (0, 0, 0), (0, 250), (500, 250))

    for x in range(100000):
        for i in range(len(biglist1)):
            testcord = biglist1[i][-1]
            for t in range(1, len(biglist1)):
                try:
                    if biglist1[t][-1] == testcord:
                        biglist1.remove(biglist1[t])
                except:
                    continue
            print (i)
            print (biglist1[i])
            if len(biglist1[i]) > x:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                temp = biglist1[i]
                # So basicly it copy the list that we are on (biglist1[i]) then
                list1 = biglist1[i].copy()
                # We create the next cord witch could be any of the 8 directions but this one is in the x direction
                cord1 = (biglist1[i][-1][0] + 1, biglist1[i][-1][1])
                # then we add the cord to the list1 making a new path that is different from the rest
                list1.append(cord1)

                list2 = biglist1[i].copy()
                cord2 = (biglist1[i][-1][0] - 1, biglist1[i][-1][1])
                list2.append(cord2)

                list3 = biglist1[i].copy()
                cord3 = (biglist1[i][-1][0], biglist1[i][-1][1] + 1)
                list3.append(cord3)

                list4 = biglist1[i].copy()
                cord4 = (biglist1[i][-1][0], biglist1[i][-1][1] - 1)
                list4.append(cord4)

                list5 = biglist1[i].copy()
                cord5 = (biglist1[i][-1][0] + 1, biglist1[i][-1][1] + 1)
                list5.append(cord5)

                list6 = biglist1[i].copy()
                cord6 = (biglist1[i][-1][0] + 1, biglist1[i][-1][1] - 1)
                list6.append(cord6)

                list7 = biglist1[i].copy()
                cord7 = (biglist1[i][-1][0] - 1, biglist1[i][-1][1] - 1)
                list7.append(cord7)

                list8 = biglist1[i].copy()
                cord8 = (biglist1[i][-1][0] - 1, biglist1[i][-1][1] + 1)
                list8.append(cord8)

                # this will make sure we dont get duplicates
                cord1Bool = False
                cord2Bool = False
                cord3Bool = False
                cord4Bool = False
                cord5Bool = False
                cord6Bool = False
                cord7Bool = False
                cord8Bool = False

                # This will test if the cord is allowed or not
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

                for i in range(len(temp)):
                    if cord1 == temp[i]:
                        cord1Bool = True
                    if cord2 == temp[i]:
                        cord2Bool = True
                    if cord3 == temp[i]:
                        cord3Bool = True
                    if cord4 == temp[i]:
                        cord4Bool = True
                    if cord5 == temp[i]:
                        cord5Bool = True
                    if cord6 == temp[i]:
                        cord6Bool = True
                    if cord7 == temp[i]:
                        cord7Bool = True
                    if cord8 == temp[i]:
                        cord8Bool = True

                for i in range(len(biglist1)):
                    for x in range(len(biglist1[i])):
                        if cord1 == biglist1[i][x]:
                            cord1Bool = True
                        if cord2 == biglist1[i][x]:
                            cord2Bool = True
                        if cord3 == biglist1[i][x]:
                            cord3Bool = True
                        if cord4 == biglist1[i][x]:
                            cord4Bool = True
                        if cord5 == biglist1[i][x]:
                            cord5Bool = True
                        if cord6 == biglist1[i][x]:
                            cord6Bool = True
                        if cord7 == biglist1[i][x]:
                            cord7Bool = True
                        if cord8 == biglist1[i][x]:
                            cord8Bool = True

                # Now if a cord is allowed to enter the biglist1 this is where it gets added. So now the biglist1 has all
                # eight new paths
                if Color[0] < 200:
                    Color = (Color[0] + 1, 0, 0)
                elif Color[1] < 240:
                    Color = (200, Color[1] + 1, 0)
                elif Color[2] < 240:
                    Color = (200, 240, Color[2] + 1)
                elif Color == (200, 240, 240):
                    Color = (150, 0, 150)

                if cord1Bool == False:
                    biglist1.append(list(list1))
                    Dot_List.add(Dot(cord1, Color))
                if cord2Bool == False:
                    biglist1.append(list(list2))
                    Dot_List.add(Dot(cord2, Color))
                if cord3Bool == False:
                    biglist1.append(list(list3))
                    Dot_List.add(Dot(cord3, Color))
                if cord4Bool == False:
                    biglist1.append(list(list4))
                    Dot_List.add(Dot(cord4, Color))
                if cord5Bool == False:
                    biglist1.append(list(list5))
                    Dot_List.add(Dot(cord5, Color))
                if cord6Bool == False:
                    biglist1.append(list(list6))
                    Dot_List.add(Dot(cord6, Color))
                if cord7Bool == False:
                    biglist1.append(list(list7))
                    Dot_List.add(Dot(cord7, Color))
                if cord8Bool == False:
                    biglist1.append(list(list8))
                    Dot_List.add(Dot(cord8, Color))

                # Then we remove the old list from the biglist1 to prevent overflow

                del biglist1[0]

                # Now we will test if that cord we determined on top is the one we need.
                # we also tests its length to determine a new minimum and add it to the final list if its
                # smaller that the other paths
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
            else:
                biglist1.remove(biglist1[i])

            Dot_List.draw(screen)
            pygame.display.update()

    #returns the shortest path :)
    global StartOver
    StartOver = True
    for i in range(len(final_list[0])):
        Dot_List.add(Dot(final_list[0][i], (0, 250, 0)))

    Dot_List.draw(screen)
    pygame.display.update()

class Dot(pygame.sprite.Sprite):
    def __init__(self, cords, color):
        x = int(cords[0]) * 10
        y = int(cords[1]) * 10
        x = x + 250
        y = 250 - y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (5, 5), 5)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

screen = pygame.display.set_mode((500, 500), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("A_Star")
gameover = False
Dot_List = pygame.sprite.Group()
Start_Cord = input("Start Cord: ")
Start_Cord = Start_Cord.split(", ")
Start_Cord = int(Start_Cord[0]), int(Start_Cord[1])
End_Cord = input("End Cord: ")
End_Cord = End_Cord.split(", ")
End_Cord = int(End_Cord[0]), int(End_Cord[1])
Dot_List.add(Dot(Start_Cord, (255, 0, 0)))
Dot_List.add(Dot(End_Cord, (255, 0, 0)))
global StartOver
StartOver = False

while gameover == False:
    for event in pygame.event.get():  # This code is to see what keys you press and input them into name
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # If you click enter it jumps to the game if theres no one in the list that has that name
                if StartOver == True:
                    Dot_List = pygame.sprite.Group()
                    Color = (0, 0, 0)
                    Start_Cord = input("Start Cord: ")
                    Start_Cord = Start_Cord.split(", ")
                    Start_Cord = int(Start_Cord[0]), int(Start_Cord[1])
                    End_Cord = input("End Cord: ")
                    End_Cord = End_Cord.split(", ")
                    End_Cord = int(End_Cord[0]), int(End_Cord[1])
                    dot = Dot(Start_Cord, (255, 0, 0))
                    Dot_List.add(dot)
                    dot = Dot(End_Cord, (255, 0, 0))
                    Dot_List.add(dot)
                    StartOver = False
    if StartOver == False:
        A_star(Start_Cord, End_Cord)

