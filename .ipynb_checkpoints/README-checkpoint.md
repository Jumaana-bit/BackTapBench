# BackTapBench Standardized Dataset
## Overview
This dataset contains standardized back-of-device tap data for benchmarking tap recognition algorithms.
## Dataset Statistics
- **Total segments**: 1299
- **Participants**: 5 (participant1, participant2, participant3, participant4, participant5)
- **Grid positions**: 9 (0-8)
- **Segment shape**: (31, 10) (samples × sensors)
- **Sampling rate**: 120 Hz
- **Segment duration**: 258ms (60ms pre-tap + 200ms post-tap)
## File Structure
```
backtapbench_standard/
├── backtapbench_data.npz          # Main dataset (segments, labels, participants, grids)
├── backtapbench_dataset.pkl       # Python pickle with all data
├── metadata.json                  # Detailed metadata for each segment
├── dataset_statistics.json        # Dataset statistics
├── dataset_summary.csv            # CSV summary
├── README.md                      # This file
├── features/                      # Extracted features for classical ML
│   ├── statistical_features.csv
│   ├── feature_matrix.npy
│   └── feature_names.json
└── splits/                        # Pre-defined dataset splits
    └── dataset_splits.json
```
## Data Format
### Main Dataset (backtapbench_data.npz)
```python
import numpy as np
data = np.load('backtapbench_standard/backtapbench_data.npz')
segments = data['segments']      # Shape: (n_samples, 31, 10)
labels = data['labels']          # Grid positions (0-8)
participants = data['participants']  # Participant IDs
grids = data['grids']            # Grid positions (same as labels)
```
### Sensor Channels
| Index | Sensor | Description |
|-------|--------|-------------|
| 0 | ax | Accelerometer X |
| 1 | ay | Accelerometer Y |
| 2 | az | Accelerometer Z |
| 3 | highX | High-frequency accelerometer X |
| 4 | highY | High-frequency accelerometer Y |
| 5 | highZ | High-frequency accelerometer Z (used for tap detection) |
| 6 | accelMag | Accelerometer magnitude |
| 7 | gx | Gyroscope X |
| 8 | gy | Gyroscope Y |
| 9 | gz | Gyroscope Z |
## Citation
If you use this dataset, please cite:
```
BackTapBench: An Open Benchmark for Back-of-Device Tap Recognition
[Your Name], [Your Institution], [Year]
```
