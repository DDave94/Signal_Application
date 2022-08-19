# Signal Analyzer App

## Table of Contents 
* [General Info] (#general-info)
* [Setup] (#setup)
* [Potenial Optimizations] (#setup)

## General Info
This project is a simple RESTful API application which computes the dominant frequency for 1D signals. 
Constructed using the FastAPI framework and dockerized to run in any environment. 
Application File Structure: 
'''bash
    .
    ├── data                                    # Contains input signal data pickle files
    ├── Dockerfile                              # Building docker image and configuration
    ├── docker-compose.yml                      # Run Docker container
    ├── main.py                                 # Source Code
    ├── requirements.txt                        # Contains required libs for docker
    └── README.md
'''

## Setup
Process to run the application: 
- Install Docker Desktop
- Navigate to the application directory containing file structure in command prompt or terminal 
- Run the following command
    - 'docker compose up'
- When the application is running, open browser and navigate to http://0.0.0.0:9000/docs

- In another bash terminal window run the following commands: 
    - 

Alternative Checking
- Perform the following operations to compute dominant frequency:
    - Locate the POST (/input) endpoint
        - Click "Try it Out". Browse to provide the pickle file in the data folder and execute
        - Verify the response is an appropriate signal of float elements 
    - Locate the GET (/dominant_frequence) endpoint
        - Click Execute 
        - Verify the response contains the dominant frequency of 320.0 Hz
    