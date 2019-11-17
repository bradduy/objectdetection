from imageai.Detection import ObjectDetection
import os
import cv2

# Get current working directory of a process
executePath = os.getcwd()

objectDetector = ObjectDetection()
objectDetector.setModelTypeAsYOLOv3()
# Input parameter object's name
detectedTargets = objectDetector.CustomObjects(person=True, cell_phone=True)
# Get model yolo.h5 from the path above
objectDetector.setModelPath(os.path.join(executePath , "yolo.h5"))
# Adjust the detecting speed
objectDetector.loadModel(detection_speed="fastest")

# Main Process
vs = cv2.VideoCapture(0)
while True:
    check, frame = vs.read()
    cv2.imwrite("beforeDetectedImg.jpg", frame)
    detections = objectDetector.detectCustomObjectsFromImage(
        custom_objects=detectedTargets,
        input_image=os.path.join(executePath , "beforeDetectedImg.jpg"),
        output_image_path=os.path.join(executePath , "afterDetectedImage.jpg"),
        minimum_percentage_probability=20)
    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        print("--------------------------------")
    img = cv2.imread('afterDetectedImage.jpg')
    cv2.imshow('frame', img)
    key = cv2.waitKey(1)
    if key == ord("q"):
            break
cv2.destroyAllWindows()
vs.stop()