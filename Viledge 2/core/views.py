from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout  # Correct import
import random
import string
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Complaint
from .forms import ComplaintForm
from django.http import JsonResponse

from django.shortcuts import render
from core.models import Complaint

# views.py
# views.py
from django.http import JsonResponse
from core.models import Complaint

def complaint_counts(request):
    # Count the complaints based on their status
    total_complaints = Complaint.objects.count()
    pending_complaints = Complaint.objects.filter(status='pending').count()
    solved_complaints = Complaint.objects.filter(status='solved').count()

    # Return the counts as a JSON response
    return JsonResponse({
        'total_complaints': total_complaints,
        'pending_complaints': pending_complaints,
        'solved_complaints': solved_complaints,
    })




def home(request):
    return render(request, "auth/home.html")

def login_view(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Correct usage of the login function from django.contrib.auth
            return redirect('dashboard')  # Redirect to a success page or dashboard
        else:
            return render(request, "auth/login.html", {'form': form})  # Return the form with errors
    else:
        initial_data={'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
        return render(request, "auth/login.html", {'form': form})

def dashboard(request):
    return render(request, "auth/dashboard.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the homepage or a success page after signup
    else:
        initial_data={'username':'', 'password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)

    return render(request, 'auth/signup.html', {'form': form})

# Other views remain the same...


def depart(request):
    return render(request, "auth/depart.html")

def status(request):
    return render(request, "auth/status.html")

def complaint_form(request):
    return render(request, "auth/complaint_form.html")


    
    # Pass the complaint_id to the template
    return render(request, 'auth/complaint_success.html', {'complaint_id': complaint_id})

def track(request):
    return render(request, "auth/track.html")

def aboutUs(request):
    return render(request, "auth/aboutus.html")


def transport(request):
    return render(request, "auth/transport.html")

def water(request):
    return render(request, "auth/water.html")


def electricity(request):
    return render(request, "auth/electricity.html")

def health(request):
    return render(request, "auth/health.html")


def education(request):
    return render(request, "auth/education.html")

def agriculture(request):
    return render(request, "auth/agriculture.html")

# Admin panel



def role_selection(request):
    if request.method == "POST":
        # Get the role from the POST data
        role = request.POST.get('role')

        # Redirect based on the role selected
        if role == 'user':
            return redirect("login")# Redirect to user home page
        elif role == 'admin':
            return redirect('admin_login')  # Redirect to admin login page
        else:
            return HttpResponse("Invalid role selected.")
    return render(request, 'auth/select_role.html')  # Render the role selection page




def admin_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Ensure the user is an admin
            if user.is_staff:
                login(request, user)  # Login the admin user
                return redirect('admin_dashboard')  # Redirect to admin dashboard or another page
            else:
                # If the user is not an admin, return an error message
                form.add_error(None, "You do not have admin privileges.")
                return render(request, "auth/admin_login.html", {'form': form})
        else:
            return render(request, "auth/admin_login.html", {'form': form})
    else:
        initial_data={'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
        return render(request, "auth/admin_login.html", {'form': form})
    



def villager_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_villager:
            login(request, user)
            return redirect("dashboard.html")  # Replace with your villager dashboard URL name
        else:
            messages.error(request, "Invalid credentials or not a villager.")
    return render(request, "login.html")

def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_admin:
            login(request, user)
            return redirect("admin_dashboard")  # Replace with your admin dashboard URL name
        else:
            messages.error(request, "Invalid credentials or not an admin.")
    return render(request, "admin_login.html")

from .middleware import villager_required, admin_required

@villager_required
def villager_dashboard(request):
    # Villager dashboard logic
    return render(request, "villager_dashboard.html")

@admin_required
def admin_dashboard(request):
    # Admin dashboard logic
    return render(request, "admin_dashboard.html")



from django.shortcuts import render, redirect
from .models import Complaint
from django.http import HttpResponse
import random
import string

# Function to generate a random complaint ID
def generate_complaint_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))



from django.utils import timezone
from django.shortcuts import render
from .models import Complaint

def complaint_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        department = request.POST.get('department')
        address = request.POST.get('address')
        complaint_desc = request.POST.get('complaint')

        # Generate the complaint ID
        complaint_id = generate_complaint_id()

        # Capture the current date and time
        created_at = timezone.now()  # Get the current date and time

        # Create and save the complaint
        complaint = Complaint(
            name=name,
            phone=phone,
            location=location,
            department=department,
            address=address,
            complaint=complaint_desc,
            complaint_id=complaint_id,
            created_at=created_at  # Store the date and time of submission
        )
        complaint.save()

        # Redirect to the success page and pass the complaint_id and created_at
        return render(request, 'auth/complaint_submit.html', {'complaint_id': complaint.complaint_id, 'created_at': complaint.created_at})

    # Fetch all complaints to display in the complaint list
    complaints = Complaint.objects.all()

    # Render the complaint list page with all complaints
    return render(request, 'auth/admin_dashboard.html', {'complaints': complaints})



def complaint_dashboard(request):
    # Fetch statistics
    total_complaints = Complaint.objects.count()
    pending_complaints = Complaint.objects.filter(status='Pending').count()
    solved_complaints = Complaint.objects.filter(status='Solved').count()

    # Pass data to the template
    return render(request, 'auth/complaint_dashboard.html', {
        'total_complaints': total_complaints,
        'pending_complaints': pending_complaints,
        'solved_complaints': solved_complaints,
    })

def admin_layout(request):
    return render(request, "layouts/admin_layout.html")

def complaint_page(request):
    



    complaints = Complaint.objects.all()  # Get all complaints initially

    # Filter by department if provided
    department = request.GET.get('department', 'all')
    if department != 'all':
        complaints = complaints.filter(department=department)

    # Filter by status if provided
    status = request.GET.get('status', 'all')
    if status != 'all':
        complaints = complaints.filter(status=status)

    # Filter by date range if provided
    date_from = request.GET.get('date-from', None)
    date_to = request.GET.get('date-to', None)
    if date_from and date_to:
        complaints = complaints.filter(created_at__range=[date_from, date_to])

    # Filter by search term if provided
    search_term = request.GET.get('search', '')
    if search_term:
        complaints = complaints.filter(Q(name__icontains=search_term) | Q(complaint_id__icontains=search_term))

    return render(request, "auth/complaint.html", {'complaints': complaints})





def complaint_details(request, complaint_id):
    # Fetch the complaint based on the ID or return a 404 if not found
    complaint = get_object_or_404(Complaint, complaint_id=complaint_id)
    
    # Pass the complaint data to the template
    return render(request, 'auth/complaint_details.html', {'complaint': complaint})


def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, complaint_id=complaint_id)

    if request.method == 'POST':
        status = request.POST.get('status')
        complaint.status = status  # Update the status
        complaint.save()  # Save the updated complaint

        return redirect('complaint_page')  # Redirect back to the complaint page (or wherever)

    return render(request, 'complaint_details.html', {'complaint': complaint})


from django.shortcuts import render
from .models import Complaint

def status(request):
    complaint = None
    error = None
    
    if request.method == 'POST':
        complaint_id = request.POST.get('complaint-id')
        
        try:
            # Fetch the complaint using the provided ID
            complaint = Complaint.objects.get(complaint_id=complaint_id)
        except Complaint.DoesNotExist:
            error = "Complaint ID not found. Please try again."
    
    return render(request, 'auth/status.html', {'complaint': complaint, 'error': error})




def update_complaint_status(request, complaint_id):
    # Retrieve the complaint using the string complaint_id
    complaint = get_object_or_404(Complaint, complaint_id=complaint_id)

    if request.method == 'POST':
        # Update the complaint status
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()  # Save the updated status
            return redirect('complaint_page')  # Redirect to the complaint management page

    else:
        # Render the form with current complaint details
        form = ComplaintForm(instance=complaint)

    return render(request, 'auth/complaint.html', {'form': form, 'complaint': complaint})



def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        complaint.status = status
        complaint.save()

    return redirect('complaint_page')  # Redirecting back to the complaint management page



# In your app's views.py file
from django.http import JsonResponse
from .models import Complaint
from django.http import JsonResponse
import json

def update_bulk_complaint_status(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body of the request
            data = json.loads(request.body)
            new_status = data.get('status')
            complaint_ids = data.get('complaintIds')  # Expecting a list of IDs

            # Update the status for each complaint
            complaints = Complaint.objects.filter(id__in=complaint_ids)
            complaints.update(status=new_status)

            # Return a JSON response confirming the update
            return JsonResponse({'status': 'success', 'message': 'Complaints updated successfully!'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)