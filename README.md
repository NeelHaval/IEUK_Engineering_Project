# Turbine Anomaly Detection

The project deals with the detection of turbines needing maintainance through a
set of metricspassed by a CSV file. Such a solution may be applied to any similar 
application which requires round the clock monitoring of large streams of data. 
A turbine is flagged as faulty if its average temperature exceeds 85°C or if its 
maximum vibration exceeds 15 mm/s.

## List of files relevant to the submission:

- `AnomalyDetection.py`
- `Dockerfile`
- `SystemArchitectureDiagram.png`
- `EngineeringReport.pdf`

## All files required in testing and running of the project:

- `AnomalyDetection.py`
- `Dockerfile`
- `README.md`
- `telemetry_data.csv`
- `Dependencies.txt`

Note that in the above `telemetry_data.csv` `Dependencies.txt` are required as
they allow access to data points and installation of dependencies respectively.

## Step by step instructions to run code:

docker build -t turbine-monitor .
docker run --rm turbine-monitor

**Note that the commands shown above must be typed exactly into the terminal or
command line interface to facilitate an environment for running the code.**

**Docker must be installed.**