import cv2 
import numpy as np 
import pytesseract
from PIL import Image
from pytesseract import image_to_string
import os 

#img = cv2.imread("/home/rahul/Desktop/Untitled Folder/mango.jpg",1)



def get_string(src_path):
    # Read image with opencv
    img = cv2.imread(src_path,0)

    
    height , weight = img.shape[:2]

#get's starting pixel coordinate from (from left corner of the rectangle)
    start_row , start_coloum = int(height*0.62), 0
    end_row , end_column = int(height*.9),weight

    cropped_img = img[start_row:end_row,start_coloum:end_column]
#cv2.imshow("cropped",cropped_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()  

    _,coins_binary = cv2.threshold(cropped_img, 130, 255, cv2.THRESH_BINARY)

# invert image to get coins
#
    coins_binary = cv2.bitwise_not(coins_binary)

    height , weight = coins_binary.shape[:2]

    start_row , start_coloum_x_1 = 0,int(weight*0.05)
    end_row , end_column_x_1 = height,int(weight*0.23)

    cropped_img_x_1 =coins_binary[start_row:end_row,start_coloum_x_1:end_column_x_1]
    cv2.imwrite(src_path +"cat111.jpg",cropped_img_x_1)


    start_row , start_coloum_x_2 = 0, int(weight*0.24)

    end_row , end_column_x_2 = height , int(weight*0.70)




    cropped_img_x_2 = coins_binary[start_row:end_row,start_coloum_x_2:end_column_x_2]

    #cv2.imshow("cropped_img_x_2",cropped_img_x_2)
    #cv2.waitKey(0)




     

    
    
   

    cv2.imwrite(src_path + "thres111.jpg",cropped_img_x_2)

     
    # Recognize text with tesseract for python
    input_channel= pytesseract.image_to_string(Image.open(src_path+"cat111.jpg"))
    programme_name =pytesseract.image_to_string(Image.open(src_path+"thres111.jpg"))

    return input_channel,programme_name
    








def chennel_match(actual_channel,input_channel):

    x = 0 # initializinz a x variable
    input_channel_spilit = list(input_channel)# spiliting the input chennel into separate letter
    
    for channel in range(len(actual_channel)):

        actual_channel_spilit = list(actual_channel[x]) # spiliting the actuall chennel from x=0 to the end
        match_probability = 0 # probability of matching letter of actual and input chennel (one by one letter increment)
        for letter in range(len(input_channel)):

            # here comparing every letter from input_channel to actuall_channel and input_channel length
            # should less than actual_channel length

            if len(input_channel)<=len(actual_channel[x]) and input_channel_spilit[letter]==actual_channel_spilit[letter]:
                
                match_probability += 1/len(actual_channel[x]) # match_probability increment letter by letter increment 
                
            else:
                x+=1
                break

        if match_probability>= 0.6: #  thereshold probability value for the prediction of actual channel dislayed 
            print(match_probability)
     #       return actual_channel[x-1]
            break
    

    if match_probability<=0.5:
       print(match_probability)
       print("No chennel detected")
    else:
        return actual_channel[x]






def programme(number,actual_channel,programme_name,time):

    channel_description  = {  "channnel_no.":number,
                                 "channel_name":actual_channel,
                                 "ongoing_programme": programme_name,
                                   " Time" :time}


    return  channel_description














src_path = "/home/TV_AUDIENCE/frame_10.jpg"
sentence_output = get_string(src_path)
print('--- Start recognize text from image ---')
sentence_output = (sentence_output[0].replace('\n\n','.'),sentence_output[1].replace('\n\n','.'))
  #number = sentence_output[0].h2
x = 0
while(True):
#for i in range(350): 
    if sentence_output[1][x]!= ".":
       x+=1
    else: 
      
         programme_name = sentence_output[1][0:x]
         Time = sentence_output[1][x+1:x+20]

         break    

x = 0
while(True):

    if sentence_output[0][x]!= ".":
       x+=1
    else: 
      
         number = sentence_output[0][0:x]
         input_channel = sentence_output[0][x+1:]

         break    







actual_channel1 = ["SET","Set HD","Let's Dance","Star Bharat","Star Bharat HD","Colors","Colors HD","Airtel Entertainment Homes","& Tv","& Tv HD","Customer Care","Homeshop18","Shop CJ","Big Magic","Sony Sab","Sony Sab HD","NT7","Rishtey","Aapki Rasoi"]
  

print("------ Done -------")
print()
actual_channel = chennel_match(actual_channel1,input_channel)
#programme_name = sentence_output[1].p1
#Time = sentence_output[1].p2

#print(trail)

channel_description = programme(number,actual_channel,programme_name,Time,)

f = open("/home/TV_AUDIENCE/send.txt","w+")

f.write(str(channel_description))

f.close()	



# for deleting the image 

try:
    os.remove(src_path+"cat111.jpg")
    os.remove(src_path + "thres111.jpg")
   # os.remove(src_path)


except: pass
           
#cv2.imshow("image_erode ", img)Dict = {old_select_hd :h}

