#importing our libraries that we will be using for emotion detection
import numpy as np
import cv2
import keras

cap = cv2.VideoCapture(0) #used for capturing the  video using the webcam
model_path = 'Optimal Model\model_optimal.h5' #path of our model
model = keras.models.load_model(model_path) #loading our model that we will use to make predictions of emotions

emotion_dict = {0:'Angry',1:'Disgust',2:'Fear',3:'Happy',4:'Neutral',5:'Sad',6:'Surprise'} #dictionary containing different values

while True: #continuous loop to keep the window running
    frame = cap.read() #reading our  frames from the capture
    facecascade = cv2.CascadeClassifier('Optimal Model\haarcascade_frontalface_default.xml') #using the cascade classifier for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting whatever we are reading into gray
    faces = facecascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5) #this helps in finding features and location in our images - we are passing in our grayscale input, we are scaling down the image which is done with scaleFactor 
    # min neighbors helps in determining the quality of detection 

    for (x, y, w, h) in faces: #drawing rectangles on the faces detected and also adding text
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2) #used to draw our rectangle, we are specifying the start and end point and also color and width of our rectangle
        roi_gray = gray[y:y + h, x:x + w] #ROI - Region of interest, in this we are trying to select the rows starting from y to y+h and then columns from x to x+h - this works like NumPy slicing
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0) #resizing the inputs in order to get  them in the same shape as the images on which our images were trained
        prediction = model.predict(cropped_img) #making predictions on the face detected
        maxindex = int(np.argmax(prediction)) #getting the maximum index out of all the predicted indices
        cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA) #printing the emotion label corresponding to the output index from our emotio dictionary

    cv2.imshow('Video', cv2.resize(frame,(700,500),interpolation = cv2.INTER_CUBIC)) #creating our video window in which we will be detecting emotions
    if cv2.waitKey(1) & 0xFF == ord('q'): #we will have to press q if we wish to exit our window
        break

cap.release() #this will release the hardware and software resources that are being used
cv2.destroyAllWindows() #destroys the window that we created for emotion detection
