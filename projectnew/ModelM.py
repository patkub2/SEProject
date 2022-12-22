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
   self.filenames = ""
   self.groups = {}
   self.feat = ""

# get and set methods
 def getPath(self):
   return self.path
 def setPath(self,arg):
   self.path = arg
 # get and set methods
 def getModel(self):
   return self.model
 def setModel(self,arg):
   self.model = arg
 # get and set methods  
 def getFlowers(self):
   return self.flowers
 def setFlowers(self,arg):
   self.flowers = arg
 # get and set methods  
 def getData(self):
   return self.data
 def setData(self,tab,value):
   self.data[tab] = value
 # get and set methods  
 def getFilenames(self):
   return self.filenames
 def setFilenames(self,arg):
   self.filenames = arg
 # get and set methods
 def getGroups(self):
   return self.groups
 def getGroupsTab(self,tab):
   return self.groups[tab]
 def setGroups(self,tab,value):
   self.groups[tab] = value
 
 # get and set methods
 def getFeat(self):
   return self.feat
 def setFeat(self,arg):
   self.feat = arg
 
 def extract_features(self,file, model):
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
  
  
# function that lets you view a cluster (based on identifier)        
 def view_cluster(self,cluster):
     plt.figure(figsize = (25,25))
     # gets the list of filenames for a cluster
     files = self.getGroupsTab(cluster)
     # only allow up to 30 images to be shown at a time
     if len(files) > 30:
         print(f"Clipping cluster size from {len(files)} to 30")
         files = files[:29]
     # plot each image in the cluster
     for index, file in enumerate(files):
         plt.subplot(10,10,index+1)
         img = load_img(file)
         img = np.array(img)
         plt.imshow(img)
         plt.axis('off')

  
# instantiate the object
