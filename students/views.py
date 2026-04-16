from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student
from .forms import StudentForm, RegisterForm

# ==========================================
# AUTH VIEWS
# ==========================================


def login_view(request):
    # If user is already logged in, redirect to student list
    if request.user.is_authenticated:
        return redirect("student_list")

    error = None

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if not email or not password:
            error = "Please enter both email and password."
        else:
            # Authenticate user by email
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
            except User.DoesNotExist:
                user = None
            if user is not None:
                login(request, user)
                return redirect("student_list")
            else:
                error = "Invalid email or password."

    # Handle GET request (show login page) or POST with errors
    return render(request, "students/login.html", {"error": error})


def register_view(request):
    # If user is already logged in, redirect
    if request.user.is_authenticated:
        return redirect("student_list")

    form = RegisterForm()

    # Handle POST request (registration form submit)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.save()

            messages.success(request, "Account created successfully! Please login.")
            return redirect("login")

    # Show registration form (GET or invalid POST)
    return render(request, "students/register.html", {"form": form})


def logout_view(request):
    # Logout the user
    logout(request)
    return redirect("login")


# ==========================================
# STUDENT CRUD VIEWS
# ==========================================


@login_required(login_url="login")
def student_list(request):
    # Get search query
    query = request.GET.get("q", "")

    # Get all students ordered by latest
    students = Student.objects.all().order_by("-created_at")

    # Apply search filter if query exists
    if query:
        students = students.filter(name__icontains=query)

    # Render student list page
    return render(
        request,
        "students/list.html",
        {
            "students": students,
            "query": query,
            "total": Student.objects.count(),
        },
    )


@login_required(login_url="login")
def student_create(request):
    form = StudentForm()

    # Handle form submission
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect("student_list")

    # Show form (GET or invalid POST)
    return render(
        request,
        "students/form.html",
        {"form": form, "title": "Add New Student", "btn": "Add Student"},
    )


@login_required(login_url="login")
def student_update(request, pk):
    # Get student object
    student = get_object_or_404(Student, pk=pk)

    form = StudentForm(instance=student)

    # Handle update request
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect("student_list")

    # Show update form (GET or invalid POST)
    return render(
        request,
        "students/form.html",
        {"form": form, "title": "Update Student", "btn": "Update Student"},
    )


@login_required(login_url="login")
def student_delete(request, pk):
    # Get student object
    student = get_object_or_404(Student, pk=pk)

    # Handle delete confirmation
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect("student_list")

    # Show confirmation page
    return render(request, "students/confirm_delete.html", {"student": student})
