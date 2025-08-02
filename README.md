# breast-cancer-svm-predictor
SVM-based breast cancer detection with a user-friendly Streamlit interface
# 🩺 Breast Cancer Prediction Using SVM

This project is a simple, beginner-friendly **machine learning web app** that predicts whether a breast tumor is benign or malignant based on key diagnostic features. The app uses a trained Support Vector Machine (SVM) model and provides a clear, color-coded result for easy interpretation.

## ✅ Features
- 🔘 Minimal input: Only 6 easy-to-understand questions
- 🤖 Accurate prediction using SVM algorithm
- 💻 Streamlit interface — no coding knowledge required
- ✅ Designed for **naive users** — friendly and non-technical language

## 📁 Files in This Repository

| File | Description |

| `aap.py` | Streamlit app code for user interface |
| `b_c_predication.ipynb` | Jupyter notebook with training, preprocessing, and EDA |
| `svm_model.pkl` | Trained SVM model file |
| `scaler.pkl` | Preprocessing scaler used for input normalization |
| `requirements.txt` | Python package dependencies |

## ▶️ How to Run the App
### 🧪 Local Setup
```bash
git clone https://github.com/Sunita0/breast-cancer-svm-predictor.git
cd breast-cancer-svm-predictor
pip install -r requirements.txt
streamlit run aap.py
📊 Dataset Used
Source: Sklearn Breast Cancer Wisconsin Diagnostic Dataset
Classes: Malignant (cancerous), Benign (non-cancerous)
Features: Tumor shape, size, texture, concavity, etc.

⚠️ Disclaimer
This app is for educational/demo purposes only. It should not be used for actual medical diagnosis. Always consult a healthcare professional.

🙋‍♀️ Author
Developed by Sunita as part of a machine learning learning journey.


---

