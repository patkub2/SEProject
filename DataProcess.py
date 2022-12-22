# for loading/processing the images  
from keras.preprocessing.image import load_img 
from keras.preprocessing.image import img_to_array 
from keras.applications.vgg16 import preprocess_input 

# models 
from keras.applications.vgg16 import VGG16 
from keras.models import Model

# clustering and dimension reduction
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# for everything else
import os
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle

# for everything else
import os

class DataProcess:

# class attribute
 img = []
 reshaped_img = []
# instance attribute
 def __init__(self,flowers):
    self.flowers = flowers
    
# creates a ScandirIterator aliased as files
 def convImage(self):
     # load the image as a 224x224 array
    self.img = load_img(self.flowers[0], target_size=(224,224))
    # convert from 'PIL.Image.Image' to numpy array
    self.img = np.array(self.img)
    self.reshaped_img = self.img.reshape(1,224,224,3)
    return preprocess_input(self.reshaped_img)


      
 

     
    
