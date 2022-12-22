# for loading/processing the images  
from tensorflow.keras.utils import load_img
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
import pandas as pd
import pickle


class ModelM:
    
# instance attributes
 def __init__(self,path,flowers,model,data):
   self.path = path
   self.flowers = flowers
   self.model = model
   self.data = data

 def getPath(self):
   return self.path
 def setPath(self,arg):
   self.path = arg
 
 def getModel(self):
   return self.model
 def setModel(self,arg):
   self.model = arg
   
 def getFlowers(self):
   return self.flowers
 def setFlowers(self,arg):
   self.flowers = arg
   
 def getData(self):
   return self.data
 def setData(self,tab,value):
   self.data[tab] = value
 
 def extract_features(file, model):
    # load the image as a 224x224 array
    img = load_img(file, target_size=(224,224))
    # convert from 'PIL.Image.Image' to numpy array
    img = np.array(img) 
    # reshape the data for the model reshape(num_of_samples, dim 1, dim 2, channels)
    reshaped_img = img.reshape(1,224,224,3) 
    # prepare image for model
    imgx = preprocess_input(reshaped_img)
    # get the feature vector
    features = model.predict(imgx, use_multiprocessing=True)
    return features
  
  
# instantiate the object
