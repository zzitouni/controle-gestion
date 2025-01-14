from django.contrib import messages
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm ,FinancialControlSubmissionForm
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser

from openpyxl import Workbook
from openpyxl.styles import NamedStyle

from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML



from .models import FinancialControlSubmission,Requete



def user_login(request):
# user login if user isn't authenticated take him to main
    if not request.user.is_authenticated: 
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                users = CustomUser.objects.all()

                print(users)

                user = authenticate(request, email=username, password=password)

                print(user)
                if user:
                    login(request, user)
                    messages.success(request, 'Connexion réussie.')


                    return redirect('main')  
                else:
                    messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            else:
                # Form is not valid, display error messages
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
        else: 
            form = LoginForm()

        return render(request, 'login.html', {'form': form})
    else:
        return redirect('main')

def user_logout(request):
#user logout
    logout(request)
    return redirect('login')  


@login_required(login_url='login')
def submission_list(request):
    submissions = FinancialControlSubmission.objects.all()
    return render(request, 'submission_list.html', {'submissions': submissions})

@login_required(login_url='login')
def first(request):
    
    if(request.user):
        print(request.user)

    context = {
       
    }

    return render(request, 'main.html', context)
def is_manager(user):
    return user.role == 'manager'

def is_admin(user):
    return user.role == 'admin'






@login_required(login_url='login')
def immofi(request):
    
    
    return render(request, 'IMMOFI.html', {})
   



# CRUD of complaint

@login_required(login_url='login')
def submission_create(request):
    if request.method == 'POST':
        form = FinancialControlSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submission_list')
    else:
        form = FinancialControlSubmissionForm()
    return render(request, 'IMMOFI.html', {'form': form})

@login_required(login_url='login')
def submission_update(request, pk):
    submission = get_object_or_404(FinancialControlSubmission, pk=pk)
    if request.method == 'POST':
        form = FinancialControlSubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('submission_list')
    else:
        form = FinancialControlSubmissionForm(instance=submission)
    return render(request, 'submission_list.html', {'form': form})
@login_required(login_url='login')
def confirm_requete(request, requete_id):
    requete = get_object_or_404(Requete, id=requete_id)
    requete.completed = True
    requete.save()
    return redirect(reverse('submission_list')) 
@login_required(login_url='login')
def submission_delete(request, pk):
    submission = get_object_or_404(FinancialControlSubmission, pk=pk)
    if request.method == 'POST':
        submission.delete()
        return redirect('submission_list')
    return render(request, 'submission_confirm_delete.html', {'submission': submission})


def download_submission_pdf(request, submission_id):
    submission = FinancialControlSubmission.objects.get(id=submission_id)
    html_string = render_to_string('submission_pdf_template.html', {'submission': submission})
    
    # Create a PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    # Create HTTP response with PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=submission_{submission.id}.pdf'

    return response