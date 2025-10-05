from django import forms
from .models import Node, Edge, Workflow


class Workflowform(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter workflow name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter workflow description',
                'rows': 3
            }),
        }
        labels = {
            'name': 'Workflow Name',
            'description': 'Workflow Description',
        }

class Nodeform(forms.ModelForm):

    class Meta:
        model = Node

        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter node name'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter node content',
                'rows': 3
            }),
        }
        labels = {
            'title': 'Node Name',
            'content': 'Node content',
        }

class Edgeform(forms.ModelForm):

    class Meta:
        model = Edge

        fields = ['from_node', 'to_node', 'condition'] 



