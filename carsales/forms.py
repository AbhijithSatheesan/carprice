from django import forms

class CarPriceForm(forms.Form):
    model = forms.ChoiceField(choices=[
        ("Actyon", "Actyon"), ("Aqua", "Aqua"), ("Camry", "Camry"),
        ("Cruze", "Cruze"), ("E 350", "E 350"), ("Elantra", "Elantra"),
        ("FIT", "FIT"), ("Fusion", "Fusion"), ("GX 460", "GX 460"),
        ("H1", "H1"), ("Highlander", "Highlander"), ("Jetta", "Jetta"),
        ("ML 350", "ML 350"), ("Optima", "Optima"), ("Prius", "Prius"),
        ("Santa FE", "Santa FE"), ("Sonata", "Sonata"), ("Transit", "Transit"),
        ("Tucson", "Tucson"), ("X5", "X5")
    ])
    production_year = forms.IntegerField(min_value=1990, max_value=2024)
    mileage = forms.FloatField(label="Mileage (km)")
    gear_box_type = forms.ChoiceField(choices=[
        ("Variator", "Variator"), ("Automatic", "Automatic"),
        ("Manual", "Manual"), ("Tiptronic", "Tiptronic")
    ])
    color = forms.ChoiceField(choices=[
        ("Black", "Black"), ("Silver", "Silver"), ("White", "White"),
        ("Grey", "Grey"), ("Blue", "Blue"), ("Orange", "Orange"),
        ("Red", "Red")
    ])
