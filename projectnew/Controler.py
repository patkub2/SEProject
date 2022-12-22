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

from ModelM import ModelM 

class Controler:

# instance attributes
 def __init__(self):
   
   modelM = ModelM(r"D:\programing projects\SEProject\pppp\pic\flower_images\flower_images",[],VGG16(),{})
   
   #modelM.setPath(r"D:\programing projects\SEProject\pppp\pic\flower_images\flower_images")
   
   # change the working directory to the path where the images are located
   os.chdir(modelM.getPath())
   
   # this list holds all the image filename
   #flowers = []
   
   # creates a ScandirIterator aliased as files
   with os.scandir(modelM.getPath()) as files:
     # loops through each file in the directory
       for file in files:
           if file.name.endswith('.png'):
             # adds only the image files to the flowers list
               modelM.flowers.append(file.name)
               
               

   
   modelM.setModel(Model(inputs = modelM.getModel().inputs, outputs = modelM.getModel().layers[-2].output)) 
   
  
      
   
   p = r"D:\programing projects\SEProject\pppp\picend"
   
   # lop through each image in the dataset
   for flower in modelM.getFlowers():
       # try to extract the features and update the dictionary
       try:
           
           modelM.setFeat(modelM.extract_features(flower,modelM.getModel()))
           modelM.setData(flower,modelM.getFeat())
           #data[flower] = feat
       # if something fails, save the extracted features as a pickle file (optional)
       except:
           with open(p,'wb') as file:
               pickle.dump(modelM.getData(),file)
             
   
   # get a list of the filenames
   modelM.setFilenames(np.array(list(modelM.getData().keys())))
   
   # get a list of just the features
   modelM.setFeat(np.array(list(modelM.getData().values())))
   
   # reshape so that there are 210 samples of 4096 vectors
   modelM.setFeat(modelM.getFeat().reshape(-1,4096))
   
   
   # get the unique labels (from the flower_labels.csv)
   df = pd.read_csv('flower_labels.csv')
   label = df['label'].tolist()
   unique_labels = list(set(label))
   
   # reduce the amount of dimensions in the feature vector
   pca = PCA(n_components=100, random_state=22)
   pca.fit(modelM.getFeat())
   x = pca.transform(modelM.getFeat())
   
   # cluster feature vectors
   kmeans = KMeans(n_clusters=len(unique_labels), random_state=22,n_init="auto")
   kmeans.fit(x)
   
   # holds the cluster id and the images { id: [images] }
   for file, cluster in zip(modelM.getFilenames(),kmeans.labels_):
       if cluster not in modelM.getGroups().keys():
           modelM.setGroups(cluster,[])
           modelM.getGroupsTab(cluster).append(file)
       else:
           modelM.getGroupsTab(cluster).append(file)
   
   
           
      
   # this is just incase you want to see which value for k might be the best 
   sse = []
   list_k = list(range(3, 50))
   
   for k in list_k:
       km = KMeans(n_clusters=k, random_state=22,n_init="auto")
       km.fit(x)
       
       sse.append(km.inertia_)
   
   # Plot sse against k
   plt.figure(figsize=(6, 6))
   plt.plot(list_k, sse)
   plt.xlabel(r'Number of clusters *k*')
   plt.ylabel('Sum of squared distance');
   
   # view the first 10 flower entries
   # print(flowers[:10])
   
   #print(modelM.getGroupsTab(1))
   print(modelM.view_cluster(2))
   
   
controler = Controler()
   # instantiate the objectdddddddddddddddddddddddddddddddddddddddddd
   