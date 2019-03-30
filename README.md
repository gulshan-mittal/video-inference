# video-inference 

Using this repository one can make inferences on video like Object detection, instance segmentation . 

The current modules includes:

*  ObjectDetection
  * YOLOv3
  * Mask-RCNN



### Requirements

* OpenCV



### Creating A Virtual environment and Install OpenCV

```bash
virtualenv -p /usr/bin/python3.5 venv
source venv/bin/activate
pip3 install opencv-python
```

* if you need both main and contrib modules then run following command

```
pip3 install opencv-contrib-python
```



### Running the Inferences

* Clone the repository with the following command

```bash
git clone https://github.com/gulshan-mittal/video-inference.git
cd video-inference
```

* Download the pre-trained models

```bash
chmod a+x download_model.sh
./download_model.sh
```

* Run the following command to make inference

  * Object detection using YOLOv3

    ```shell
    python3 video_inference.py --task ObjectDetection --network "YOLOv3" --input /Path/to/Input/Video/ --output ./Path/to/Output/Folder/
    ```

  * Object detection using Mask-RCNN

    ```shell
    python3 video_inference.py --task ObjectDetection --network "Mask-RCNN" --input /Path/to/Input/Video/ --output ./Path/to/Output/Folder/
    ```

### Results (Sample Inferences)
* Yolov3
  
  ![](https://github.com/gulshan-mittal/video-inference/blob/master/results/YOLOv3-min.gif)

