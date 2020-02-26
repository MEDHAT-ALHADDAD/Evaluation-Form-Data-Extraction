import cv2


########### determine the answers ##########
def DetermineAnswers(image):
    answer = ""
    counter = 0
    
    ####### getting the contours of the image ############
    enhanced, contours = GetContours(image)
    
    for i in contours:
        ######### remove the contours that are not marks #######
        if(cv2.contourArea(i)>25):
            continue        
        box = cv2.boundingRect(i) #gets the bounding box of the contour
        counter+=1        
        ######### gets the answer of the questions #########
        if(counter == 1):
            temp,enhanced = GetGender(box, counter, enhanced)
            if (temp != 0):
                answer = answer +  temp
        elif(counter == 2):
            temp,enhanced = GetSemester(box, counter, enhanced)
            if (temp != 0):
                answer = answer +  temp
        elif(temp == 3):
            temp,enhanced = GetProgram(box, counter, enhanced)
            if (temp != 0):
                answer = answer +  temp
        else:
            temp,enhanced = GetRest(box, counter, enhanced)
            if (temp != 0):
                answer = answer +  temp
    return answer,enhanced


####### getting the contours of the image ############
def GetContours(image):
    _,contours, _ = cv2.findContours(image,mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)
    contours.reverse() # reverse the list, so the marks are from the top to the bottom
    enhanced = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
    return enhanced, contours
    
