# 🌌 Astra-Inference
### *High-Performance 3D LiDAR Ground Segmentation*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![LiDAR](https://img.shields.io/badge/Sensor-LiDAR%203D-lightgrey.svg)]()
[![Algorithm](https://img.shields.io/badge/Algorithm-Probability%20Occupancy%20Grid-red.svg)]()

**Astra-Inference** is a specialized 3D point cloud processing engine designed for autonomous vehicle perception. It implements a robust **Probability Occupancy Grid** algorithm to efficiently segment ground points from obstacles in real-time, even in complex urban or off-road environments.

## 🌟 Key Features
- **Probability Occupancy Grid Segmentation**: A mathematical approach to ground detection that handles sensor noise and varying point densities.
- **Fast Voxel Downsampling**: Optimized spatial indexing to reduce computational load without losing critical geometric features.
- **Elevation Mapping**: Dynamic thresholding based on local height distributions to handle slopes and uneven terrain.
- **Real-time 3D Visualization**: Built-in support for Open3D to inspect segmentation results in a 3D environment.

## 🧠 Core Algorithm: Probability Occupancy Grid
Unlike simple height-thresholding, Astra-Inference treats each cell in a polar or Cartesian grid as a probabilistic entity. The ground is identified by analyzing the variance and mean elevation within these cells:

 P(Ground | Cell) = \exp \left( -\frac{(h - \mu)^2}{2\sigma^2} \right) 

*(Note: LaTeX visualization supported in most Markdown viewers)*

## 🚀 Quick Start
1. **Clone the Repo**
   `ash
   git clone https://github.com/mukhlasadib46/Astra-Inference.git
   cd Astra-Inference
   `

2. **Install Dependencies**
   `ash
   pip install -r requirements.txt
   `

3. **Run Demo**
   `ash
   python main.py --input ./data/sample_cloud.pcd
   `

## 🏗️ Project Structure
- stra/: Core algorithmic implementations.
- examples/: Sample scripts and data loaders.
- utils/: Coordinate transformation and point cloud helpers.

## 🤝 About the Author
**Mukhlas Adib Rasyidy** is a Machine Learning Engineer specializing in computer vision and LiDAR processing for autonomous systems. This project is inspired by his research in real-time 3D perception.

---
*Precision. Performance. Perception.*