from django import forms
from .models import Form,Course


class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Form
        fields='__all__'
        widgets = {
            'textbook': forms.CheckboxInput(),
            'exampaper': forms.CheckboxInput()
        }
       
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()     
        if 'department' in self.data:
            try:
                department_id=int(self.data.get('department')) # type: ignore
                self.fields['course'].queryset=Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset=self.instance.country.course_set.order_by('name')     
                   