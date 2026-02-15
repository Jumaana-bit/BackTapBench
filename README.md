# BackTapBench Standardized Dataset
## Overview
This dataset contains standardized back-of-device tap data for benchmarking tap recognition algorithms. It provides synchronized inertial sensor recordings captured during controlled tap gestures across multiple grid locations and participants. The dataset is suitable for classical machine learning, deep learning, and signal‑processing research.
## Purpose and Applications
BackTapBench enables reproducible research on back‑of‑device interaction by providing a unified dataset with consistent preprocessing, segmentation, and labeling. It is intended for:
- Tap‑recognition algorithm development
- Benchmarking across classical ML and deep learning models
- Sensor‑fusion research
- Gesture‑recognition studies
- Human–computer interaction (HCI) experimentation
- Rapid prototyping of mobile interaction techniques

## Data Collection Protocol
### Hardware
- **Device**: Samsung Galaxy Note 8
- **Operating System**: Android 9
- **Sensors Used**: Built-in accelerometer, gyroscope, and high-frequency accelerometer channels
- **Sampling Rate**: 120 Hz

### Collection Interface
A custom Android application was developed to guide participants during data collection. The app displayed a **3×3 grid overlay** on the back of the device, ensuring that participants tapped the correct grid location for each trial.

### Participant Instructions
All participants followed a standardized procedure:
- **Handedness**: Right hand
- **Finger**: Index finger
- **Grip**: Device held in one hand (the same hand performing the tap)
- **Posture**: Seated position
- **Environment**: Quiet indoor setting

Participants were instructed to tap naturally but consistently on the indicated grid location. Each tap was automatically segmented into a 60ms pre-tap window and a 200ms post-tap window.

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

## How to Reproduce
A full reproducibility pipeline, including preprocessing, segmentation, feature extraction, and benchmarking scripts, is available on GitHub:
**GitHub Repository:**
[link text](https://github.com/Jumaana-bit/BackTapBench.git)
The repsitory includes:
- End‑to‑end data loading and parsing scripts
- Benchmarking across classical ML and deep learning models
- Feature extraction code
- Classical ML and deep learning baselines
- Visualization notebooks
- Rapid prototyping of mobile interaction techniques
- Environment and dependency files

## Versioning
This dataset release corresponds to:
- **BackTapBench Standardized Dataset v1.0**
- Future updates (e.g., additional participants, new sensors, or expanded benchmarks) will be versioned and documented in the Dataverse version history. 

## License
This dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.
You are free to share and adapt the dataset, provided appropriate credit is given.

## Contact
For questions, corrections, or collaboration inquiries, please contact:

Jumaana Aslam

jumaana.aslam@gmail.com

## Citation
If you use this dataset, please cite:
```
BackTapBench: An Open Benchmark for Back-of-Device Tap Recognition
[Your Name], [Your Institution], [Year]
```
