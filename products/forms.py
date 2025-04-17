from django import forms

class ProductForm(forms.Form):
  name = forms.CharField(label='Tên món:', max_length=255, required=True)
  price = forms.DecimalField(label='Giá bán:', max_digits=10, decimal_places=2, required=True)
  description = forms.CharField(label='Mô tả món ăn:', widget=forms.Textarea, required=False)
  url_image = forms.URLField(label='URL ảnh:', required=False)

class UpdateProductForm(forms.Form):
  price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
  description = forms.CharField(widget=forms.Textarea, required=False)
  url_image = forms.URLField(required=False)
