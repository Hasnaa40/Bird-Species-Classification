
# Bird Species Classification

## Overview  
This project focuses on classifying bird species using a **Convolutional Neural Network (CNN)**. 
The model is trained to recognize six bird species from a dataset of images. 
It provides a Streamlit web app interface for users to upload an image and predict the bird species.

## Dataset  
The dataset consists of six bird species:  
1. American Goldfinch  
2. Barn Owl  
3. Carmine Bee-Eater  
4. Downy Woodpecker  
5. Emperor Penguin  
6. Flamingo  

You can download the dataset [here](https://drive.google.com/drive/folders/1Agdj1C-UmYfuvEykJSMFGOLIwGRPHh8g?usp=sharing).

---

## Project Structure  
1. **Data Preprocessing**  
   - Images are read, resized, and converted to arrays.  
   - The dataset is split into training and testing sets.  
   - Labels are binarized for multi-class classification.  

2. **Model Building**  
   - **Artificial Neural Network (ANN):** Tested for baseline performance.  
   - **Convolutional Neural Network (CNN):** Built for accurate image classification.  
   - **Callbacks:** Early stopping and learning rate reduction are implemented.

3. **Evaluation**  
   - Accuracy and loss curves are plotted for training and validation.  
   - Confusion matrix and classification report are generated.

---

## How to Run the Project  
1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies**  
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Dataset**  
   Place the dataset in the appropriate directory as mentioned in the notebook.

4. **Run the Streamlit App**  
   ```bash
   streamlit run app.py
   ```

---

## Usage  
- Upload an image of a bird through the Streamlit interface.  
- The app will display the uploaded image and predict the bird species.

---

## Dependencies  
- Python 3.x  
- TensorFlow  
- OpenCV  
- Pandas, NumPy, Seaborn, Matplotlib  
- Streamlit  

