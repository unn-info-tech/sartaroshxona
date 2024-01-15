from django import forms
from .models import Country, City, Region, District
from main.models import CustomUser

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['country', 'region', 'district', 'city']

    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Select Country")

    region = forms.ModelChoiceField(queryset=Region.objects.none(), required=False,
                                    label="Region/State/Province")
    
    district = forms.ModelChoiceField(queryset=District.objects.none(), required=False,
                                    label="District/County")

    city = forms.ModelChoiceField(queryset=City.objects.none(), required=False,
                                    label="City/Town/Village")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.none()
        self.fields['district'].queryset = District.objects.none()
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['region'].queryset = Region.objects.filter(country_id=country_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['region'].queryset = self.instance.country.region_set.order_by('name')

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['district'].queryset = District.objects.filter(region_id=region_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.region.district_set.order_by('name')

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(district_id=district_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset

        
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.district.city_set.order_by('name')
