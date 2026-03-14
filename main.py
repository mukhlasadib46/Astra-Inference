import numpy as np
import open3d as o3d
from loguru import logger
from astra.segmenter import ProbabilityGridSegmenter

def create_sample_pcd(num_points: int = 10000):
    \"\"\"
    Generates a synthetic point cloud with a ground plane and some random obstacles.
    \"\"\"
    # Create a ground plane
    ground_x = np.random.uniform(-10, 10, num_points // 2)
    ground_y = np.random.uniform(-10, 10, num_points // 2)
    ground_z = np.random.normal(0, 0.05, num_points // 2) # Flat ground with small noise
    
    # Create some obstacles (blocks)
    obs_x = np.random.uniform(-5, 5, num_points // 2)
    obs_y = np.random.uniform(-5, 5, num_points // 2)
    obs_z = np.random.uniform(0, 2, num_points // 2) # Points above ground
    
    points = np.vstack([
        np.column_stack((ground_x, ground_y, ground_z)),
        np.column_stack((obs_x, obs_y, obs_z))
    ])
    return points

def main():
    logger.info("Starting Astra-Inference Demo Pipeline...")

    # 1. Generate or load data
    points = create_sample_pcd()
    
    # 2. Initialize Segmenter
    segmenter = ProbabilityGridSegmenter(grid_size=0.5, h_threshold=0.2)
    
    # 3. Run Segmentation
    ground_idx, obstacle_idx = segmenter.segment(points)

    # 4. Visualize (in a real environment, we'd save or send to perception stack)
    logger.info("Astra segmentation complete. Visualizing results...")
    
    # Create Open3D objects
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    
    # Colorize: Ground=Green, Obstacles=Red
    colors = np.zeros_like(points)
    colors[ground_idx] = [0, 1, 0] # Green
    colors[obstacle_idx] = [1, 0, 0] # Red
    pcd.colors = o3d.utility.Vector3dVector(colors)

    print("\n--- ASTRA-INFERENCE OUTPUT ---")
    print(f"Total Points: {len(points)}")
    print(f"Ground: {len(ground_idx)}")
    print(f"Obstacles: {len(obstacle_idx)}")
    print("------------------------------\n")

    # In a real environment, you'd call o3d.visualization.draw_geometries([pcd])
    # For now, we simulate a successful completion.
    logger.success("Pipeline finished successfully.")

if __name__ == "__main__":
    main()