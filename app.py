# import streamlit as st
# st.title ("Dell Global Busyness Centre")
# st.image ("dell_logo.jpg")
# st.camera_input ("Case Input:")
# st.date_input ("Transactional Date")
# st.radio ("Department:", ['AI', 'CFI', 'ISG NPI', 'CSG NPI'])


import streamlit as st
import joblib
from PIL import Image
import numpy as np

try:
    import cv2
except ImportError:
    st.error("OpenCV (cv2) is not installed properly. Check requirements.txt.")
    raise
    
st.title ("Dell Global Busyness Centre")
st.image ("dell_logo.jpg")
#st.camera_input ("Case")
st.text ("Crack Detector using KNN")
from sklearn.tree import DecisionTreeClassifier

model = joblib.load ("trained_model_KNN.pkl")

# Preprocessing and feature extraction
def preprocess_image(img):
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges
 
def extract_features(img):
    resized = cv2.resize(img, (64, 64))
    return resized.flatten().reshape(1, -1)

uploaded_file = st.file_uploader ("Upload an image", type=["png", "jpg","jpeg"])

#"L" mode means 8-bit pixels, black and white
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")    
    img_array = np.array (image)

    st.image (image, caption = "You have uploaded this image")
    processed_image = preprocess_image (img_array)
    features = extract_features (processed_image)
    
    #FIX
    #clf = DecisionTreeClassifier() 
    prediction = model.predict (features)[0]
    #label = clf.predict(img_array)[0]
    label = "Positive" if prediction == 1 else "Negative"
    st.success(f"**Prediction:** {label}")
    st.balloons ()
    
    

    



