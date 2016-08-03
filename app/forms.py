from django import forms 
from django.core.validators import RegexValidator
from models import State, City
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Submit, HTML, Layout, Div, Field
from crispy_forms.bootstrap import FormActions 
from django.core.urlresolvers import reverse



# class CitySearchForm(forms.Form):
#     like_website = forms.TypedChoiceField(
#         label = "Do you like this website?",
#         choices = ((1, "Yes"), (0, "No")),
#         coerce = lambda x: bool(int(x)),
#         widget = forms.RadioSelect,
#         initial = '1',
#         required = True,
#     )

#     favorite_food = forms.CharField(
#         label = "What is your favorite food?",
#         max_length = 80,
#         required = True,
#     )

#     favorite_color = forms.CharField(
#         label = "What is your favorite color?",
#         max_length = 80,
#         required = True,
#     )

#     favorite_number = forms.IntegerField(
#         label = "Favorite number",
#         required = False,
#     )

#     notes = forms.CharField(
#         label = "Additional notes or feedback",
#         required = False,
#     ) 
#     def __init__(self, *args, **kwargs):
#         super(CitySearchForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'get'
#         self.helper.form_action = 'city_search'

#         self.helper.add_input(Submit('submit', 'Search'))     


class EditCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        




 
class CityCreate(forms.ModelForm):
        class Meta:
            model = City
            fields = '__all__'



class CitySearchForm(forms.Form):
    letters_only = RegexValidator(r'^[a-zA-Z]*$', 
                                    'only letters are allowed'
                                    )

    state = forms.CharField(required=True, 
                            validators=[letters_only],
                            )
    city = forms.CharField(required=True,
                            validators=[letters_only]
                        ) 
    def __init__(self, *args, **kwargs):
        super(CitySearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_action = 'city_search'
        self.helper.layout = Layout(
                                    Div('city', css_class='col-sm-5 col-md-5'),
                                    Div('state', css_class='col-sm-5 col-md-5'),
                                        FormActions (
                                            Submit('submit','Search', css_class="btn-primary"),
                                            css_class='col-sm-2 col-md',
                                            style='margin-top:25px;'


                                            )
                                        

                                    )

        # self.helper.add_input(Submit('submit', 'Search'))
class EditState(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditState, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('edit_city',kwargs={'pk': self.instance.pk})
        self.helper.layout = Layout(
                                    Div('city', css_class='col-sm-5 col-md-5'),
                                    Div('state', css_class='col-sm-5 col-md-5'),
                                        FormActions (
                                            Submit('submit','Search', css_class="btn-primary"),
                                            css_class='col-sm-2 col-md',
                                            style='margin-top:25px;'


                                            )
                                        

                                    )