# 📡 Antenna Radiation Pattern Visualizer

A Python-based tool for visualizing **E-field (Electric)** and **H-field (Magnetic)** radiation patterns for **Waveguide Linear Slot Array Antennas**. This project maps measured gain data (dB) onto a polar coordinate system for professional antenna analysis and reporting.

## 📌 Features
*   **Measurement Data Mapping**: Direct input of gain values (dB) from physical measurement tables.
*   **Beam Characteristic Simulation**: Accurately reflects peak directivity at $0^\circ$ and specific attenuation trends.
*   **Threshold-Based Plotting**: Implements a fixed $-10\text{dB}$ floor for angles beyond $\pm 18^\circ$ as per experimental specifications.
*   **Standardized Polar Plot**: Configured with $0^\circ$ at North (Up) and clockwise direction for industry-standard readability.

## 🛠 Tech Stack
*   **Language**: Python 3.x
*   **Core Libraries**: `NumPy`, `Matplotlib`

## 📊 Data Overview (E-field Sample)
Key measurement points extracted from the experimental data:


| Angle ($^\circ$) | Gain (dB) | Angle ($^\circ$) | Gain (dB) |
| :--- | :--- | :--- | :--- |
| **0 (Peak)** | **0.0** | **-1** | **-0.8** |
| 11 | -6.8 | -7 | -4.4 |
| 14 | -7.8 | -13 | -8.5 |
| **$\pm 18$ to $\pm 180$** | **-10.0** | **-18+** | **-10.0** |