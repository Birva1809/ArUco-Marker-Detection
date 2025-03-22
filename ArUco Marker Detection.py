import cv2 as cv
from cv2 import aruco
import numpy as np
import math

ArUco_details_dict = {}
ArUco_corners = {}

dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_250)
parameters =  cv.aruco.DetectorParameters()
detector = cv.aruco.ArucoDetector(dictionary, parameters)

path=input('Enter the image path conntaing Aruco (Without " "): ')
# img = cv.imread(r"E:\E_Yantra_Robotics_Competition\Task_2A_files\public_test_cases\aruco_2.png")
img = cv.imread(path)

markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(img)
for i in range(len(markerIds)):
    current_marker = markerCorners[i]
    # markerCorners=np.reshape(markerCorners,(4,2))
    current_marker = np.reshape(current_marker,(4,2))
    ArUco_corners[int(markerIds[i])] = current_marker
    x_sum = current_marker[:, 0].sum()
    y_sum = current_marker[:, 1].sum()
    center_pixel = list((int(x_sum/4),int(y_sum/4)))
    
    x1 = current_marker[0][0]
    y1 = current_marker[0][1]
    x2 = current_marker[3][0]
    y2 = current_marker[3][1]
    
    if(x2 - x1 != 0):
          M1 = (float)(y2-y1)/(x2-x1)  
    else:
        M1=90
    # print ("Slope is:", M1)
    x3 = current_marker[3][0]
    y3 = current_marker[3][1]
    x4 = current_marker[3][0] + 100
    y4 = current_marker[3][1]
    
    if(x4 - x3 != 0):
          M2 = (float)(y4-y3)/(x4-x3)
    PI = 3.14159265
    # Store the tan value of the angle
    angle =(M2 - M1) / (1 + M1 * M2)
    # Calculate tan inverse of the angle
    ret = math.atan(angle)
    # Convert the angle from
    # radian to degree
    val = (ret * 180) / PI
    if val>0:
        val=val-91.004
    else:
        val=val+88.996
    # print(round(val,4))
    angle = val
    ArUco_details_dict[int(markerIds[i])] = [center_pixel,angle]
    
    print("-------------------------------------------")
    print("Aruco ID: ", markerIds[i][0])
    print("Aruco Center Coordinates (x,y): ", ArUco_details_dict[int(markerIds[i])][0])
    print("Aruco Angle (Tilted with respect to vertical): ", ArUco_details_dict[int(markerIds[i])][1])
    print("Aruco Corner Coordinates (Followed by, Bottom Left, Bottom Right, Upper Right, Upper Left): ", ArUco_corners[int(markerIds[i])])
    print("-------------------------------------------")
    
def mark_ArUco_image(image,ArUco_details_dict, ArUco_corners):

    for ids, details in ArUco_details_dict.items():
        center = details[0]
        cv.circle(image, center, 5, (0,0,255), -1)

        corner = ArUco_corners[int(ids)]
        cv.circle(image, (int(corner[0][0]), int(corner[0][1])), 5, (50, 50, 50), -1)
        cv.circle(image, (int(corner[1][0]), int(corner[1][1])), 5, (0, 255, 0), -1)
        cv.circle(image, (int(corner[2][0]), int(corner[2][1])), 5, (128, 0, 255), -1)
        cv.circle(image, (int(corner[3][0]), int(corner[3][1])), 5, (25, 255, 255), -1)

        tl_tr_center_x = int((corner[0][0] + corner[1][0]) / 2)
        tl_tr_center_y = int((corner[0][1] + corner[1][1]) / 2) 

        cv.line(image,center,(tl_tr_center_x, tl_tr_center_y),(255,0,0),5)
        display_offset = int(math.sqrt((tl_tr_center_x - center[0])**2+(tl_tr_center_y - center[1])**2))
        cv.putText(image,str(ids),(center[0]+int(display_offset/2),center[1]),cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        angle = details[1]
        cv.putText(image,str(angle),(center[0]-display_offset,center[1]),cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    return image


#displaying the marked image
img = mark_ArUco_image(img, ArUco_details_dict, ArUco_corners) 
cv.imshow("Marked Image",img)
cv.waitKey(0)
cv.destroyAllWindows()     
        
        
        
        
        
        
        
        
        
        
        
        
        