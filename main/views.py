from django.shortcuts import render, redirect
from django.views import View

from main.forms import ProductForm
from main.models import Picture, Category, Product


class HomeView(View):

    def get(self, request):
        return render(request, 'index.html')


class SHoppingView(View):

    def get(self, request):
        return render(request, 'shop.html')


class ShoppingCartView(View):

    def get(self, request):
        return render(request, 'cart.html')


class AddProductView(View):
    form_class = ProductForm
    template_name = 'add-product.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name)

    def post(self, request):
        # form = self.form_class(request.POST, request.FILES)
        # print(form.data)

        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        description = request.POST.get('product_description')
        author = request.user  # Assuming request.user represents the product's author

        # Get the selected category (assuming you have a form field for category)
        category = Category.objects.filter(pk=request.POST.get('product_category')).first()

        # Create the Product object with all required fields set
        print(category)
        product = Product.objects.create(
            name=name,
            price=price,
            description=description,
            user=author,  # Change 'author' to 'user'
            category=category  # Set the category
        )

        images = request.FILES.getlist('product_image')  # Correctly access the uploaded files

        for image in images:
            picture = Picture.objects.create(
                image=image,
                product=product
            )
            picture.save()
        return redirect('/')
