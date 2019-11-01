import cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm

TRAIN_DIR='/home/satvik/Downloads/major/dataset/train'
TEST_DIR ='/home/satvik/Downloads/major/dataset/val'
IMG_SIZE=50
LR=1e-3 #learning rate

MODEL_NAME = 'medicinal_leaves-{}={}.model'.format(LR,'2conv-basic')



def label_img(img):
    word_label = img.split('.')[-3] 
    if (word_label == "drumstick"):
        return [1,0,0,0,0]
    elif (word_label == "Heena"):
        return [0,1,0,0,0]
    elif (word_label == "Neem"):
        return [0,0,1,0,0]
    elif (word_label == "peppermint"):
        return [0,0,0,1,0]
    elif (word_label == "Tulsi"):
        return [0,0,0,0,1]
    
    
def create_train_data():
    training_data = []
    for img in tqdm(os.listdir(TRAIN_DIR)):
        label = label_img(img)
        path = os.path.join(TRAIN_DIR,img)
        img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
        training_data.append([np.array(img),np.array(label)])
    shuffle(training_data)
    np.save('train_data.npy', training_data)
    return training_data

def process_test_data():
    testing_data = []
    for img in tqdm(os.listdir(TEST_DIR)):
        path = os.path.join(TEST_DIR,img)
        img_num = img.split('.')[0]
        img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
        testing_data.append([np.array(img), img_num])
        
    shuffle(testing_data)
    np.save('test_data.npy', testing_data)
    return testing_data

train_data= create_train_data()
