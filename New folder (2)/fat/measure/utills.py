import joblib
import sklearn

def load_bodyfat_model():
    model_path = '../body_fat_model.pkl'  # Replace with the actual path to your joblib file
    model = joblib.load(model_path)
    return model
