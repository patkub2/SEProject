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
 def __init__(self, path):
    self.modelM = ModelM(path,[],VGG16(),{}) 

 def runAlgorith(self):
       
   
   
   #self.modelM.setPath(r"D:\programing projects\SEProject\pppp\pic\flower_images\flower_images")
   
   # change the working directory to the path where the images are located
   os.chdir(self.modelM.getPath())
   
   # this list holds all the image filename
   #flowers = []
   
   # creates a ScandirIterator aliased as files
   with os.scandir(self.modelM.getPath()) as files:
     # loops through each file in the directory
       for file in files:
           if file.name.endswith('.png'):
             # adds only the image files to the flowers list
               self.modelM.flowers.append(file.name)
               
               

   
   self.modelM.setModel(Model(inputs = self.modelM.getModel().inputs, outputs = self.modelM.getModel().layers[-2].output)) 
   
  
      
   
   p = r"D:\programing projects\SEProject\pppp\picend"
   
   # lop through each image in the dataset
   for flower in self.modelM.getFlowers():
       # try to extract the features and update the dictionary
       try:
           
           self.modelM.setFeat(self.modelM.extract_features(flower,self.modelM.getModel()))
           self.modelM.setData(flower,self.modelM.getFeat())
           #data[flower] = feat
       # if something fails, save the extracted features as a pickle file (optional)
       except:
           with open(p,'wb') as file:
               pickle.dump(self.modelM.getData(),file)
             
   
   # get a list of the filenames
   self.modelM.setFilenames(np.array(list(self.modelM.getData().keys())))
   
   # get a list of just the features
   self.modelM.setFeat(np.array(list(self.modelM.getData().values())))
   
   # reshape so that there are 210 samples of 4096 vectors
   self.modelM.setFeat(self.modelM.getFeat().reshape(-1,4096))
   
   
   # get the unique labels (from the flower_labels.csv)
   df = pd.read_csv('flower_labels.csv')
   label = df['label'].tolist()
   unique_labels = list(set(label))
   
   # reduce the amount of dimensions in the feature vector
   pca = PCA(n_components=100, random_state=22)
   pca.fit(self.modelM.getFeat())
   x = pca.transform(self.modelM.getFeat())
   
   # cluster feature vectors
   kmeans = KMeans(n_clusters=len(unique_labels), random_state=22,n_init="auto")
   kmeans.fit(x)
   
   # holds the cluster id and the images { id: [images] }
   for file, cluster in zip(self.modelM.getFilenames(),kmeans.labels_):
       if cluster not in self.modelM.getGroups().keys():
           self.modelM.setGroups(cluster,[])
           self.modelM.getGroupsTab(cluster).append(file)
       else:
           self.modelM.getGroupsTab(cluster).append(file)
   
   
           
      
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
   
   print(list_k)
   print(sse)
   print(k)
   print(km)
   print(cluster)
   print(file)
   print(list(self.modelM.getGroups().keys()).count())
   print(list(self.modelM.getGroups().keys()))
   # view the first 10 flower entries
   #print(self.modelM.getFlowers()[:10])
   #return self.modelM.getFlowers()
   
   #print(self.modelM.getGroupsTab(1))
   #print(self.modelM.getGroups())
   #print(self.modelM.view_cluster(2))

 def returnCluster(self, number):
    return self.modelM.view_cluster(number)

 def returnAllClusters(self):
    return self.modelM.getGroups()
    
 
#controler = Controler()
   # instantiate the objectdddddddddddddddddddddddddddddddddddddddddd
   