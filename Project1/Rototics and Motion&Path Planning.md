# Rototics and Motion/Path Planning


% I.→1.→(1)
### I.Problem Statement:  
(What does the topic cover? Why it is important?)

This topic can be basically divided into two parts:
* The Soul-Robot data processing, the key problem: image processing, point cloud processing, target recognition and machine learning
* The Body-Robot interacts with the physical world: robotic arm motion algorithm, movement algorithm, end-of-freedom design

I think that the first part, that is, the robot vision and machine learning algorithm part is the core part, it contains methods for the robot camera to obtain 2D image, 3D depth image, points cloud and further processing. This part is an important prerequisite for robot target recognition and corresponding feedback. After obtaining high-quality image or point cloud data, the machine learning model that has been trained is recognized, and finally the target information is returned, such as what the object is, the position and posture information of the object, etc.

The other part is the motion algorithm when the robot interacts with the physical world. After the robot obtains the recognition result, it must perform specified operations on the target. The realization of these operations requires appropriate navigation methods, robotic arm motion planning, and flexible operation technology. We can almost say that where there are people working, robots can go to work in this place, and even where people can’t reach, robots can also reach there and perform work. This means that, first, robots can assist humans in completing tasks in a large number of fields and scenarios and improve work efficiency and accuracy, second, special robots designed for special environments can work in extreme scenarios to prevent humans from being dangerous. We can give examples based on scenarios. For example, in a precision processing factory, such as chip processing and drug processing, every step of the operation requires extremely high precision. But humans often cannot do such precise operations, so factories can choose robots to operate, from identifying the operating area to completing the operation, and humans only need to adjust the robots and check the correctness of the results.

### II.Applications
(What are applications of the topic? What is the societal significance of the research?)

There are many applicable scenarios and fields for this theme. The following include medical scenarios, manufacturing and processing scenarios, and life service scenarios. In addition to the above, it also includes a variety of special environments.

* Medical scenarios: compound medical robots, laparoscopic surgery robots. The compound medical robot refers to the service assistant robot in the medical field, which is mainly used for the assistance of the inpatient department and the auxiliary work of the non-surgical field, such as guiding patients to seek medical treatment by themselves. The current development of surgical robots is still dominated by surgeons. For example, the Da Vinci laparoscopic robot and the Chinese ‘Miaoshou-S’ laparoscopic robot generally cannot make autonomous judgments, but they can be controlled by humans and made precise movements by the operating end with a high degree of freedom. The recognition of irregular organ images and lesion images is thrown in the research. Due to the inexplicability of computer-aided diagnosis and the huge amount of data of three-dimensional images (such as MRI), there is still a lot of room for development in this area ("Prometheus"). '' in the emergency medical warehouse). The recognition of irregular organ images and lesion images is still under study. Due to the inexplicability of computer-aided diagnosis and the huge amount of data in three-dimensional images (such as MRI), there is still a lot of room for development in this area (refer to the emergency medical warehouse in movie "Prometheus").

* Industrial assembly line: chip processing, medicine processing, machine manufacturing. Both chip and drug processing are precision technologies, and as the demand increases, any small error will cause huge losses. In drug processing, the added amount of a certain drug can be calculated and measured by the robot's high-speed camera and adjusted in real time.

* Life services: smart logistics, contactless transportation (COVID-19), unmanned driving. In the foreseeable next few years, COVID-19 will always coexist with humans. With the birth of COVID-19, the corresponding safety measures include contactless unmanned vehicles, such as the "kuafu" unmanned vehicle developed by the Hong Kong University of Science and Technology. Similarly, unmanned technology companies have sprung up like bamboo shoots. Unmanned vehicles need to model the surroundings through images or lasers, and make autonomous driving judgments through real-time recognition of surrounding objects.

* Special fields: underwater exploration, military, rescue, outer space, (some extreme areas that are dangerous to humans or cannot be reached by humans)

So what is the societal significance of the research?

