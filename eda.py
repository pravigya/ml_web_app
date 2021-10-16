# importing packages

import streamlit as st 
import pandas as pd
from PIL import Image 
import matplotlib.pyplot as plt
from PIL import Image

def eda():
	df = pd.read_csv("heart.csv")
	df = pd.read_ipynb("code (1).ipynb")
