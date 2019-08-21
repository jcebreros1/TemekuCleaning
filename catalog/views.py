from django.shortcuts import render
from django.utils import timezone
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def index(request):
    """View function for home page of site."""
    date = timezone.now()

    context = {
        'timedate': date
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def management(request):
    """View function for home page of site."""
    date = timezone.now()

    context = {
        'timedate': date
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'management.html', context=context)

def services(request):
    """View function for home page of site."""
    date = timezone.now()

    context = {
        'timedate': date
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'services.html', context=context)


def aboutus(request):
    """View function for home page of site."""
    date = timezone.now()

    context = {
        'timedate': date
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'aboutus.html', context=context)


def blog(request):
    """View function for home page of site."""
    date = timezone.now()

    context = {
        'timedate': date
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'blog.html', context=context)

def contactus(request):
    """View function for home page of site."""
    date = timezone.now()
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name','')
            phone = request.POST.get('phone','')
            time_preference = request.POST.get('time_preference','')
            #contact_email = request.POST.get('contact_email','')
            #form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')


            context = {
                'timedate': date,
                'contact_name': contact_name,
                'phone': phone,
                'time_preference': time_preference,
                #'contact_email': contact_email,
                #'form_content': form_content,
            }

            content = template.render(context)

            email = EmailMessage(
                                "content of email",
                                content,
                                "temekucleaning.com"+'',
                                ["cebrerosjesus@gmail.com"],
                                #headers = {'Reply-To':contact_email}
                                )
            email.send()
            return redirect('contactus')

    context = {
                'timedate': date,
            }
    return render(request, 'contactus.html', context=context)


def houseservices(request):
    """View function for home page of site."""
    date = timezone.now()

    context = {
        'timedate': date
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'houseservices.html', context=context)

def officeservices(request):
    """View function for home page of site."""
    date = timezone.now()

    context = {
        'timedate': date
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'officeservices.html', context=context)


