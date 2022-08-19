# Signal Analyzer App

## Table of Contents
1. [Project](#project)
2. [Setup](#setup)
3. [Potential Optimizations](#potential-optimizations)

## Project
This project is a simple RESTful API application which computes the dominant frequency for 1D signals. 
Constructed using the FastAPI framework and dockerized to run in any environment. 
Application has two main endpoints: 
1. POST '/input': Accepts list of float numbers in pickle format and performs signal object creation
2. GET '/dominant_frequency': Returns the dominant frequency for the 1D signal

File Structure: 
```
project
├── data                                    # Contains input signal data pickle files
├── Dockerfile                              # Building docker image and configuration
├── docker-compose.yml                      # Run Docker container
├── main.py                                 # Source Code
├── requirements.txt                        # Contains required libs for docker
└── README.md
```

## Setup
Process to run the application: 
- Install Docker Desktop
- Navigate to the application directory containing file structure in command prompt or terminal 
- Run the following command
    - 'docker compose up'
- When the application is running, open browser and navigate to http://0.0.0.0:9000/

Process to provide signal inputs and find dominant frequency:
- Open terminal window and run the following command: 
```
curl -X 'POST' \
  'http://0.0.0.0:9000/input' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@./{insert_your_file_path}/sampleSigData.pickle'
```
This should create a signal object resource on the server

- In the same terminal window and run the following command: 
```
curl -X 'GET' \
  'http://0.0.0.0:9000/dominant_frequency' \
  -H 'accept: application/json'
```
This should compute the dominant frequency and provide the following response: 
"The dominant frequency of signal is 320.0"

Alternative process to provide signal data and compute frequency 
- Navigate to http://0.0.0.0:9000/docs in your browser
- Perform the following operations to compute dominant frequency:
    - Locate the POST (/input) endpoint
        - Click "Try it Out". Browse to provide the pickle file in the data folder and execute
        - Verify the response is an appropriate signal of float elements 
    - Locate the GET (/dominant_frequence) endpoint
        - Click Execute 
        - Verify the response contains the dominant frequency of 320.0 Hz
    
## Potential Optimizations
- Replacing the pickle list into an array to reduce memory usage
- Change the 
