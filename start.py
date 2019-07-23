import cv2
import os
vidcap = cv2.VideoCapture('/home/haritk/TV_AUDIENCE/test2.MP4')
success,image = vidcap.read()
fps = vidcap.get(cv2.CAP_PROP_FPS)
totalframes = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

frame2skip = 10  # num of frames to skip when extracting
outputframe = int(totalframes / frame2skip)

#print('Video FPS rate is {}'.format(fps))
#print('You will get {} frames in total'.format(outputframe))

while success:
    frameId = int(round(vidcap.get(1)))
    success, image = vidcap.read()


    #cv2.imshow('Frame',image)

    if frameId % frame2skip == 0:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('frame.jpg' , gray)
        #print('Export frame {}: '.format(frameId), success)
        os.system('python3 extract.py')
       # cv2.imshow('Frame',image)

vidcap.release()
#print ('Extraction completed!')
#os.system('python3 extract.py')ss
