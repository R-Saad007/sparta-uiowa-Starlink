# Starlink Satellite Security Analysis

A comprehensive security research project investigating potential vulnerabilities in SpaceX's Starlink satellite constellation through systematic data analysis and network communication patterns.

## 🎯 Project Overview

This project represents collaborative security research conducted with Dr. Antonio Bianchi at Purdue University, focusing on identifying potential security concerns within Starlink's satellite network infrastructure. The research combines satellite tracking, network analysis, and automated data collection to examine communication patterns and potential vulnerabilities that could reveal sensitive information about ground antenna locations.

The investigation demonstrates how packet loss patterns and satellite positioning data can potentially be exploited to determine the physical location of Starlink base antennas, highlighting critical security considerations for satellite-based internet infrastructure.

## 🚀 Key Features

**Automated Satellite Data Collection**: Developed robust web automation scripts using Selenium to systematically extract real-time satellite positioning data from multiple sources, eliminating manual data collection bottlenecks.

**Advanced Satellite Tracking**: Implemented precise satellite coordinate calculations using the Skyfield library to track all 1,645+ Starlink satellites over extended time periods with high accuracy positioning.

**Network Communication Analysis**: Built a custom client-server architecture to simulate and analyze Starlink base antenna communication protocols, enabling controlled testing of network behavior patterns.

**Security Vulnerability Assessment**: Created algorithms to correlate packet loss percentages with satellite proximity data, revealing potential information leakage that could compromise antenna location privacy.

**Geospatial Analysis Tools**: Developed location tracking capabilities with Haversine distance calculations to analyze satellite coverage patterns and identify security implications of predictable communication windows.

## 🛠️ Technology Stack

**Programming Languages**: Python 3.x for all core functionality and data analysis workflows

**Web Automation**: Selenium WebDriver for automated satellite data extraction from web interfaces

**Astronomical Computing**: Skyfield library for precise satellite ephemeris calculations and orbital mechanics

**Network Programming**: Custom UDP implementation for client-server communication modeling

**Data Analysis**: NumPy and standard Python libraries for statistical analysis of packet loss patterns

**Geospatial Computing**: Custom Haversine distance formula implementation for location-based calculations

## 📋 Prerequisites

Before running this security analysis toolkit, ensure your development environment meets these requirements:

```bash
Python 3.7 or higher
Chrome/Chromium browser (for Selenium automation)
Stable internet connection (for satellite data retrieval)
```

## 🔧 Installation

Clone the repository and set up the research environment:

```bash
git clone https://github.com/R-Saad007/sparta-uiowa-Starlink.git
cd sparta-uiowa-Starlink
```

Install the required Python dependencies:

```bash
pip install selenium skyfield numpy requests
```

Download and configure ChromeDriver for web automation:

```bash
# Download ChromeDriver matching your Chrome version
# Place in system PATH or project directory
```

## 🎮 Usage

### Satellite Data Collection

Execute the automated data collection script to gather current satellite positioning information:

```bash
python satellite_data_collector.py
```

This script will automatically navigate web interfaces and extract real-time satellite coordinates for the entire Starlink constellation.

### Network Communication Analysis

Start the client-server communication model to analyze base antenna behavior:

```bash
# Terminal 1: Start the server component
python server.py

# Terminal 2: Run the client analysis
python client.py
```

### Security Analysis

Run the location tracking analysis to identify potential security vulnerabilities:

```bash
python location_tracker.py --north 42.5 --south 41.5 --east -90.0 --west -92.0
```

The security analysis will output packet loss percentages across a configurable grid pattern, demonstrating how communication patterns could potentially reveal antenna locations.

### Data Visualization

Generate security assessment reports showing vulnerability patterns:

```bash
python analyze_packet_loss.py
```

## 📊 Research Dataset

The project includes comprehensive satellite tracking data covering the period from July 25, 2021, to July 30, 2021, encompassing:

**Complete Satellite Coverage**: Tracking data for all 1,645 operational Starlink satellites during the analysis window

**Temporal Analysis**: Five-day continuous monitoring period capturing satellite movement patterns and coverage variations

**Packet Loss Correlation**: Statistical analysis of communication failures correlated with satellite positioning data

**Grid-based Location Analysis**: Systematic evaluation of packet loss patterns across a 10x10 geographical grid relative to true antenna positions

## 🏗️ Project Architecture

```
sparta-uiowa-Starlink/
│
├── satellite_data_collector.py    # Automated web scraping for satellite data
├── server.py                      # UDP server for antenna communication modeling
├── client.py                      # Client component for network analysis
├── location_tracker.py            # Geospatial analysis and vulnerability assessment
├── analyze_packet_loss.py         # Statistical analysis of communication patterns
├── data/
│   ├── satellite_coordinates/     # Raw satellite positioning data
│   ├── packet_loss_analysis/      # Network communication analysis results
│   └── security_reports/          # Generated vulnerability assessments
└── README.md                      # Project documentation
```

## 🔬 Research Methodology

The security analysis follows a systematic approach to identify potential vulnerabilities in satellite communication systems. The methodology begins with comprehensive data collection, using automated tools to gather real-time satellite positioning information across the entire Starlink constellation. This data forms the foundation for subsequent analysis phases.

The research then employs network communication modeling to understand how ground antennas interact with overhead satellites. By implementing a controlled client-server environment, the study can systematically test communication patterns and identify correlations between satellite positions and network performance metrics.

The final phase involves statistical analysis of packet loss patterns, revealing how communication failures might inadvertently disclose information about ground antenna locations. This analysis demonstrates the critical importance of considering operational security implications in satellite internet infrastructure design.

## 🤝 Acknowledgments

This research was conducted in collaboration with Dr. Antonio Bianchi at Purdue University as part of ongoing security research initiatives examining satellite communication infrastructure vulnerabilities.

## ⚖️ Research Ethics

This project is conducted for academic research purposes and responsible disclosure of potential security considerations. All analysis is performed using publicly available satellite tracking data and does not involve unauthorized access to any systems or networks.

## 📄 License

This research project is shared for educational and academic purposes. Please cite appropriately if using this work in academic or professional contexts.

---

*This project demonstrates advanced capabilities in security research, satellite communication analysis, and automated data collection - core competencies highly valued in cybersecurity and aerospace technology sectors.*



# This repository contains
- UDP file transfer for Client/Server application
- Script for automation of web forms
- Starlink satellite data for all 1645 satellites for the time period: (2021-07-25) - (2021-07-30)
- Code for number of satellites present within a certain distance from the antenna with respect to time
- Contains code for calculating the percentage disconnections due to packet losses
- location_tracker.py has been updated, and contains the variables North, South, East, and West to be used as arguments for the Haversine distance formula calculator
- Contains the packet loss percentage data for a 10x10 grid relative to true antenna location
