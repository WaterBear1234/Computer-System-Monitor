# Computer System Monitor

**System Monitor** is a lightweight tool that records system metrics (CPU and memory usage) and visualizes the performance data.

The system records metrics every **6 seconds** (1-second CPU sampling + 5-second sleep interval).

## Project Overview
* **Logging:** Metrics are stored in `logs/system_usage.csv`.
* **Visualization:** A separate script reads the CSV and saves a time-series plot to `plots/system_usage.png`.

## Tech Stack
* **[psutil](https://psutil.readthedocs.io/):** Reading system metrics (CPU/RAM).
* **[pandas](https://pandas.pydata.org/):** Data handling and CSV logging.
* **[matplotlib](https://matplotlib.org/):** Plotting data.
* **os:** Automatic folder creation.

## Installation

### 1. Clone the repository
```git clone https://github.com/WaterBear1234/Computer-System-Monitor.git```
```cd system_monitor```

### 2. Create and activate a virtual environment
```python -m venv venv```

\# macOS / Linux

```source venv/bin/activate```

\# Windows

```venv\Scripts\activate```

### 3. Install dependencies
```pip install psutil pandas matplotlib```

## Usage

### Start Logging
Run the monitor script to start recording data:

```python monitor.py```

**This script will**:
* Create a ```logs/``` directory if it doesn't exist.
* Create ```system_usage.csv``` if missing.
* Append a new row of data every 6 seconds.
* **Stop:** Press ```Ctrl + C``` to stop logging.

### Generate Performance Plot
Run the plotting script to visualize the data:

```python plot_data.py```

**This script will:**
* Read data from ```logs/system_usage.csv```.
* Generate and save the plot to ```plots/system_usage.png```.
* Display the graph in a window (if supported by your OS).

## Roadmap & Future Work
### Future Improvements
* Live plotting (Real-time updates)
* GPU monitoring support
* Configurable sampling intervals via CLI
* Alert notifications for high usage
* Web dashboard implementation
### Tests
* Validate correct CSV header format
* Mock ```psutil``` output for predictable testing
* Test plotting functionality in headless mode

## Credits
**Author:** Bui Hoang My Linh
**Libraries Used:**
* ```psutil```
* ```pandas```
* ```matplotlib```
* ```csv, os, datetime```

## License
This project is licensed under the MIT License.
