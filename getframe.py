import cv2
from time import time

def getframe():
    vid = cv2.VideoCapture(0)
    st = time()
    
    while(True):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
               break
        if time()-st >= 0.1:
            st = time()
            cv2.imwrite('frm.png', frame)

    # After the loop release the cap object
    vid.release()
    cv2.destroyAllWindows()
    return frame

getframe()
