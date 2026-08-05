# FAST-LIVO2

## FAST-LIVO2: Fast, Direct LiDAR-Inertial-Visual Odometry

### 📢 News

- 🔓 **2025-01-23**: Code released!  
- 🎉 **2024-10-01**: Accepted by **T-RO '24**!  
- 🚀 **2024-07-02**: Conditionally accepted.

### 📬 Contact

For further inquiries or assistance, please contact [zhengcr@connect.hku.hk](mailto:zhengcr@connect.hku.hk).

## 1. Introduction

FAST-LIVO2 is an efficient and accurate LiDAR-inertial-visual fusion localization and mapping system, demonstrating significant potential for real-time 3D reconstruction and onboard robotic localization in severely degraded environments.

**Developer**: [Chunran Zheng](https://github.com/xuankuzcr)

## KangjianPeng Fork Changes

This fork provides the ROS 2 Humble port of FAST-LIVO2, including ROS 2
interfaces, `ament_cmake` build files, and ROS 2-compatible Vikit and Sophus
submodules. The mapping node publishes `/aft_mapped_to_init` as
`nav_msgs/msg/Odometry` with covariance values populated from the FAST-LIVO2
EKF state: position and orientation covariance come from the pose state,
linear velocity covariance comes from the velocity state, and angular
velocity covariance uses the configured gyroscope variance.

The fork also includes a Gazebo Sim configuration for the simulated camera,
IMU, and Mid-360 input stream. Start it with
`ros2 launch fast_livo mapping_gazebo.launch.py rviz:=true` after building and
sourcing the workspace.

<div align="center">
    <img src="pics/Framework.png" width = 100% >
</div>

### 1.1 Related video

Our accompanying video is now available on [**Bilibili**](https://www.bilibili.com/video/BV1Ezxge7EEi) and [**YouTube**](https://youtu.be/6dF2DzgbtlY).

### 1.2 Related paper

[FAST-LIVO2: Fast, Direct LiDAR-Inertial-Visual Odometry](https://arxiv.org/pdf/2408.14035)  

[FAST-LIVO2 on Resource-Constrained Platforms](https://arxiv.org/pdf/2501.13876)  

[FAST-LIVO: Fast and Tightly-coupled Sparse-Direct LiDAR-Inertial-Visual Odometry](https://arxiv.org/pdf/2203.00893)

[FAST-Calib: LiDAR-Camera Extrinsic Calibration in One Second](https://www.arxiv.org/pdf/2507.17210)

### 1.3 Our hard-synchronized equipment

We open-source our handheld device, including CAD files, synchronization scheme, STM32 source code, wiring instructions, and sensor ROS driver. Access these resources at this repository: [**LIV_handhold**](https://github.com/xuankuzcr/LIV_handhold).

### 1.4 Our associate dataset: FAST-LIVO2-Dataset
Our associate dataset [**FAST-LIVO2-Dataset**](https://connecthkuhk-my.sharepoint.com/:f:/g/personal/zhengcr_connect_hku_hk/ErdFNQtjMxZOorYKDTtK4ugBkogXfq1OfDm90GECouuIQA?e=KngY9Z) used for evaluation is also available online.

### 1.5 Our LiDAR-camera calibration method
The [**FAST-Calib**](https://github.com/hku-mars/FAST-Calib) toolkit is recommended. Its output extrinsic parameters can be directly filled into the YAML file. 

## 2. Prerequisites

### 2.1 Ubuntu and ROS

Ubuntu 22.04 with [ROS 2 Humble](https://docs.ros.org/en/humble/Installation.html).

### 2.2 PCL && Eigen && OpenCV

PCL>=1.8, Follow [PCL Installation](https://pointclouds.org/). 

Eigen>=3.3.4, Follow [Eigen Installation](https://eigen.tuxfamily.org/index.php?title=Main_Page).

OpenCV>=4.2, Follow [Opencv Installation](http://opencv.org/).

### 2.3 Sophus

Sophus Installation for the non-templated/double-only version.

```bash
git clone https://github.com/strasdat/Sophus.git
cd Sophus
git checkout a621ff
mkdir build && cd build && cmake ..
make
sudo make install
```

### 2.4 Vikit

Vikit contains the camera models and vision utilities used by FAST-LIVO2. The
ROS 2-compatible source revision is pinned as a Git submodule and built as part
of this package; no system-wide Vikit installation is required.

```bash
git submodule update --init --recursive
```

### 2.5 Livox message compatibility

This ROS 2 branch generates the Livox custom point-cloud interfaces directly
from [`msg/CustomPoint.msg`](msg/CustomPoint.msg) and
[`msg/CustomMsg.msg`](msg/CustomMsg.msg). Their fields and serialization order
match the original `livox_ros_driver/CustomPoint` and
`livox_ros_driver/CustomMsg` definitions bundled by upstream FAST-LIVO2.

The generated ROS 2 topic type is:

```text
fast_livo/msg/CustomMsg
```

The former `include/livox_ros_driver/Custom*.h` files were ROS 1 `gencpp`
output and depended on ROS 1 serialization headers. They are intentionally not
used or shipped by this ROS 2 branch.

ROS middleware matches both topic name and message type. A ROS 1 bag or a ROS
2 driver publishing `livox_ros_driver2/msg/CustomMsg` must therefore be
converted or adapted to `fast_livo/msg/CustomMsg`; changing only the topic name
is not sufficient.

## 3. Build

Clone this ROS 2 branch together with its submodules, then build with colcon:

```bash
git clone --recurse-submodules -b humble \
  https://github.com/KangjianPeng/FAST-LIVO2.git
cd FAST-LIVO2
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```

## 4. Run our examples

Download FAST-LIVO2-Dataset from [Global-LVBA](https://github.com/xuankuzcr/Global-LVBA) Section IV.

```bash
ros2 launch fast_livo mapping_avia.launch.py rviz:=true
ros2 bag play YOUR_ROS2_BAG
```


## 5. License

The source code of this package is released under the [**GPLv2**](http://www.gnu.org/licenses/) license. For commercial use, please contact me at <zhengcr@connect.hku.hk> and Prof. Fu Zhang at <fuzhang@hku.hk> to discuss an alternative license.
