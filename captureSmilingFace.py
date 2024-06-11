
# importing the necessary libraries
# Here, mediapipe, which is a library created by Google, is used to capture the landmarks on face(especially eyebrows by which we will detect a smile)
# winsound is used to play a shutter sound whenever a photo is clicked
import cv2 as cv
import mediapipe
import winsound




# these are the variables to store the lamdmark points
x1,x2,y1,y2 = 0,0,0,0

# here face_mesh is used to detect and track faces in image or video streams
# The FaceMesh object provides information about the location of key facial features, known as landmarks.
# the refine_landmarks is an optional parameter that enables the refinement of landmarks, which results in more accurate landmark detection. 
faceLandmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)


camera = cv.VideoCapture(0)


# loop to keep the camera on
while True:
    # capturing each frame from camera
    res, frame = camera.read()

    # as the rear camera gives mirror images we need to flip it
    frame = cv.flip(frame, 1)
    h, w, _ = frame.shape
    
    # converting the frame/image format from bgr to rgb
    rgbImg = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # When you call the process method on a FaceMesh object in MediaPipe, it processes the input image or video frame to detect faces and their landmarks.
    # returns a FaceMeshResults object containing information about the detected faces and their landmarks.
    output = faceLandmarks.process(rgbImg)


    # To access the landmarks for multiple faces, we used the multi_face_landmarks attribute of the FaceMeshResults object.
    # lmPoints will contain a list of landmark points for each detected face in the image.
    lmPoints = output.multi_face_landmarks

    if lmPoints:
        # form lmPoints we are only taking lamdmark points of the first face detected 
        lmarks = lmPoints[0].landmark
        for id, lmark in enumerate(lmarks):

            # the output of lmark.x/lmark.y gives a float value so we set it properly to be processed in our frame
            x = int(lmark.x * w)
            y = int(lmark.y * h)



            # MediaPipe uses the 468-point face landmark model, which includes points for various facial components like the eyes, 
            # eyebrows, nose, mouth, and face contour.
            # from that we use the landmark 43 for outer edge of the left eyebrow and
            # landmark 287 for outer edge of the right eyebrow, symmetrical to point 43.
            if id == 43:
                x1 = x
                y1 = y
            if id == 287:
                x2 = x
                y2 = y
        # calculating the euclidean distance between the two points
        dst = ((x2-x1) ** 2 + (y2-y1) ** 2) ** (0.5)
        # print(dst)


        # if the distance is larger then we click a picture
        if dst > 79:
            cv.waitKey(100)
            cv.imwrite('selfie.png', frame)
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
            cv.waitKey(100)

    cv.imshow('Smile to capture the image', frame)

    # if 'esc' key is pressed the exit the window
    key = cv.waitKey(100)
    if key == 27:
        break


# release the camera and close any OpenCV windows after completing operations
camera.release()
cv.destroyAllWindows()