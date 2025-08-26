# Starlink Satellite Security Analysis

A comprehensive security research project investigating potential vulnerabilities in SpaceX's Starlink satellite constellation through systematic data analysis and network communication patterns.

## Project Overview

This project represents collaborative security research conducted with Dr. Antonio Bianchi at Purdue University, focusing on identifying potential security concerns within Starlink's satellite network infrastructure. The research combines satellite tracking, network analysis, and automated data collection to examine communication patterns and potential vulnerabilities that could reveal sensitive information about ground antenna locations.

The investigation demonstrates how packet loss patterns and satellite positioning data can potentially be exploited to determine the physical location of Starlink base antennas, highlighting critical security considerations for satellite-based internet infrastructure.

## Key Features

**Automated Satellite Data Collection**: Developed robust web automation scripts using Selenium to systematically extract real-time satellite positioning data from multiple sources, eliminating manual data collection bottlenecks.

**Advanced Satellite Tracking**: Implemented precise satellite coordinate calculations using the Skyfield library to track all 1,645+ Starlink satellites over extended time periods with high accuracy positioning.

**Network Communication Analysis**: Built a custom client-server architecture to simulate and analyze Starlink base antenna communication protocols, enabling controlled testing of network behavior patterns.

**Security Vulnerability Assessment**: Created algorithms to correlate packet loss percentages with satellite proximity data, revealing potential information leakage that could compromise antenna location privacy.

**Geospatial Analysis Tools**: Developed location tracking capabilities with Haversine distance calculations to analyze satellite coverage patterns and identify security implications of predictable communication windows.

## Technology Stack

**Programming Languages**: Python 3.x for all core functionality and data analysis workflows

**Web Automation**: Selenium WebDriver for automated satellite data extraction from CelesTrak

**Astronomical Computing**: Skyfield library for precise satellite ephemeris calculations and orbital mechanics

**Network Programming**: Custom UDP implementation for client-server communication modeling

**Data Analysis**: NumPy and standard Python libraries for statistical analysis of packet loss patterns

**Geospatial Computing**: Custom Haversine distance formula implementation for location-based calculations

## Prerequisites

Before running this security analysis toolkit, ensure your development environment meets these requirements:

```bash
Python 3.7 or higher
Chrome/Chromium browser (for Selenium automation)
Stable internet connection (for satellite data retrieval)
```

## Installation

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

## Usage

### Satellite Data Collection

Execute the automated data collection script to gather current satellite positioning information:

```bash
python webscript.py
```

This script will automatically navigate web interfaces and extract real-time satellite coordinates for the entire Starlink constellation through CelesTrak

### Network Communication Analysis

Start the client-server communication model to analyze base antenna behavior:

```bash
# Terminal 1: Start the server component
python server.py

# Terminal 2: Run the client analysis
python client.py

# Terminal 3: Run the script for parsing ping data
python ping_parser.py
```

### Security Analysis

Run the location tracking analysis to identify potential security vulnerabilities:

```bash
python location_tracker.py --north 42.5 --south 41.5 --east -90.0 --west -92.0
```

The security analysis will output packet loss percentages across a configurable grid pattern, demonstrating how communication patterns could potentially reveal antenna locations.

![Alt text]("/Packet Loss Percentages 10x10 Grid.png" "Packet Loss Percentages 10x10 Grid")

## Research Dataset

The project includes comprehensive satellite tracking data covering the period from July 25, 2021, to July 30, 2021, encompassing:

**Complete Satellite Coverage**: Tracking data for all 1,645 operational Starlink satellites during the analysis window

**Temporal Analysis**: Five-day continuous monitoring period capturing satellite movement patterns and coverage variations

**Packet Loss Correlation**: Statistical analysis of communication failures correlated with satellite positioning data

**Grid-based Location Analysis**: Systematic evaluation of packet loss patterns across a 10x10 geographical grid relative to true antenna positions

## Research Methodology

The security analysis follows a systematic approach to identify potential vulnerabilities in satellite communication systems. The methodology begins with comprehensive data collection, using automated tools to gather real-time satellite positioning information across the entire Starlink constellation. This data forms the foundation for subsequent analysis phases.

The research then employs network communication modeling to understand how ground antennas interact with overhead satellites. By implementing a controlled client-server environment, the study can systematically test communication patterns and identify correlations between satellite positions and network performance metrics.

The final phase involves statistical analysis of packet loss patterns, revealing how communication failures might inadvertently disclose information about ground antenna locations. This analysis demonstrates the critical importance of considering operational security implications in satellite internet infrastructure design.

## Acknowledgments

This research was conducted in collaboration with Dr. Antonio Bianchi at Purdue University as part of ongoing security research initiatives examining satellite communication infrastructure vulnerabilities.

## Research Ethics

This project is conducted for academic research purposes and responsible disclosure of potential security considerations. All analysis is performed using publicly available satellite tracking data and does not involve unauthorized access to any systems or networks.

## License

This research project is shared for educational and academic purposes. Please cite appropriately if using this work in academic or professional contexts.

---

*This project demonstrates advanced capabilities in security research, satellite communication analysis, and automated data collection - core competencies highly valued in cybersecurity and aerospace technology sectors.*
