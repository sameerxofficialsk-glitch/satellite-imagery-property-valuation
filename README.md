# Multimodal Model for House Price Prediction

## Overview
This project predicts house prices using a **multimodal machine learning pipeline** that combines:
- **Tabular property features** (size, location, condition, etc.)
- **Satellite imagery** (visual context around each property)

The goal is to evaluate whether satellite images add value beyond strong tabular baselines, while demonstrating an end-to-end, reproducible ML workflow.

---

## Repository Structure
```
Multimodal-Model-for-House-Price-Prediction/
│
├── data/
│ ├── train.csv
│ └── test.csv
│
├── images/
│ └── <property_id>/
│     └── *.jpg
│
├── notebooks/
│ ├── 01_preprocessing.ipynb
│ ├── 02_tabular_baseline_models.ipynb
│ ├── 03_data_fetcher.ipynb
│ ├── 04_image_embeddings.ipynb
│ └── 05_model_training.ipynb
│
├── models/
│ ├── tabular_xgb_model.pkl
│ ├── multimodal_xgb_model.pkl
│ ├── image_embeddings.pkl
│ └── scaler.pkl
│
├── outputs/
│ ├── baseline_predictions/
│ │ ├── rf_tabular_predictions.csv
│ │ └── xgb_tabular_predictions.csv
│ └── final_submission.csv
│
├── src/
│ └── data_fetcher.py
│
└── README.md
```
---

## Setup Instructions

### 1) Clone the Repository
```
git clone https://github.com/sameerxofficialsk-glitch/Multimodal-Model-for-House-Price-Prediction
cd Multimodal-Model-for-House-Price-Prediction
```

### 2) Create & Activate a Virtual Environment (Recommended)
### Windows
```
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS
```
python -m venv venv
source venv/bin/activate
```

### 3) Install Dependencies
If requirements.txt is present:
```
pip install -r requirements.txt
```

### Otherwise install core dependencies:
```
pip install pandas numpy scikit-learn xgboost matplotlib seaborn torch torchvision sentinelhub
```

## Sentinel Hub Credentials (Optional)
Satellite images were fetched during development using the Sentinel Hub API.

***Note:*** API credits have expired. Image downloading is not required to run this project because all images and embeddings are already stored locally.

### If you still want to configure credentials (optional):
```
setx SENTINEL_CLIENT_ID "your_client_id"
setx SENTINEL_CLIENT_SECRET "your_client_secret"
setx SENTINEL_INSTANCE_ID "your_instance_id"
```
*Restart Jupyter after setting variables*

# How to Run the Project
**Step 1: Preprocessing & EDA**
Open:
```
notebooks/01_preprocessing.ipynb
```
- Loads and cleans tabular data
- Performs EDA
- Prepares features

**Step 2: Tabular Baseline Models**
Open:
```
notebooks/02_tabular_baseline_models.ipynb
```
- Trains tabular-only models (Random Forest, XGBoost)
- Evaluates RMSE and R^2
- Saves baseline predictions to outputs/baseline_predictions/

**Step 3: Satellite Image Fetching (Documentation Only)**
Open:
```
notebooks/03_data_fetcher.ipynb
```
- Demonstrates how images were fetched using latitude/longitude
- Do not re-run (API credits expired)

***Production-style script:***
```
src/data_fetcher.py
```

**Step 4: Image Embeddings (Already Generated)**
Open:
```
notebooks/04_image_embeddings.ipynb
```
- Shows CNN-based embedding extraction
- Do not re-run; embeddings are already saved to models/image_embeddings.pkl

**Step 5: Multimodal Training & Final Predictions**
Open:
```
notebooks/05_model_training.ipynb
```
- Fuses tabular features with image embeddings
- Trains multimodal model
- Compares with tabular baseline
- Generates final predictions

**Final Submission File**
The only file intended for submission:
```
outputs/final_submission.csv
```
***Format:***
```
id,predicted_price
```

**Results Summary**
| Model | RMSE | R^2 |
|------|------|----|
| XGBoost (Tabular) | ~108k | ~0.9055 |
| Random Forest (Tabular) | ~121k | ~0.8806 |
| XGBoost (Multimodal) | ~122k | ~0.8787 |
| Linear Regression (Tabular) | ~190k | ~0.7084 |

*Selected Final Model: XGBoost (Tabular)*
**Reason:** Best RMSE and R^2; strong tabular features dominated predictive power.

## Limitations
- Satellite imagery did not outperform strong tabular baselines in this dataset
- External API access is limited by service credits

***Reproducibility Notes***
- All paths are relative (no hard-coded system paths)
- No credentials stored in code
- Images and embeddings are cached locally
- API-dependent steps are documented but not re-executed


Sameer Kumar
BS-MS (Economics)
24322024, IIT Roorkee