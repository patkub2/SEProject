
# for everything else
import os

class LoadingData:

# class attribute
 flowers = []

# instance attribute
 def __init__(self, path,flowers):
    self.path = path
    
# creates a ScandirIterator aliased as files
 def load(self):
      with os.scandir(self.path) as files:
  # loops through each file in the directory
        for file in files:
            if file.name.endswith('.png'):
          # adds only the image files to the flowers list
                self.flowers.append(file.name)

# outputs flowers
 def getFlowers(self):
     return self.flowers
      
 

     
    
