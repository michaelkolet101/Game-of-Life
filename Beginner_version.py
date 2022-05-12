from os import system, name
import time

HEIGHT = 5
WIDTH = 5

ALIVE = 1
DEAD = 0

#אני עובד עם לינוקס אז עשיתי שניקוי המסך יעבוד גם עם וינדוס
def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def get_neighbors_count(board, y, x):

    alive_neighbors = 0

    for  y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            #נבדוק מסביב התא הנוכחי ולא אותו עצמו
            
            if ((y_offset == 0) and (x_offset == 0)):
                continue
                
            #נבדוק שאנו לא חורגים מהמערך
            checked_y  = (y + y_offset)
            if (checked_y == -1):
                checked_y = HEIGHT-1
            elif(checked_y == HEIGHT):
                checked_y = 0

            checked_x = (x + x_offset)
            if (checked_x == -1):
                checked_x = WIDTH - 1
            elif(checked_x == WIDTH):
                checked_x = 0

            

            if (board[checked_y][checked_x] == ALIVE):
               alive_neighbors +=1


    return alive_neighbors


def print_board(board):
    for i in board:
        print(i)
    print("\n")

#העתקת מטריצה אחת לשניה
def copy_board(src, dest):
    dest = src[:]
    return dest

def play_turn(board):
    
    tmp = []
    tmp = copy_board(board, tmp)

    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            
            neighbors = get_neighbors_count(tmp, y, x)
            current = tmp[y][x]

            if (current == ALIVE):

                if (neighbors < 2):
                    board[y][x] = DEAD
                
                elif (neighbors < 4):
                    board[y][x] = ALIVE
                
                else:
                    board[y][x] = DEAD
            
            else:
                if (neighbors == 3):
                    board[y][x] = ALIVE



def main():

    board = [[ALIVE, DEAD, DEAD, DEAD, DEAD],
             [DEAD, DEAD, DEAD, DEAD, DEAD],
             [DEAD, ALIVE, ALIVE, ALIVE, DEAD],
             [DEAD, DEAD, DEAD, DEAD, DEAD],
             [DEAD, DEAD, DEAD, DEAD, ALIVE]
    ]
    

    

    while True:
        print_board(board)
        play_turn(board)
        time.sleep(2)
        clearScreen()
    










if __name__ == "__main__":
    main()