######### gets the answer of the gender question #########
def GetGender(box, counter,enhanced):
    if(counter == 1):
        if(box[0]<390):
            cv2.putText(enhanced,"M", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            return "Gender,Male\n",enhanced
            if(395<box[0] and box[0]<460):
                cv2.putText(enhanced, "F", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                return "Gender,Female\n",enhanced
    return 0


######### gets the answer of the semester question #########
def GetSemester(box, counter,enhanced):
    if(counter == 2):
        if(box[0]< 200):
            cv2.putText(enhanced,"Fall", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            return "Semester,Fall\n",enhanced
        elif(box[0]<280):
            cv2.putText(enhanced,"Spring", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            return "Semester,Spring\n",enhanced
        else:
            cv2.putText(enhanced,"Summer", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            return "Semester,Summer\n",enhanced
    return 0
    
####### gets the answer of the program question #########
def GetProgram(box, counter,enhanced):
    if(counter == 3):
            if(box[1]< 140):
                if(box[0]<170):
                    cv2.putText(enhanced,"MCTA", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,MCTA\n",enhanced
                elif(box[0]<195):
                    cv2.putText(enhanced,"ENVER", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,ENVER\n",enhanced
                elif(box[0]<240):
                    cv2.putText(enhanced,"BLDG", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,BLDG\n",enhanced
                elif(box[0]<270):
                    cv2.putText(enhanced,"CESS", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,CESS\n",enhanced
                elif(box[0]<310):
                    cv2.putText(enhanced,"ERGY", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,ERGY\n",enhanced
                elif(box[0]<355):
                    cv2.putText(enhanced,"COMM", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,COMM\n",enhanced
                elif(box[0]<400):
                    cv2.putText(enhanced,"MANF", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,MANF\n",enhanced
            elif(box[0]<152):
                if(box[0]<170):
                    cv2.putText(enhanced,"LAAR", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,LAAR\n",enhanced
                elif(box[0]<190):
                    cv2.putText(enhanced,"MATL", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,MATL\n",enhanced
                elif(box[0]<230):
                    cv2.putText(enhanced,"CISE", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,CISE\n",enhanced
                elif(box[0]<270):
                    cv2.putText(enhanced,"HAUD", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    return "Program,HAUD\n",enhanced
    return 0

########### gets the answers of the rest of the questions ######
def GetRest(box, counter,enhanced):
    if(330 < box[0] and box[0] < 355):
        cv2.putText(enhanced, "SA", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
        return str(counter-3)+"- Strongly Agree\n",enhanced
    elif(360 < box[0] and box[0] < 385):
        cv2.putText(enhanced, "A", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
        return str(counter-3)+"- Agree\n",enhanced
    elif(390 < box[0] and box[0] < 415):
        cv2.putText(enhanced, "N", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
        return str(counter-3)+"- Neutral\n",enhanced
    elif(420 < box[0] and box[0] < 445):
        cv2.putText(enhanced, "D", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
        return str(counter-3)+"- Disagree\n",enhanced
    elif(450 < box[0] and box[0] < 475):
        cv2.putText(enhanced, "SD", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
        return str(counter-3)+"- Strongly Disgree\n",enhanced    
    return 0



########### determine the answers ##########
def determineAnswers(image):
    ####### getting the contours of the image ############
    enhanced, contours = GetContours(image)
    com_ans = ""
    answer = ""
    counter = 0
    for i in contours:
        ######### remove the contours that are not marks #######
        if(cv2.contourArea(i)>25):
            continue
    
        box = cv2.boundingRect(i) #gets the bounding box of the contour
        counter+=1
        ######### gets the answer of the gender question #########
        if(counter == 1):
            if(box[0]<390):
                cv2.putText(enhanced,"M", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                answer = answer + "Gender,Male\n"
                com_ans = com_ans + "Male"
            if(395<box[0] and box[0]<460):
                cv2.putText(enhanced, "F", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                answer = answer + "Gender,Female\n"
                com_ans = com_ans + "Female"
            continue
    
        ######### gets the answer of the semester question #########
        if(counter == 2):
            if(box[0]< 200):
                cv2.putText(enhanced,"Fall", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                answer = answer + "Semester,Fall\n"
                com_ans = com_ans + ",Fall"
            elif(box[0]<280):
                cv2.putText(enhanced,"Spring", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                answer = answer + "Semester,Spring\n"
                com_ans = com_ans + ",Spring"
            else:
                cv2.putText(enhanced,"Summer", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                answer = answer + "Semester,Summer\n"
                com_ans = com_ans + ",Summer"
            continue
    
        ####### gets the answer of the program question #########
        if(counter == 3):
            if(box[1]< 140):
                if(box[0]<170):
                    cv2.putText(enhanced,"MCTA", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,MCTA\n"
                    com_ans = com_ans + ",MCTA"
                elif(box[0]<195):
                    cv2.putText(enhanced,"ENVER", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,ENVER\n"
                    com_ans = com_ans + ",ENVER"
                elif(box[0]<240):
                    cv2.putText(enhanced,"BLDG", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,BLDG\n"
                    com_ans = com_ans + ",BLDG"
                elif(box[0]<270):
                    cv2.putText(enhanced,"CESS", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,CESS\n"
                    com_ans = com_ans + ",CESS"
                elif(box[0]<310):
                    cv2.putText(enhanced,"ERGY", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,ERGY\n"
                    com_ans = com_ans + ",ERGY"
                elif(box[0]<355):
                    cv2.putText(enhanced,"COMM", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,COMM\n"
                    com_ans = com_ans + ",COMM"
                elif(box[0]<400):
                    cv2.putText(enhanced,"MANF", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,MANF\n"
                    com_ans = com_ans + ",MANF"
            elif(box[1]<152):
                if(box[0]<170):
                    cv2.putText(enhanced,"LAAR", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,LAAR\n"
                    com_ans = com_ans + ",LAAR"
                elif(box[0]<190):
                    cv2.putText(enhanced,"MATL", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,MATL\n"
                    com_ans = com_ans + ",MATL"
                elif(box[0]<230):
                    cv2.putText(enhanced,"CISE", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,CISE\n"
                    com_ans = com_ans + ",CISE"
                elif(box[0]<270):
                    cv2.putText(enhanced,"HAUD", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                    answer = answer + "Program,HAUD\n"
                    com_ans = com_ans + ",HAUD"
            continue
        
        ########### gets the answers of the rest of the questions ######
        if(330 < box[0] and box[0] < 355):
            cv2.putText(enhanced, "SA", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            answer = answer + str(counter-3)+",Strongly Agree\n"
            com_ans = com_ans + ",Strongly Agree"
        elif(360 < box[0] and box[0] < 385):
            cv2.putText(enhanced, "A", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            answer = answer + str(counter-3)+",Agree\n"
            com_ans = com_ans + ",Agree"
        elif(390 < box[0] and box[0] < 415):
            cv2.putText(enhanced, "N", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            answer = answer + str(counter-3)+",Neutral\n"
            com_ans = com_ans + ",Neutral"
        elif(420 < box[0] and box[0] < 445):
            cv2.putText(enhanced, "D", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            answer = answer + str(counter-3)+",Disagree\n"
            com_ans = com_ans + ",Disagree"
        elif(450 < box[0] and box[0] < 475):
            cv2.putText(enhanced, "SD", (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            answer = answer + str(counter-3)+",Strongly Disgree\n"
            com_ans = com_ans + ",Strongly Disgree"
    com_ans = com_ans + "\n"
    return answer,enhanced,com_ans