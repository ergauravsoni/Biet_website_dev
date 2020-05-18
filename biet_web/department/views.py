from django.shortcuts import render
from .models import mechanical_dept, biotechnology_dept, chemical_dept, chemistry_dept, civil_dept
from .models import computer_science_dept, electronics_and_communication_dept, electrical_and_electronics_dept
from .models import information_science_dept, mathematics_dept, physics_dept, textile_dept, mca_dept, environmental_dept
from .models import civil_depatment_gallery, mechanical_dept_gallery, biotechnology_dept_gallery, chemical_dept_gallery
from .models import chemistry_dept_gallery, computer_science_dept_gallery, electronics_and_communication_gallery
from .models import electrical_and_electronics_gallery, information_science_dept_gallery, mathematics_dept_gallery
from .models import physics_dept_gallery, textile_dept_gallery, mca_dept_gallery, environmental_dept_gallery

# Create your views here.


def achievements(request, course, dept):
    print(dept, course)
    return render(request, 'department/'+course+'/' + dept + '/achievements.html')


def activities(request, course, dept):
    print(dept)
    return render(request, 'department/'+course+'/' + dept + '/activities.html')


def faculty(request, course, dept):
    print(dept)

    if course == 'UG' and dept == 'BT':
        faculties_data = biotechnology_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'CV':
        faculties_data = civil_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'ME':
        faculties_data = mechanical_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'CH':
        faculties_data = chemical_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'CHE':
        faculties_data = chemistry_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'CS':
        faculties_data = computer_science_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'EC':
        faculties_data = electronics_and_communication_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'EEE':
        faculties_data = electrical_and_electronics_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'EI':
        faculties_data = biotechnology_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'IS':
        faculties_data = information_science_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'MAT':
        faculties_data = mathematics_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'PHY':
        faculties_data = physics_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'TX':
        faculties_data = textile_dept.objects.all().order_by('image')

        for faculty_data in faculties_data:
            print(faculty_data.name, faculty_data.designation,
                  faculty_data.image, faculty_data.detail)

    return render(request, 'department/'+course+'/' + dept + '/faculty.html', {'faculties_data': faculties_data})


def gallery(request, course, dept):
    print(dept)
    if course == 'UG' and dept == 'BT':
        images = biotechnology_dept_gallery.objects.all()
    elif course == 'UG' and dept == 'CV':
        images = civil_depatment_gallery.objects.all()
    elif course == 'UG' and dept == 'ME':
        images = mechanical_dept_gallery.objects.all()
    elif course == 'UG' and dept == 'CH':
        images = chemical_dept_gallery.objects.all()
    elif course == 'UG' and dept == 'CHE':
        images = chemistry_dept_gallery.objects.all()
    elif course == 'UG' and dept == 'CS':
        images = computer_science_dept_gallery.objects.all()
    elif course == 'UG' and dept == 'EC':
        images = electronics_and_communication_gallery.objects.all()
    elif course == 'UG' and dept == 'EEE':
        images = electrical_and_electronics_gallery.objects.all()
    elif course == 'UG' and dept == 'EI':
        images = biotechnology_dept.objects.all()
    elif course == 'UG' and dept == 'IS':
        facuimageslties_data = information_science_dept_gallery.objects.all()
    elif course == 'UG' and dept == 'MAT':
        images = mathematics_dept_gallery.objects.all()
    elif course == 'UG' and dept == 'PHY':
        images = physics_dept_gallery.objects.all()
    elif course == 'UG' and dept == 'TX':
        images = textile_dept_gallery.objects.all()

    return render(request, 'department/'+course+'/' + dept + '/gallery.html', {'images': images})


def home(request, course, dept):
    print(dept)
    # print(dept)

    if course == 'UG' and dept == 'BT':
        faculties_data = biotechnology_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'CV':
        faculties_data = civil_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'ME':
        faculties_data = mechanical_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'CH':
        faculties_data = chemical_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'CHE':
        faculties_data = chemistry_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'CS':
        faculties_data = computer_science_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'EC':
        faculties_data = electronics_and_communication_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'EEE':
        faculties_data = electrical_and_electronics_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'EI':
        faculties_data = biotechnology_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'IS':
        faculties_data = information_science_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'MAT':
        faculties_data = mathematics_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'PHY':
        faculties_data = physics_dept.objects.all().order_by('image')
    elif course == 'UG' and dept == 'TX':
        faculties_data = textile_dept.objects.all().order_by('image')

        for faculty_data in faculties_data:
            print(faculty_data.name, faculty_data.designation,
                  faculty_data.image, faculty_data.detail)

    return render(request, 'department/'+course+'/' + dept + '/home.html', {'faculties_data': faculties_data})


def infrastructure(request, course, dept):
    print(dept)
    return render(request, 'department/'+course+'/' + dept + '/infrastructure.html')


def profile(request, course, dept):
    print(dept)
    return render(request, 'department/'+course+'/'+dept+'/profile.html')


def research(request, course, dept):
    print(dept)
    return render(request, 'department/'+course+'/'+dept+'/research.html')


def psopso(request, course, dept):
    print(dept)
    return render(request, 'department/'+course+'/'+dept+'/psopso.html')


def newsletter(request, course, dept):
    print(dept)
    return render(request, 'department/'+course+'/'+dept+'/newsletter.html')
