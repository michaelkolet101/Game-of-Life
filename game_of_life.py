import pygame
import numpy as np


#עבודה עם צבעים בגרפיקה כל משתנה מחזיק צבע אחר לתא 
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)

def update(surface, cur, sz):

    #מאתחל מערך דו ממדי זהה באפסים
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    #לולאה על המערך הדו ממדי
    for r, c in np.ndindex(cur.shape):

        #נבדוק כמה תאים חיים יש מסביב לתא בנבחר
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

        #אם יש פחות משני תאים חיים או יותר משלושה חיים והתא הנוכחי חי 
        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            #התא הנוכחי מתאפס
            col = col_background
        #אחרת אם התא הנוכחי חי ויש לו שנים או שלושה שכנים או שהוא כבוי ויש לו שלושה שכנים בדיוק 
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            #התא הנוכחי יהיה דולק
            col = col_alive

        col = col if cur[r, c] == 1 else col_background
        
        #לצייר ריבוע גרפי שעליו יתבצע כל המשחק
        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))

    return nxt

def init(dimx, dimy):

    #נאתחל את המערך לאפסים
    cells = np.zeros((dimy, dimx))

    #יצירת המערך ההתחלתי
    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    
    #נקודה התחלתית על הלוח שממנה המשחק מתחיל
    pos = (3,3)

    #pattern.shape[0] מחזיר שורות ועמודות לתוי ב 0 או 1
    cells[ pos[0]:pos[0] + pattern.shape[0], pos[1]:pos[1] + pattern.shape[1] ] = pattern
    return cells

def main(dimx, dimy, cellsize):
    
    pygame.init()  

    #אתחול  מסך לתצוגה
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))

    #נוסיף כותרת למסך המשחק 
    pygame.display.set_caption("Game of Life by Michael Kolet")

    #איתחול המערך הדו ממדי
    cells = init(dimx, dimy)

    #לולאה אינסופית - הלולאה הראשית של המשחק
    while True:

        #לולאה לכל אירוע שנמצא בתור
        for event in pygame.event.get():

            #אם האירוע הוא יציאהאז יוצאים מהמשחק
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #מילוי שטח המסך במערך שלנו
        surface.fill(col_grid)

        #נקרא לפונקציה שמעדכנת את המערך שלנו לפי כללי המשחק
        cells = update(surface, cells, cellsize)

        #נעדכן את מסך המשחק שלנו 
        pygame.display.update()

if __name__ == "__main__":
    main(120, 90, 8)