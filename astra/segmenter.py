import numpy as np
from loguru import logger
from typing import Tuple, List

class ProbabilityGridSegmenter:
    \"\"\"
    Astra-Inference Ground Segmenter using Probability Occupancy Grid logic.
    Optimized for high-speed processing of 3D point cloud data.
    \"\"\"
    def __init__(self, grid_size: float = 0.5, h_threshold: float = 0.3):
        self.grid_size = grid_size
        self.h_threshold = h_threshold
        logger.info(f"Initialized Astra Segmenter [Grid: {grid_size}m, Threshold: {h_threshold}m]")

    def segment(self, points: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        \"\"\"
        Segments points into Ground and Non-Ground.
        
        Args:
            points: Nx3 numpy array (x, y, z).
            
        Returns:
            Tuple: (ground_indices, obstacle_indices)
        \"\"\"
        if points.shape[1] < 3:
            raise ValueError("Input points must have at least 3 columns (x, y, z).")

        logger.debug(f"Segmenting {len(points)} points...")

        # 1. Create a 2D grid based on X and Y coordinates
        x_min, x_max = points[:, 0].min(), points[:, 0].max()
        y_min, y_max = points[:, 1].min(), points[:, 1].max()

        # 2. Assign each point to a grid cell
        grid_x = ((points[:, 0] - x_min) / self.grid_size).astype(int)
        grid_y = ((points[:, 1] - y_min) / self.grid_size).astype(int)
        
        # 3. Use unique grid IDs to group points
        grid_ids = grid_x * 10000 + grid_y # Simple unique ID for each cell
        unique_ids = np.unique(grid_ids)

        ground_mask = np.zeros(len(points), dtype=bool)

        # 4. Probabilistic elevation check for each cell
        # In a real production system, this would be vectorized or done in C++.
        for gid in unique_ids:
            cell_indices = np.where(grid_ids == gid)[0]
            cell_points = points[cell_indices]
            
            # Find the minimum Z in the cell (likely the ground)
            min_z = np.min(cell_points[:, 2])
            
            # Points within the height threshold from the minimum are ground
            ground_mask[cell_indices] = (cell_points[:, 2] - min_z) < self.h_threshold

        ground_idx = np.where(ground_mask)[0]
        obstacle_idx = np.where(~ground_mask)[0]

        logger.info(f"Segmented: {len(ground_idx)} ground, {len(obstacle_idx)} obstacles.")
        return ground_idx, obstacle_idx

# Astra Project Core