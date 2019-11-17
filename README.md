# OBJECT_DETECTION
Simple Object Detection by using ImageAI via laptop camera

Set up Python 3.5: https://www.python.org/downloads/release/python-350/
CUDA Toolkit 9.0: https://developer.nvidia.com/cuda-90-download-archive
If there is an error about missing cudart64_100.dll, 
resolve it by unzipping cudart64_100.dll_.zip and copy it in ~/NVIDIA GPU Computing Toolkit/CUDA/v9.0/bin

1. Set up environments and required models:
 1.1. Tensorflow and Tensorflow-gpu: 1.4.0 or later versions, but MUSTE BE < 2.0
 1.2. The rest of libs: numpy, scipy, opencv-python, opencv-python, pillow, matplotlib, h5py, keras
      ImageAI:   pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl
      Install:   pip3 install tensorflow==1.xx     (E.g: 1.15)
                 pip3 install tensorflow-gpu==1.xx (E.g: 1.15)
                 pip3 install numpy
                 pip3 install scipy
                 pip3 install opencv-python
                 pip3 install opencv-python
                 pip3 install pillow
                 pip3 install matplotlib
                 pip3 install h5py
                 pip3 install keras
      If there is error when pip3 command does not recognize, you guy can use: 'python -m pip' instead of 'pip3'
      
  1.3. Download YOLOv3 model: https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
  
2. Put Yolov3 model (yolo.h5) in current dictionary which you clone
3. Arguments should be known:
   3.1: detection_speed: You can adjust speed by using one of these: "normal(defaul)", "fast", "faster" , "fastest", "flash"
   3.2: method .CustomObjects(): add object's name to detect what you want to
       Note: With some have more than 1 word, add underscore(_) between them. (E.g cell phone should be cell_phone)
       - List of object name:
          person,  bicycle,  car, motorcycle, airplane, bus, train,  truck,  boat,  traffic light,  fire hydrant, stop_sign,
          parking meter,   bench,   bird,   cat,   dog,   horse,   sheep,   cow,   elephant,   bear,   zebra,
          giraffe,   backpack,   umbrella,   handbag,   tie,   suitcase,   frisbee,   skis,   snowboard,
          sports ball,   kite,   baseball bat,   baseball glove,   skateboard,   surfboard,   tennis racket,
          bottle,   wine glass,   cup,   fork,   knife,   spoon,   bowl,   banana,   apple,   sandwich,   orange,
          broccoli,   carrot,   hot dog,   pizza,   donot,   cake,   chair,   couch,   potted plant,   bed,
          dining table,   toilet,   tv,   laptop,   mouse,   remote,   keyboard,   cell phone,   microwave,   oven,
          toaster,   sink,   refrigerator,   book,   clock,   vase,   scissors,   teddy bear,   hair dryer,   toothbrush.
       <check it here https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection>
   4. Have fun with this!
      
