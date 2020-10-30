from graphics import *
import random
import math
def parcheesi_board():
    #Making the GraphWin (will be moved to main in a later stage)
    board = GraphWin("Parcheesi!", 721, 721)
    
    #Coloring background
    board.setBackground(color_rgb(255,250,194))
    
    #Creating all starting areas
    top_left_start = Circle(Point(120,120), 120)
    top_left_start.setFill(color_rgb(255,105,97))
    top_left_start.draw(board)
    rectangle1 = Rectangle(Point(35.15,35.15), Point(204.85,204.85))
    rectangle1.setFill("light blue")
    rectangle1.draw(board)
    top_right_start = Circle(Point(600,120), 120)
    top_right_start.setFill("blue")
    top_right_start.draw(board)
    rectangle2 = rectangle1.clone()
    rectangle2.move(480,0)
    rectangle2.draw(board)
    bottom_left_start = Circle(Point(120,600), 120)
    bottom_left_start.setFill("green")
    bottom_left_start.draw(board)
    rectangle3 = rectangle1.clone()
    rectangle3.move(0,480)
    rectangle3.draw(board)
    bottom_right_start = Circle(Point(600,600), 120)
    bottom_right_start.setFill("yellow")
    bottom_right_start.draw(board)
    rectangle4 = rectangle1.clone()
    rectangle4.move(480,480)
    rectangle4.draw(board)

    #Creating the white and red/orange tiles
    white_background = Polygon(Point(240,0), Point(240,210), Point(210, 240), Point(0, 240), Point(0, 480), Point(210,480), Point(240,510), Point(240,720), Point(480,720), Point(480,510), Point(510,480), Point(720,480), Point(720,240), Point(510,240), Point(480,210), Point(480,0))
    white_background.setFill("white")
    white_background.draw(board)
    line = Line(Point(240,0), Point(240,210))
    line.draw(board)
    line = Line(Point(480,0), Point(480,210))
    line.draw(board)
    red_background = Polygon(Point(320,30), Point(320,320), Point(30,320), Point(30,400), Point(320,400), Point(320,690), Point(400,690), Point(400,400), Point(690,400), Point(690,320), Point(400,320), Point(400,30))
    red_background.setFill(color_rgb(239,65,0))
    red_background.draw(board)
    for i in range(0, 211, 30):
        line = Line(Point(240,i), Point(480, i))
        line.draw(board)
        line = Line(Point(i, 240), Point(i, 480))
        line.draw(board)
        line = Line(Point(510 + i, 240), Point(510 + i, 480))
        line.draw(board)
        line = Line(Point(240, 510 + i), Point(480, 510 + i))
        line.draw(board)

    #Creating the safe tiles
    for i in range(0, 2):
        x = i * 690
        y = i * 450
        safe = Rectangle(Point(320,0 + x), Point(400,30 + x))
        safe.setFill("light blue")
        safe.draw(board)
        circle = Circle(Point(360,15 + x), 15)
        circle.draw(board)
        safe = Rectangle(Point(0 + x,320), Point(30 + x,400))
        safe.setFill("light blue")
        safe.draw(board)
        circle = Circle(Point(15 + x, 360), 15)
        circle.draw(board)
        safe = Rectangle(Point(240,120 + y), Point(320, 150 + y))
        safe.setFill("light blue")
        safe.draw(board)
        circle = Circle(Point(280,135 + y), 15)
        circle.draw(board)
        safe = Rectangle(Point(400,120 + y), Point(480, 150 + y))
        safe.setFill("light blue")
        safe.draw(board)
        circle = Circle(Point(440,135 + y), 15)
        circle.draw(board)
        safe = Rectangle(Point(120 + y,240), Point(150 + y,320))
        safe.setFill("light blue")
        safe.draw(board)
        circle = Circle(Point(135 + y,280), 15)
        circle.draw(board)
        safe = Rectangle(Point(120 + y,400), Point(150 + y,480))
        safe.setFill("light blue")
        safe.draw(board)
        circle = Circle(Point(135 + y,440), 15)
        circle.draw(board)

    #Creating the Home space + finishing touches
    home = Rectangle(Point(240,240), Point(480,480))
    home.setFill("pink")
    home.draw(board)
    line = Line(Point(240,240), Point(225,225))
    line.draw(board)
    line = Line(Point(480,240), Point(495,225))
    line.draw(board)
    line = Line(Point(240,480), Point(225,495))
    line.draw(board)
    line = Line(Point(480,480), Point(495,495))
    line.draw(board)

    #Setting up default values
    red_start = [[75,75], [75,165], [165,75], [165,165]]
    blue_start = [[555, 75], [555, 165], [645, 75], [645, 165]]
    green_start = [[75, 555], [75, 645], [165, 555], [165, 645]]
    yellow_start = [[555, 555], [555, 645], [645, 555], [645, 645]]
    red_end = [[270, 270], [270, 315], [315, 270], [315, 315]]
    blue_end = [[405, 270], [405, 315], [450, 270], [450, 315]]
    green_end = [[270, 405], [270, 450], [315, 405], [315, 450]]
    yellow_end = [[405, 405], [405, 450], [450, 405], [450, 450]]
    red = [[None,None,"start",-1,"red"],[None,None,"start",-1,"red"],[None,None,"start",-1,"red"],[None,None,"start",-1,"red"]]
    blue = [[None,None,"start",-1,"blue"],[None,None,"start",-1,"blue"],[None,None,"start",-1,"blue"],[None,None,"start",-1,"blue"]]
    green = [[None,None,"start",-1,"green"],[None,None,"start",-1,"green"],[None,None,"start",-1,"green"],[None,None,"start",-1,"green"]]
    yellow = [[None,None,"start",-1,"yellow"],[None,None,"start",-1,"yellow"],[None,None,"start",-1,"yellow"],[None,None,"start",-1,"yellow"]]
    for i in range(4):
        red[i][0] = Circle(Point(red_start[i][0], red_start[i][1]), 15)
        red[i][0].setFill("red")
        blue[i][0] = Circle(Point(blue_start[i][0], blue_start[i][1]), 15)
        blue[i][0].setFill("blue")
        green[i][0] = Circle(Point(green_start[i][0], green_start[i][1]), 15)
        green[i][0].setFill("green")
        yellow[i][0] = Circle(Point(yellow_start[i][0], yellow_start[i][1]), 15)
        yellow[i][0].setFill("yellow")
    board_order = [[280,15],[280,45],[280,75],[280,105],[280,135],[280,165],[280,195],[280,225],[225,280],[195,280],[165,280],[135,280],[105,280],[75,280],[45,280],[15,280],[15,360],[15,440],[45,440],[75,440],[105,440],[135,440],[165,440],[195,440],[225,440],[280,495],[280,525],[280,555],[280,585],[280,615],[280,645],[280,675],[280,705],[360,705],[440,705],[440,675],[440,645],[440,615],[440,585],[440,555],[440,525],[440,495],[495,440],[525,440],[555,440],[585,440],[615,440],[645,440],[675,440],[705,440],[705,360],[705,280],[675,280],[645,280],[615,280],[585,280],[555,280],[525,280],[495,280],[440,225],[440,195],[440,165],[440,135],[440,105],[440,75],[440,45],[440,15],[360,15],[360,45],[360,75],[360,105],[360,135],[360,165],[360,195],[360,225],[45,360],[75,360],[105,360],[135,360],[165,360],[195,360],[225,360],[360,675],[360,645],[360,615],[360,585],[360,555],[360,525],[360,495],[675,360],[645,360],[615,360],[585,360],[555,360],[525,360],[495,360]]
    red_order = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74]
    blue_order = [55,56,57,58,59,60,61,62,63,64,65,66,67,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,89,90,91,92,93,94,95]
    green_order = [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,75,76,77,78,79,80,81]
    yellow_order = [38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,82,83,84,85,86,87,88]
    safe_spaces = [4,11,16,21,28,33,38,45,50,55,62,67]
    
    #Check any order (dev tool)
    #for i in red_order:
    #    red_test = Circle(Point(board_order[i][0],board_order[i][1]), 15)
    #    red_test.setFill("red")
    #    red_test.draw(board)
    #    text = Text(Point(board_order[i][0], board_order[i][1]), i - 4)
    #    text.draw(board)
    #j = 0
    #for i in blue_order:
    #    blue_test = Circle(Point(board_order[i][0],board_order[i][1]), 15)
    #    blue_test.setFill("blue")
    #    blue_test.draw(board)
    #    text = Text(Point(board_order[i][0], board_order[i][1]), j)
    #    text.draw(board)
    #    j += 1
    #for i in green_order:
    #    green_test = Circle(Point(board_order[i][0],board_order[i][1]), 15)
    #    green_test.setFill("green")
    #    green_test.draw(board)
    #    text = Text(Point(board_order[i][0], board_order[i][1]), j)
    #    text.draw(board)
    #    j += 1
    #for i in yellow_order:
    #    yellow_test = Circle(Point(board_order[i][0],board_order[i][1]), 15)
    #    yellow_test.setFill("yellow")
    #    yellow_test.draw(board)
    #    text = Text(Point(board_order[i][0], board_order[i][1]), j)
    #    text.draw(board)
    #    j += 1
    for i in range(len(board_order)):
        text = Text(Point(board_order[i][0], board_order[i][1]), i)
        text.draw(board)
        
    #Players choose how many players there are
    test = True
    num_players = str(input("How many players will be playing? (min 2, max 4) "))
    while(test == True):
        try:
            while(int(num_players) < 2 or int(num_players) > 4):
                num_players = str(input("An error occurred, please input a number between 2 and 4: "))
            test = False
        except:
            num_players = str(input("An error occurred, please make sure you input an integer: "))
    num_players = int(num_players)

    #Players choose their colors.
    for i in range(num_players):
        print(f'Player {i + 1}, please choose which color you want to be. (click on the starting area of the respective color)')
        test = True
        while (test == True):
            point = board.getMouse()
            test = False
            if(35.15 < point.getX() < 204.85 and 35.15 < point.getY() < 204.85):
                if(red[0][1] == None):
                    red[0][1], red[1][1], red[2][1], red[3][1] = i + 1, i + 1, i + 1, i + 1
                    print(f'Player {i + 1} is red.')
                    for i in range(4):
                        red[i][0].draw(board)
                else:
                    print(f'Error: player {i + 1} is already red. Please choose another color.')
                    test = True
            else:
                if(515.15 < point.getX() < 684.85 and 35.15 < point.getY() < 204.85):
                    if(blue[0][1] == None):
                        blue[0][1], blue[1][1], blue[2][1], blue[3][1] = i + 1, i + 1, i + 1, i + 1
                        print(f'Player {i + 1} is blue.')
                        for i in range(4):
                            blue[i][0].draw(board)
                    else:
                        print(f'Error: player {i + 1} is already blue. Please choose another color.')
                        test = True
                else:
                    if(35.15 < point.getX() < 204.85 and 515.15 < point.getY() < 684.85):
                        if(green[0][1] == None):
                            green[0][1], green[1][1], green[2][1], green[3][1] = i + 1, i + 1, i + 1, i + 1
                            print(f'Player {i + 1} is green.')
                            for i in range(4):
                                green[i][0].draw(board)
                        else:
                            print(f'Error: player {i + 1} is already green. Please choose another color.')
                            test = True
                    else:
                        if(515.15 < point.getX() < 684.85 and 515.15 < point.getY() < 684.85):
                            if(yellow[0][1] == None):
                                yellow[0][1], yellow[1][1], yellow[2][1], yellow[3][1] = i + 1, i + 1, i + 1, i + 1
                                print(f'Player {i + 1} is yellow.')
                                for i in range(4):
                                    yellow[i][0].draw(board)
                            else:
                                print(f'Error: player {i + 1} is already yellow. Please choose another color.')
                                test = True
                        else:
                            print(f'Error: no click found in any of the starting points, please try again. (must be within the square of the starting point)')
                            test = True
    
    #Roll the die to see who goes first
    roll = []
    print(f'\nRolling the die for {num_players} players...')
    for i in range(num_players):
        a = True
        b = True
        roll.append(random.randrange(1, 7))
        print(f'Player {i + 1}\'s roll: {roll[i]}')
        while(a == True):
            a = False
            for j in range(i):
                b = True
                if(b == True):
                    while(roll[i] == roll[j]):
                        roll[i] = random.randrange(1, 7)
                        print(f'Rerolling player {i + 1}\'s roll due to it being equal to player {j + 1}\'s roll. ')
                        print(f'Player {i + 1}\'s roll: {roll[i]}')
                        b = False
                        a = True
    lowest = roll[0]
    first = 0
    for i in range(1, num_players):
        if(roll[i] < lowest):
            lowest = roll[i]
            first = i

    #Calculates and decides the final order
    print(f'Player {first + 1} will be going first, the player to go after them will be chosen in a counter-clockwise order, and so on.')
    player_order = []
    n = 1
    #When red's player is first...
    if(red[0][1] == first + 1):
        player_order.append(red[0][1])
        one = red
        for i in range(4):
            red[i][0].undraw()
            one[i][0].draw(board)
            one_order = red_order
        if(green[0][1] != None):
            player_order.append(green[0][1])
            if(n == 1):
                two = green
                two_order = green_order
                for i in range(4):
                    green[i][0].undraw()
                    two[i][0].draw(board)
            n += 1
        if(yellow[0][1] != None):
            player_order.append(yellow[0][1])
            if(n == 1):
                two = yellow
                two_order = yellow_order
                for i in range(4):
                    yellow[i][0].undraw()
                    two[i][0].draw(board)
            if(n == 2):
                three = yellow
                three_order = yellow_order
                for i in range(4):
                    yellow[i][0].undraw()
                    three[i][0].draw(board)
            n += 1
        if(blue[0][1] != None):
            player_order.append(blue[0][1])
            if(n == 1):
                two = blue
                two_order = blue_order
                for i in range(4):
                    blue[i][0].undraw()
                    two[i][0].draw(board)
            if(n == 2):
                three = blue
                three_order = blue_order
                for i in range(4):
                    blue[i][0].undraw()
                    three[i][0].draw(board)
            if(n == 3):
                four = blue
                four_order = blue_order
                for i in range(4):
                    blue[i][0].undraw()
                    four[i][0].draw(board)

    #When blue's player is first...
    if(blue[0][1] == first + 1):
        player_order.append(blue[0][1])
        one = blue
        one_order = blue_order
        for i in range(4):
            blue[i][0].undraw()
            one[i][0].draw(board)
        if(red[0][1] != None):
            player_order.append(red[0][1])
            if(n == 1):
                two = red
                two_order = red_order
                for i in range(4):
                    red[i][0].undraw()
                    two[i][0].draw(board)
            n += 1
        if(green[0][1] != None):
            player_order.append(green[0][1])
            if(n == 1):
                two = green
                two_order = green_order
                for i in range(4):
                    green[i][0].undraw()
                    two[i][0].draw(board)
            if(n == 2):
                three = green
                three_order = green_order
                for i in range(4):
                    green[i][0].undraw()
                    three[i][0].draw(board)
            n += 1
        if(yellow[0][1] != None):
            player_order.append(yellow[0][1])
            if(n == 1):
                two = yellow
                two_order = yellow_order
                for i in range(4):
                    yellow[i][0].undraw()
                    two[i][0].draw(board)
            if(n == 2):
                three = yellow
                three_order = yellow_order
                for i in range(4):
                    yellow[i][0].undraw()
                    three[i][0].draw(board)
            if(n == 3):
                four = yellow
                four_order = yellow_order
                for i in range(4):
                    yellow[i][0].undraw()
                    four[i][0].draw(board)

    #When green's player is first...
    if(green[0][1] == first + 1):
        player_order.append(green[0][1])
        one = green
        one_order = green_order
        for i in range(4):
            green[i][0].undraw()
            one[i][0].draw(board)
        if(yellow[0][1] != None):
            player_order.append(yellow[0][1])
            if(n == 1):
                two = yellow
                two_order = yellow_order
                for i in range(4):
                    yellow[i][0].undraw()
                    two[i][0].draw(board)
            n += 1
        if(blue[0][1] != None):
            player_order.append(blue[0][1])
            if(n == 1):
                two = blue
                two_order = blue_order
                for i in range(4):
                    blue[i][0].undraw()
                    two[i][0].draw(board)
            if(n == 2):
                three = blue
                three_order = blue_order
                for i in range(4):
                    blue[i][0].undraw()
                    three[i][0].draw(board)
            n += 1
        if(red[0][1] != None):
            player_order.append(red[0][1])
            if(n == 1):
                two = red
                two_order = red_order
                for i in range(4):
                    red[i][0].undraw()
                    two[i][0].draw(board)
            if(n == 2):
                three = red
                three_order = red_order
                for i in range(4):
                    red[i][0].undraw()
                    three[i][0].draw(board)
            if(n == 3):
                four = red
                four_order = four_order
                for i in range(4):
                    red[i][0].undraw()
                    four[i][0].draw(board)

    #When yellow's player is first...
    if(yellow[0][1] == first + 1):
        player_order.append(yellow[0][1])
        one = yellow
        one_order = yellow_order
        for i in range(4):
            yellow[i][0].undraw()
            one[i][0].draw(board)
        if(blue[0][1] != None):
            player_order.append(blue[0][1])
            if(n == 1):
                two = blue
                two_order = blue_order
                for i in range(4):
                    blue[i][0].undraw()
                    two[i][0].draw(board)
            n += 1
        if(red[0][1] != None):
            player_order.append(red[0][1])
            if(n == 1):
                two = red
                two_order = red_order
                for i in range(4):
                    red[i][0].undraw()
                    two[i][0].draw(board)
            if(n == 2):
                three = red
                three_order = red_order
                for i in range(4):
                    red[i][0].undraw()
                    three[i][0].draw(board)
            n += 1
        if(green[0][1] != None):
            player_order.append(green[0][1])
            if(n == 1):
                two = green
                two_order = green_order
                for i in range(4):
                    green[i][0].undraw()
                    two[i][0].draw(board)
            if(n == 2):
                three = green
                three_order = green_order
                for i in range(4):
                    green[i][0].undraw()
                    three[i][0].draw(board)
            if(n == 3):
                four = green
                four_order = green_order
                for i in range(4):
                    green[i][0].undraw()
                    four[i][0].draw(board)
                    
    print(f'\nHere is the order:')
    if(num_players == 4):
        print(f'Player {player_order[0]} ({one[0][4]}) will be going first\nPlayer {player_order[1]} ({two[0][4]}) will be going second\nPlayer {player_order[2]} ({three[0][4]}) will be going third\nPlayer {player_order[3]} ({four[0][4]}) will be going last.')
    if(num_players == 3):
        print(f'Player {player_order[0]} ({one[0][4]}) will be going first\nPlayer {player_order[1]} ({two[0][4]}) will be going second\nPlayer {player_order[2]} ({three[0][4]}) will be going last.')
    if(num_players == 2):
        print(f'Player {player_order[0]} ({one[0][4]}) will be going first\nPlayer {player_order[1]} ({two[0][4]}) will be going second.\n')

    die = [None, None]
    win = False
    while(win == False):
        print(f'\nPlayer {one[0][1]}\'s ({one[0][4]}) turn. Rolling the die...')
        die[0] = random.randrange(1,7)
        die[1] = random.randrange(1,7)
        print(f'Here are your rolls: {die[0]}, {die[1]}')
        test = True
        choice = str(input(f'Choose which roll to use first (or both, if you so choose):\n1. {die[0]}\n2. {die[1]}\n3. {int(die[0]) + int(die[1])}'))
        while(test == True):
            try:
                while(int(choice) != 1 and int(choice) != 2 and int(choice) != 3):
                    choice = str(input(f'An error occurred, please input "1" for {die[0]}, "2" for {die[1]} or "3" or {int(die[0]) + int(die[1])}: '))
                test = False
            except:
                choice = str(input("An error occurred, please make sure you input an integer: "))
        choice = int(choice)
        switch = {
            1: die[0],
            2: die[1],
            3: int(die[0]) + int(die[1])
        }
        temp = switch[choice]
        print(f'Choose a piece to move {temp} space(s) on the board.')
        test = True
        while(test == True):
            test = False
            a = False
            point = board.getMouse()
            x = point.getX()
            y = point.getY()
            for i in range(4):
                point1 = one[i][0].getP1()
                point2 = one[i][0].getP2()
                x2 = (point1.getX() + point2.getX())/2
                y2 = (point1.getY() + point2.getY())/2
                distance = math.sqrt(((x - x2) ** 2) + ((y - y2) ** 2))
                print(distance, one[i][0].getRadius())
                if(distance < one[i][0].getRadius()):
                    piece = i
                    a = True
                    test = False
                else:
                    if(a == False):
                        test = True
                
        
        one[piece][0].undraw()
        one[piece][3] += temp
        one[piece][0] = Circle(Point(board_order[one_order[temp]][0], board_order[one_order[temp]][1]), 15)
        one[piece][0].setFill(one[piece][4])
        one[piece][0].draw(board)
        win = True
              
    #71 = home
    #-1 = start
    #[Circle,player_number,state_of_piece,board_number,color]
                

    board.getMouse()
    board.close()

parcheesi_board()
