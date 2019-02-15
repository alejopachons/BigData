from django import forms

class NumbersForm(forms.Form):

    number1 = forms.IntegerField(
        label="Número 1", 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Digite el primer número a operar'
                }
            )
        )

    number2 = forms.IntegerField(
        label="Número 2", 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class':'form-control', 
                'placeholder':'Digite el segundo número a operar'
                }
            )
        )

    operation = forms.ChoiceField(
        label="Operación", 
        required=True, 
        choices=[
            ("Suma","Suma"),
            ("Resta","Resta"),
            ("Potencia","Potencia")
            ]
        )
