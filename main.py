"""
Signal Analyzer Exercise
Description: 
    RESTful API application which computes the dominant frequency for 1D signal
    Application has two main endpoints: 
        1. POST '/input': Accepts list of float numbers in pickle format and performs signal object creation
        2. GET '/dominant_frequency': Returns the dominant frequency for the 1D signal
Author: Dhanya Dave 
Date: Aug 19, 2022
"""
import random
import shutil
import uvicorn
import pickle
from typing import Union
from fastapi import FastAPI, UploadFile, File, HTTPException
import numpy as np

#Creating application and signal data object 
app = FastAPI(title = "Signal Analyzer")
sigObjects = []
 
class Signal():
    """ 1D signal class, handles signals represent using lists
        and computes dominant frequency for a given signal

    Attributes: 
        data: A list of float elements representing 1D signal
        dom_freq: Dominant frequency pertaining to the signal
    """
    def __init__(self, data):
        """Instantiating a signal using list data"""
        self.data = data
        self.dom_freq = None
    
    def compute(self):
        """Computing Dominant Frequency of 1D signal data attribute"""
        sampling_rate = 1000
        # Gathering time data values
        td = self.data
        # Computing 1D Fourier Transform and acquiring 1D discrete-time sample frequencies
        fft_data = np.fft.fft(td)
        freqs = np.fft.fftfreq(len(td))
        # Finding index of peak frequency and computing dominant frequency
        peak_td = np.argmax(np.abs(fft_data))
        peak_freq = freqs[peak_td]
        self.dom_freq = abs(peak_freq * sampling_rate)
        return self.dom_freq

@app.get('/')
def root() -> dict:
    """Root Get"""
    return {"Welcome to Signal Analyzer"}


@app.post('/input')
async def add_signal(file: UploadFile=File(...)):
    """
    Creates a signal resource by reading pickle file containing data
    and instantiating signal class object with the data. 
    
    Args: 
        Pickle File, containing signal data (list with float elements)

    Returns: 
        A list object containing newly created Signal instance. 
    
    Raises: 
        HTTPException: Invalid pickle file format type
    """
    # Raise error if unexpected file format
    if (file.content_type!= 'application/octet-stream'):
        raise HTTPException(status_code=400, detail="Invalid signal data file format. Only pickle files containing single lists are allowed")
    else:
        # Saving uploaded file data for usage
        with open(f'./data/{file.filename}', "wb") as buffer: 
            shutil.copyfileobj(file.file, buffer)
        # Extracting contents from file
        with open(f'./data/{file.filename}', "rb") as input_file: 
            rndData = pickle.load(input_file)
        # Creating signal instance
        sig = Signal(data = rndData)
        # Clearing older objects and adding new signal instance to object list
        sigObjects.clear()
        sigObjects.append({"signal":sig})
        return {"data":sigObjects}   

# Input object verification
def signalCheck():
    """
    Checking if the signal object exists
    
    Args: 
        None 
    Returns: 
        None
    Raises: 
        HTTP Exception: No Signal data found
    """
    # Raising exception if empty signal data object
    if (len(sigObjects) == 0):
        raise HTTPException(status_code=401, detail="No Signal data dound")

@app.get('/dominant_frequency')
def compute_freq():
    """
    Computes dominant frequency in the signal data

    Args: 
        None 
    Returns: 
        Dominant Frequency of last randomly generated signal data
    """
    # Checking for signal data exists
    signalCheck()
    # Acquiring signal and computing dominant frequency using class method
    sampleSignal = sigObjects[-1]["signal"]
    sampleSignal.dom_freq = sampleSignal.compute()
    return f"The dominant frequency of signal is {sampleSignal.dom_freq} Hz"
   