from django import forms
from .models import *
'''from registration.forms import RegistrationForm
from rating.models import User, UserProfile, Business, Review, Boba, Flavour

class RegisterForm(RegistrationForm):
	is_business = forms.BooleanField(label ="Business User", initial = False, required = False)

	class Meta:
		fields = ('username', 'is_business', 'email', 'password', 'password2')
		model = User
	pass

class UserProfileForm(forms.ModelForm):
	image = forms.ImageField(help_text= 'Profile image:', required = False)
	class Meta:
		model = UserProfile
		fields = ('image')

	def __init(self, *args, **kwargs):
		super(UserProfileForm, self).__init(*args, **kwargs)
		self.fields['image'].widget.attrs.update({'type': image, 'accept': 'image/*'})

class BusinessForm(forms.ModelForm):
	name
	address
	description
	stocks
	slug

	class Meta:
		#'''


