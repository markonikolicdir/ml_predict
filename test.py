from flask import Flask

import numpy as np

import json

import keras.models as models

# Opening JSON file
f = open('deviation.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

for i in data['deviation']:
    print(i)
 
# Closing file
f.close()


model = models.load_model("kneeRight.h5")

result = model.predict([data['deviation']])

print(result);