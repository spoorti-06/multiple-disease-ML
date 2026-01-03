import os
import pickle

working_dir = os.path.dirname(os.path.abspath(__file__))

models = {
    'diabetes_model': 'saved_models/diabetes_model.sav',
    'heart_disease_model': 'saved_models/heart_disease_model.sav',
    'parkinsons_model': 'saved_models/parkinsons_model.sav'
}

for name, relpath in models.items():
    path = os.path.join(working_dir, relpath)
    print(f"Checking {name} at {path} -> ", end='')
    if not os.path.exists(path):
        print("MISSING")
        continue
    try:
        with open(path, 'rb') as f:
            _ = pickle.load(f)
        print("OK (loaded)")
    except Exception as e:
        print(f"ERROR: {e}")
