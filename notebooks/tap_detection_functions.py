
# Tap Detection Functions (from 02_tap_detection_validation.ipynb)

import numpy as np
from collections import deque

def detect_taps_in_signal(highZ, gyro_mag, window_size=6, z_threshold=3.0, 
                         gyro_threshold=1.0, debounce_samples=14):
    """
    Detect tap positions using Z-energy algorithm
    """
    n = len(highZ)
    energy_window = deque(maxlen=window_size)
    tap_indices = []
    last_tap_idx = -debounce_samples
    
    for i in range(n):
        energy_window.append(highZ[i])
        
        if len(energy_window) < window_size:
            continue
            
        energyZ = np.mean(np.array(energy_window)**2)
        
        if (energyZ > z_threshold and 
            gyro_mag[i] < gyro_threshold and 
            (i - last_tap_idx) > debounce_samples):
            
            tap_indices.append(i)
            last_tap_idx = i
    
    return tap_indices

def extract_tap_segments(df, tap_indices, pre_samples=7, post_samples=24, 
                        sensor_cols=None):
    """
    Extract segments around detected tap positions
    """
    if sensor_cols is None:
        sensor_cols = ['ax', 'ay', 'az', 'highX', 'highY', 'highZ', 
                      'accelMag', 'gx', 'gy', 'gz']
    
    segments = []
    n = len(df)
    target_length = pre_samples + post_samples
    
    for tap_center in tap_indices:
        start_idx = max(0, tap_center - pre_samples)
        end_idx = min(n, tap_center + post_samples)
        
        segment = df.iloc[start_idx:end_idx][sensor_cols].to_numpy()
        
        # Pad if necessary
        if len(segment) < target_length:
            pad_before = pre_samples - (tap_center - start_idx)
            pad_after = post_samples - (end_idx - tap_center)
            segment = np.pad(segment, 
                            ((pad_before, pad_after), (0, 0)), 
                            mode='edge')
        
        segments.append(segment)
    
    return segments
