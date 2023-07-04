from django.shortcuts import render
from .forms import BodyFatPredictionForm
from .models import BodyFatPrediction
from .utills import load_bodyfat_model

def predict_bodyfat(request):
    form = BodyFatPredictionForm()  # Instantiate the form

    if request.method == 'POST':
        form = BodyFatPredictionForm(request.POST)
        if form.is_valid():
            density = form.cleaned_data['density']
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            neck = form.cleaned_data['neck']
            chest = form.cleaned_data['chest']
            abdomen = form.cleaned_data['abdomen']
            hip = form.cleaned_data['hip']
            thigh = form.cleaned_data['thigh']
            knee = form.cleaned_data['knee']
            ankle = form.cleaned_data['ankle']
            biceps = form.cleaned_data['biceps']
            forearm = form.cleaned_data['forearm']
            wrist = form.cleaned_data['wrist']

            # Create a new BodyFatPrediction instance with the provided input data
            bodyfat_prediction = BodyFatPrediction.objects.create(
                density=density, age=age, weight=weight, height=height, neck=neck, chest=chest,
                abdomen=abdomen, hip=hip, thigh=thigh, knee=knee, ankle=ankle,
                biceps=biceps, forearm=forearm, wrist=wrist
            )

            # Load the bodyfat prediction model
            model = load_bodyfat_model()

            # Preprocess the input features if necessary
            input_features = [bodyfat_prediction.density, bodyfat_prediction.age, bodyfat_prediction.weight,
                              bodyfat_prediction.height, bodyfat_prediction.neck, bodyfat_prediction.chest,
                              bodyfat_prediction.abdomen, bodyfat_prediction.hip, bodyfat_prediction.thigh,
                              bodyfat_prediction.knee, bodyfat_prediction.ankle, bodyfat_prediction.biceps,
                              bodyfat_prediction.forearm, bodyfat_prediction.wrist]

            # Perform prediction using the loaded model
            predicted_bodyfat = round(model.predict([input_features])[0], 2)

            # Update the BodyFatPrediction instance with the predicted value
            bodyfat_prediction.predicted_bodyfat = predicted_bodyfat
            bodyfat_prediction.save()

            # Pass the predicted bodyfat value to the template
            context = {'form': form, 'predicted_bodyfat': predicted_bodyfat}

            return render(request, 'measure/page.html', context)

    # Pass the form to the template
    context = {'form': form}
    return render(request, 'measure/page.html', context)
