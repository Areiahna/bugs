from django import forms
from bug_app.models import MyUser, Ticket


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)


class AssignTicketForm(forms.ModelForm):
    assigned = forms.ModelChoiceField(queryset=Ticket.objects.all())

    class Meta:
        model: Ticket
        fields: '__all__'