1. Improve productivity. Further improve the working efficiency of the robot, broaden the working field of the robot, and improve the accuracy of operation.
2. Assist the development of the medical industry. Share the work pressure of doctors, assist in medical diagnosis, and provide higher-level medical services for remote areas.
3. Improve people's quality of life. Promote the development of contactless transportation and unmanned driving, and expand the development and construction of human beings in extreme fields.
4. Promote the development of robotics and related disciplines, such as materials science, mechanical structure, computer vision, machine learning, motion dynamics, etc.
5. However, the cost of each robot is very high, and the maximum benefit is the key to the popularization and development of hand-eye robots.

### III.Pick an area of focus that interests you in the topic

As I mentioned before, the core problem of the hand-eye robot is The Soul. How to get closer to the real-life recognition target, and how to make accurate and precise operations after recognizing the target is a problem we need to consider. And I think that the point cloud data contains more information such as the depth of the object than the two-dimensional image. It can provide more operation information for the hand-eye robot and can be used as the input of the deep learning model. So 3D point cloud recognition will be my entry point.

### IV.Literature review
(As comprehensive as you can, research the different approaches and solutions in research community and industry)

The following includes a brief description of some papers and patents.

1.Ming L.[1] first built a binocular stereo vision platform and calibrated to collect the point cloud data of the target scene, and performed conditional filtering, voxel filtering and statistical filtering on the original point cloud data to obtain the preprocessed point cloud data. Secondly, based on the PointNet point cloud classification network, the MV-Point Net network model is proposed. The network uses multi-view point cloud data as the network input, and uses View-Pooling to aggregate multi-view features. The model uses different View-Pooling methods and the number of angles of view to evaluate the experiment, and compared with Point Net, on the data based on the Model Net data set to obtain 86.5% of the recognition accuracy rate.

2.Bin L.[2] invented a target recognition and monitoring method based on LiDAR point cloud data, including the following steps: 
(1) Use lidar to detect substation workers to obtain sparse point cloud data, and feed the original point cloud data representing three-dimensional geometric information to the PointRCNN neural network to extract features. In the first stage, the former scenic spots are extracted and the region of interest RoI is generated, and the generated frame is refined in the second stage; The feature extraction network of the PointRCNN is a network based on PointNet++, and the feature extraction part is composed of multi-layer perception (MLP), T-Net and Max-pooling layers;
(2) Use a layer-based accumulation module to accumulate point cloud data to enhance the semantic information of the object;
(3) Use the random forest algorithm to classify the features and determine whether the staff wears a helmet;

### V.Open Source research
(Research the different open source projects that touch the topic of your interest, Duplicate the results)

By reading our papers and patents, we can find that the point cloud recognition solutions will be related to "1. Radar data input 2. Point cloud data filtering 3 Using PointNet or PointNet++ and other feature classification networks for recognition" 
In order to be able to transplant the project more conveniently, especially to transplant this function to the robot, I think ROS is the most suitable development platform, and ROS itself includes the 3D point cloud processing program rviz, which can assist us in processing point cloud data.
I found this open source project on GitHub: https://github.com/AmeyaWagh/3D_object_recognition.
The Python version used in this project is 2.7. If we want to learn this project, it is best to try to update the Python version to 3.x. Similarly, the author has updated openCV2 to openCV3. The ROS project is generally divided into nodes, and each node is controlled by the node manager ROSmaster. The project is divided into the following nodes: 
·	tf_emitter 
·	segmentationNode
·	classifierNode
·	RViz
·	pcd_to_pointcloud
The running file is roslaunch robot_vision robot_vision3.launch, training classifier: rosrun robot_vision trainer.py, training dataset open source has provided.

#### reference

[1]	Li Ming. Target recognition and pose estimation based on stereo vision [D]. Huazhong University of Science and Technology, 2020.

[2]	Liu Bin, Xiong Guoyou, Gao Purun, Lu Bo, Yang Zeming, Yang Bin, Cao Tianen, Yang Guangcan, Yang Tao, Hu Fangfang. A target recognition and monitoring method based on LiDAR point cloud data [P]. Hubei Province: CN113298163A, 2021-08-24.
