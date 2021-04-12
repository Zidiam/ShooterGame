import pygame

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

def A_Star(start_cord, end_cord):
    global Color
    global biglist
    global canttouch
    for z in range(len(biglist)):
        if Color[0] < 200:
            Color = (Color[0] + 1, 0, 0)
        elif Color[1] < 240:
            Color = (200, Color[1] + 1, 0)
        elif Color[2] < 240:
            Color = (200, 240, Color[2] + 1)
        elif Color == (200, 240, 240):
            Color = (150, 0, 150)

        cord1 = biglist[z][-1][0] + 1, biglist[z][-1][1]
        cord2 = biglist[z][-1][0] - 1, biglist[z][-1][1]
        cord3 = biglist[z][-1][0], biglist[z][-1][1] + 1
        cord4 = biglist[z][-1][0], biglist[z][-1][1] - 1
        cord5 = biglist[z][-1][0] + 1, biglist[z][-1][1] + 1
        cord6 = biglist[z][-1][0] + 1, biglist[z][-1][1] - 1
        cord7 = biglist[z][-1][0] - 1, biglist[z][-1][1] + 1
        cord8 = biglist[z][-1][0] - 1, biglist[z][-1][1] - 1

        cord1_Safe = True
        cord2_Safe = True
        cord3_Safe = True
        cord4_Safe = True
        cord5_Safe = True
        cord6_Safe = True
        cord7_Safe = True
        cord8_Safe = True

        for ind in range(len(canttouch)):
            if canttouch[ind] == cord1:
                cord1_Safe = False
            if canttouch[ind] == cord2:
                cord2_Safe = False
            if canttouch[ind] == cord3:
                cord3_Safe = False
            if canttouch[ind] == cord4:
                cord4_Safe = False
            if canttouch[ind] == cord5:
                cord5_Safe = False
            if canttouch[ind] == cord6:
                cord6_Safe = False
            if canttouch[ind] == cord7:
                cord7_Safe = False
            if canttouch[ind] == cord8:
                cord8_Safe = False

        for t in range(len(biglist)):
            for x in range(len(biglist[t])):
                if biglist[t][x] == cord1:
                    cord1_Safe = False
                if biglist[t][x] == cord2:
                    cord2_Safe = False
                if biglist[t][x] == cord3:
                    cord3_Safe = False
                if biglist[t][x] == cord4:
                    cord4_Safe = False
                if biglist[t][x] == cord5:
                    cord5_Safe = False
                if biglist[t][x] == cord6:
                    cord6_Safe = False
                if biglist[t][x] == cord7:
                    cord7_Safe = False
                if biglist[t][x] == cord8:
                    cord8_Safe = False

        list1 = biglist[z].copy()
        list2 = biglist[z].copy()
        list3 = biglist[z].copy()
        list4 = biglist[z].copy()
        list5 = biglist[z].copy()
        list6 = biglist[z].copy()
        list7 = biglist[z].copy()
        list8 = biglist[z].copy()

        del biglist[0]

        if cord1_Safe == True:
            list1.append(cord1)
            biglist.append(list1)
            Dot_List.add(Dot(cord1, Color))
        if cord2_Safe == True:
            list2.append(cord2)
            biglist.append(list2)
            Dot_List.add(Dot(cord2, Color))
        if cord3_Safe == True:
            list3.append(cord3)
            biglist.append(list3)
            Dot_List.add(Dot(cord3, Color))
        if cord4_Safe == True:
            list4.append(cord4)
            biglist.append(list4)
            Dot_List.add(Dot(cord4, Color))
        if cord5_Safe == True:
            list5.append(cord5)
            biglist.append(list5)
            Dot_List.add(Dot(cord5, Color))
        if cord6_Safe == True:
            list6.append(cord6)
            biglist.append(list6)
            Dot_List.add(Dot(cord6, Color))
        if cord7_Safe == True:
            list7.append(cord7)
            biglist.append(list7)
            Dot_List.add(Dot(cord7, Color))
        if cord8_Safe == True:
            list8.append(cord8)
            biglist.append(list8)
            Dot_List.add(Dot(cord8, Color))

        if cord1 == end_cord:
            for i in range(len(list1)):
                Dot_List.add(Dot(list1[i], (0, 250, 0)))
            return True
        if cord2 == end_cord:
            for i in range(len(list2)):
                Dot_List.add(Dot(list2[i], (0, 250, 0)))
            return True
        if cord3 == end_cord:
            for i in range(len(list3)):
                Dot_List.add(Dot(list3[i], (0, 250, 0)))
            return True
        if cord4 == end_cord:
            for i in range(len(list4)):
                Dot_List.add(Dot(list4[i], (0, 250, 0)))
            return True
        if cord5 == end_cord:
            for i in range(len(list5)):
                Dot_List.add(Dot(list5[i], (0, 250, 0)))
            return True
        if cord6 == end_cord:
            for i in range(len(list6)):
                Dot_List.add(Dot(list6[i], (0, 250, 0)))
            return True
        if cord7 == end_cord:
            for i in range(len(list7)):
                Dot_List.add(Dot(list7[i], (0, 250, 0)))
            return True
        if cord8 == end_cord:
            for i in range(len(list8)):
                Dot_List.add(Dot(list8[i], (0, 250, 0)))
            return True

    return False
screen = pygame.display.set_mode((500, 500), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("A_Star")

Dot_List = pygame.sprite.Group()

gameOver = False
startOver = False

Start_Cord = input("Start Cord: ")
Start_Cord = Start_Cord.split(", ")
Start_Cord = int(Start_Cord[0]), int(Start_Cord[1])
End_Cord = input("End Cord: ")
End_Cord = End_Cord.split(", ")
End_Cord = int(End_Cord[0]), int(End_Cord[1])
Dot_List.add(Dot(Start_Cord, (255, 0, 0)))
Dot_List.add(Dot(End_Cord, (255, 0, 0)))

canttouch = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]  # These cords show a verticle line
for i in range(len(canttouch)):
    Dot_List.add(Dot(canttouch[i], (0, 0, 0)))

Color = (150, 0, 150)


biglist = []

biglist.append([Start_Cord])

while gameOver == False:
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 500, 500))
    pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 500))
    pygame.draw.line(screen, (0, 0, 0), (0, 250), (500, 250))
    for event in pygame.event.get():  # This code is to see what keys you press and input them into name
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # If you click enter it jumps to the game if theres no one in the list that has that name
                if startOver == True:
                    Start_Cord = input("Start Cord: ")
                    Start_Cord = Start_Cord.split(", ")
                    Start_Cord = int(Start_Cord[0]), int(Start_Cord[1])
                    End_Cord = input("End Cord: ")
                    End_Cord = End_Cord.split(", ")
                    End_Cord = int(End_Cord[0]), int(End_Cord[1])
                    Dot_List = pygame.sprite.Group()
                    for i in range(len(canttouch)):
                        Dot_List.add(Dot(canttouch[i], (0, 0, 0)))
                    Color = (150, 0, 150)
                    biglist = []
                    biglist.append([Start_Cord])
                    Dot_List.add(Dot(Start_Cord, (255, 0, 0)))
                    Dot_List.add(Dot(End_Cord, (255, 0, 0)))
                    startOver = False

    if startOver == False:
        startOver = A_Star(Start_Cord, End_Cord)

    Dot_List.draw(screen)
    pygame.display.update()