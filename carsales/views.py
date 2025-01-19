from django.shortcuts import render

# Create your views here.
import os
import joblib
from django.shortcuts import render
from .forms import CarPriceForm


import warnings
from sklearn.exceptions import DataConversionWarning


warnings.filterwarnings('ignore', category=DataConversionWarning)
warnings.filterwarnings('ignore', message='X does not have valid feature names')



# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'ml_model', 'car_price_predictor_model.joblib')
model = joblib.load(model_path)

# Encoding mappings
encoding_mappings = {
    "Model": {
        "Actyon": 0,
        "Aqua": 1,
        "Camry": 2,
        "Cruze": 3,
        "E 350": 4,
        "Elantra": 5,
        "FIT": 6,
        "Fusion": 7,
        "GX 460": 8,
        "H1": 9,
        "Highlander": 10,
        "Jetta": 11,
        "ML 350": 12,
        "Optima": 13,
        "Prius": 14,
        "Santa FE": 15,
        "Sonata": 16,
        "Transit": 17,
        "Tucson": 18,
        "X5": 19
    },
    "Gear box type": {
        "Variator": 0,
        "Automatic": 1,
        "Manual": 2,
        "Tiptronic": 3
    },
    "Color": {
        "Black": 0,
        "Silver": 1,
        "White": 2,
        "Grey": 3,
        "Blue": 4,
        "Orange": 5,
        "Red": 6
    }
}

def predict_car_price(request):
    result = None
    if request.method == "POST":
        form = CarPriceForm(request.POST)
        if form.is_valid():
            model_input = encoding_mappings["Model"][form.cleaned_data["model"]]
            production_year = form.cleaned_data["production_year"]
            mileage = form.cleaned_data["mileage"]
            gearbox_input = encoding_mappings["Gear box type"][form.cleaned_data["gear_box_type"]]
            color_input = encoding_mappings["Color"][form.cleaned_data["color"]]

            # Predict using the model
            predicted_price = model.predict([[model_input, production_year, mileage, gearbox_input, color_input]])
            result = predicted_price[0] * 1.3  # Adjust scale
    else:
        form = CarPriceForm()

    return render(request, "carsales/predict_price.html", {"form": form, "result": result})
