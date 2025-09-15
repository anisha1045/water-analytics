
# Project Overview

This project is a prototype for Utilyze, a water analytics platform. The goal is to analyze water data from utility companies and send alerts to users about potential issues like leaks.

## Tech Stack

- **Backend:** Python
- **Frontend:** Next.js (if necessary)
- **Database:** The system should be designed to be compatible with Snowflake for future data retrieval from utility companies.

## Target Audience

- Homeowners
- Apartment tenants
- Landlords

## Communication Style

- All user-facing alerts (text or email) should be concise, easy to understand, and avoid technical jargon.

## Data Requirements

The following data is needed for model training and analysis:

- **Location Data:** To determine the location for weather data retrieval.
- **Weather Data:** Used as input for the burst pipe prediction model.
- **Water Flow Data:** Real-time or near-real-time water usage data.
- **Historical Water Usage Data:** To establish a baseline for normal water usage patterns at a specific location.

## Core Deliverables

### Code

1.  **Burst Pipe Prediction Model:** Train a machine learning model to predict the likelihood of burst pipes based on weather data.
2.  **Abnormal Water Usage Detection Model:** Train a machine learning model to detect anomalies in water usage.
3.  **User Notification System:** Implement a system to send email or text alerts to users when the backend flags a potential leak or abnormal usage.

### Demos

- The development team will produce weekly demo videos to showcase project progress.
- Weekly development goals should be planned to ensure a demonstrable product update is ready by the end of each week.

### Output
- When generating code that contains machine learning models or other similar predictive models, the code should be trained on one of the water usage datasets listed in data-sources.txt. The model should then be run on the training data, and the training error should be reported as part of the output. Report the training error as a proportion of training data.
