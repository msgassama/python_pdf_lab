
# from django.shortcuts import render

# # Create your views here.


# importez les modules nécessaires
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit

# vue pour la génération de PDF
def generate_pdf(request):
    # données de simulation
    order = {
        'name': 'John Doe',
        'address': '1234 Main St, Anytown USA',
        'phone': '555-555-5555',
        'email': 'johndoe@example.com',
        'created_at': '2022-04-01 14:30:00',
        'order_number': '123456',
        'payment_method': 'Credit Card',
        'payment': {
            'transaction_id': 'abcd1234',
        },
        'total': 25000,
    }
    ordered_food = [
        {
            'fooditem': 'Pizza Margherita',
            'quantity': 2,
            'fooditem_image_url': 'https://images.pexels.com/photos/8259499/pexels-photo-8259499.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
            'vendor_name': 'Pizza Palace',
            'vendor_slug': 'pizza-palace',
            'price': 5000
        },
        {
            'fooditem': 'Spaghetti Bolognese',
            'quantity': 1,
            'fooditem_image_url': 'https://images.pexels.com/photos/1170449/pexels-photo-1170449.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
            'vendor_name': 'Italian Delight',
            'vendor_slug': 'italian-delight',
            'price': 15000
        }
    ]
    tax_data = {
        'Sales Tax': {
            '10': 2000,
        },
        'VAT': {
            '5': 1250,
        }
    }
    subtotal = sum(item['quantity'] * item['price'] for item in ordered_food)

    # contexte pour le rendu du modèle
    context = {
        'order': order,
        'ordered_food': ordered_food,
        'tax_data': tax_data,
        'subtotal': subtotal,
    }
    # rendu du modèle
    # html = render(request, 'receipt/pdf_template.html', context)
    return render(request, 'receipt/pdf_template.html', context)


# import pdfkit
# from django.http import HttpResponse
# from django.template.loader import render_to_string

def download_receipt(request):
    # données de simulation
    order = {
        'name': 'John Doe',
        'address': '1234 Main St, Anytown USA',
        'phone': '555-555-5555',
        'email': 'johndoe@example.com',
        'created_at': '2022-04-01 14:30:00',
        'order_number': '123456',
        'payment_method': 'Credit Card',
        'payment': {
            'transaction_id': 'abcd1234',
        },
        'total': 25000,
    }
    ordered_food = [
        {
            'fooditem': 'Pizza Margherita',
            'quantity': 2,
            'fooditem_image_url': 'https://images.pexels.com/photos/8259499/pexels-photo-8259499.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
            'vendor_name': 'Pizza Palace',
            'vendor_slug': 'pizza-palace',
            'price': 5000
        },
        {
            'fooditem': 'Spaghetti Bolognese',
            'quantity': 1,
            'fooditem_image_url': 'https://images.pexels.com/photos/1170449/pexels-photo-1170449.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
            'vendor_name': 'Italian Delight',
            'vendor_slug': 'italian-delight',
            'price': 15000
        }
    ]
    tax_data = {
        'Sales Tax': {
            '10': 2000,
        },
        'VAT': {
            '5': 1250,
        }
    }
    subtotal = sum(item['quantity'] * item['price'] for item in ordered_food)

    # contexte pour le rendu du modèle
    context = {
        'order': order,
        'ordered_food': ordered_food,
        'tax_data': tax_data,
        'subtotal': subtotal,
    }

    # rendu du modèle
    html_string = render_to_string('receipt/pdf_template.html', context)

    # options pour la conversion de pdfkit
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        # "enable-local-file-access": "",
        'enable-local-file-access': None
    }

    # conversion du HTML en PDF
    pdf = pdfkit.from_string(html_string, False, options=options)

    # création d'une réponse HTTP pour le fichier PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="receipt.pdf"'

    return response
