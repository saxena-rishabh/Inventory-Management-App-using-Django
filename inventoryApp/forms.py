from django import forms
from inventoryApp.models import item

class InventoryForm(forms.ModelForm):
    class Meta:
        model = item
        fields = '__all__'