# Player Detection and Tracking with YOLOv11 + StrongSORT + OSNet

![Tracking Demo](Test/embedd.gif)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pranavv11/Object-Detection-Tracking/blob/main/Object-Detection-Tracking/Tracker.ipynb)

# Introduction
This project performs **player detection and tracking** on football match videos in `.mp4` format.
It uses a custom-trained [YOLOv11](https://github.com/ultralytics/ultralytics) model to detect multiple players in each frame. For robust tracking, it integrates the [StrongSORT](https://github.com/mikel-brostrom/boxmot) algorithm, enhanced with a [OSNet](https://github.com/KaiyangZhou/deep-person-reid) Re-Identification (ReID) model. This combination helps maintain consistent player IDs across frames and reduces ID switches during partial occlusions.

# Steps to run the tracker
1. Clone the Repository (with Git LFS support)
   To properly download the pretrained model weights, ensure you have Git LFS installed:
   <pre><code>git lfs install
   git clone https://github.com/pranavv11/Object-Detection-Tracking.git
   </code></pre>
2. Clone the Yolov7_StrongSORT_OSNet repository and set directory
   <pre><code>git clone https://github.com/mikel-brostrom/Yolov7_StrongSORT_OSNet.git
   </code></pre>
3. Install all the dependencies
   <pre><code>pip install -r requirements.txt</code></pre>
   or
    <pre><code>pip install .</code></pre>
4. Download the required model weights from **[osnet_x0_25_msmt17.pt](https://github.com/KaiyangZhou/deep-person-reid)**
   
5. Prepare the test video in `.mp4` format
   
6. Run the tracking command in terminal
<pre> <code> boxmot track Models/yolov8_best.pt
        Models/osnet_x0_25_msmt17.pt 2 
      --source Test/15sec_input_720p.mp4
      --conf 0.62 
      --iou 0.5 
      --save 
      --project Output 
      --name run1
      --verbose 
</code></pre>
7. Find your output
 <pre>Yolov7_StrongSORT_OSNet/Output/run1/15sec_input_720p.avi</pre>
8. Tune StrongSORT behavior (Optional)
To improve tracking quality or reduce identity switches, you can pass additional parameters via command line or change them in source code:
<pre>
a. --max-ageNumber of frames to keep lost tracks alive
b. --nn-budget: ReID gallery size
c. --max-iou-dist: Controls how strictly tracks are associated
</pre>
