from django.contrib.auth.forms import UserCreationForm

#This is use to override the label help text from the UserCreationForm
class UserCreateForm(UserCreationForm):
    def __init__(self,*args, **kwargs):
        super(UserCreateForm, self).__init__(*args,**kwargs)
        for fieldname in ['username','password1','password2']:
            #This remove all label and instruction associate with the form.
            self.fields[fieldname].help_text = None
            #This hand over the Form control to the Boostrap using class
            self.fields[fieldname].widget.attrs.update({'class':'form-control'})