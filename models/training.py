# -*- coding: utf-8 -*-
"""style_5_27.ipynb
 
Automatically generated by Colaboratory.
 
Original file is located at
    https://colab.research.google.com/drive/1wy1oSnK01iiYRwUf4Rc4Y1rxyb_LTpu2
"""
 
# packages in this training file
 
from train_module import *
 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
 
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow import keras
 
from tensorflow.keras.preprocessing import image
 
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from tensorflow.keras.layers.experimental.preprocessing import StringLookup
 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
import cv2
 
import matplotlib.image as mpimg
 
# connect with google while working on colab
from google.colab import drive
drive.mount('/content/drive')

with ZipFile(file_name, 'r') as zip:
  zip.extractall()
  print('Done')
 
 
styles = get_df()
 
styles["subCategory"].unique() # we can check by this code that we only have three subcategory now.
 
"""# Model-1: """
 
 
 
le = LabelEncoder()
#
styles["subCategory"] = le.fit_transform(styles["subCategory"])
 
 
 
 
styles.head()
 
le.classes_
 
 
 
sub_train,sub_val,sub_test = make_input_xx(make_input_array_subcate(styles))
 
sub_model = build_model(80, 60)
 
sub_model.summary()
 
from tensorflow.keras.utils import plot_model
plot_model(sub_model)
 
sub_model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
 
sub_history = sub_model.fit(sub_train,
                    epochs=5,
                    steps_per_epoch = 2000,
                    validation_data = sub_val)
 
sub_model.save("/content/drive/MyDrive/models/model_sub")
 
test_model = tf.keras.models.load_model("/content/drive/MyDrive/models/model_sub")
 
test_model.evaluate(sub_test)
 
"""# Model 234"""
 
 
top_df = get_234_df("Topwear")
bottom_df = get_234_df("Bottomwear")
foot_df = get_234_df("Footwear")
 
top_df,top_art,top_gen,top_base,top_sea,top_usage = my_le(top_df)
bottom_df,bottom_art,bottom_gen,bottom_base,bottom_sea,bottom_usage = my_le(bottom_df)
foot_df,foot_art,foot_gen,foot_base,foot_sea,foot_usage = my_le(foot_df)
 
foot_usage.classes_
 
top_base_model = build_model(80,60,top_art,top_gen,top_base,top_sea,top_usage)
bottom_base_model = build_model(80,60,bottom_art,bottom_gen,bottom_base,bottom_sea,bottom_usage)
foot_base_model = build_model(80,60,foot_art,foot_gen,foot_base,foot_sea,foot_usage)
 
 
top_train, top_val, top_test = make_input_xx(make_input_array_2(top_df))
bottom_train, bottom_val, bottom_test = make_input_xx(make_input_array_2(bottom_df))
foot_train, foot_val, foot_test = make_input_xx(make_input_array_2(foot_df))




bottom_base_model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])






 
bottom_history = bottom_base_model.fit(bottom_train,
                    epochs=15,
                    steps_per_epoch = 50,
                    validation_data = bottom_val)
 
bottom_base_model.evaluate(bottom_test)
 
bottom_base_model.save("/content/drive/MyDrive/models/model_2.2")