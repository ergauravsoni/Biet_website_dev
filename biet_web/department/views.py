from django.shortcuts import render
from .models import mechanical_dept, biotechnology_dept, chemical_dept, chemistry_dept, civil_dept
from .models import computer_science_dept, electronics_and_communication_dept, electrical_and_electronics_dept
from .models import information_science_dept, mathematics_dept, physics_dept, textile_dept, mca_dept, environmental_dept
from .models import civil_dept_gallery, mechanical_dept_gallery, biotechnology_dept_gallery, chemical_dept_gallery
from .models import chemistry_dept_gallery, computer_science_dept_gallery, electronics_and_communication_gallery
from .models import electrical_and_electronics_gallery, information_science_dept_gallery, mathematics_dept_gallery
from .models import physics_dept_gallery, textile_dept_gallery, mca_dept_gallery, environmental_dept_gallery
from .models import computer_science_dept_lab_facilities, computer_science_dept_major_equipments, computer_science_dept_activities
from .models import computer_science_dept_classroom,computer_science_dept_events
from .models import computer_science_dept_achievements, computer_science_dept_timetable
from .models import computer_science_dept_research_scholars, computer_science_dept_research_guide,computer_science_dept_laboratory_facilities_gallary
from .models import computer_science_dept_book_chapters, computer_science_dept_publications, computer_science_dept_accreditation
from .models import physics_dept_lab_facilities, physics_dept_activities, physics_dept_major_equipments, physics_dept_achievements
from .models import physics_dept_timetable, physics_dept_events, physics_dept_classroom, physics_dept_research_guide, physics_dept_research_scholars
from .models import physics_dept_laboratory_facilities_gallary, physics_dept_book_chapters, physics_dept_publications
from .models import chemistry_dept_lab_facilities, chemistry_dept_activities, chemistry_dept_major_equipments, chemistry_dept_achievements
from .models import chemistry_dept_timetable, chemistry_dept_events, chemistry_dept_classroom, chemistry_dept_research_guide, chemistry_dept_research_scholars
from .models import chemistry_dept_laboratory_facilities_gallary, chemistry_dept_book_chapters, chemistry_dept_publications
from .models import mathematics_dept_lab_facilities, mathematics_dept_activities, mathematics_dept_major_equipments, mathematics_dept_achievements
from .models import mathematics_dept_timetable, mathematics_dept_events, mathematics_dept_classroom, mathematics_dept_research_guide, mathematics_dept_research_scholars
from .models import mathematics_dept_laboratory_facilities_gallary, mathematics_dept_book_chapters, mathematics_dept_publications
from .models import civil_dept_lab_facilities, civil_dept_activities, civil_dept_major_equipments, civil_dept_achievements
from .models import civil_dept_timetable, civil_dept_events, civil_dept_classroom, civil_dept_research_guide, civil_dept_research_scholars
from .models import civil_dept_laboratory_facilities_gallary, civil_dept_book_chapters, civil_dept_publications
from .models import mechanical_dept_lab_facilities, mechanical_dept_activities, mechanical_dept_major_equipments, mechanical_dept_achievements
from .models import mechanical_dept_timetable, mechanical_dept_events, mechanical_dept_classroom, mechanical_dept_research_guide, mechanical_dept_research_scholars
from .models import mechanical_dept_laboratory_facilities_gallary, mechanical_dept_book_chapters, mechanical_dept_publications
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
    elif course == 'UG' and dept == 'EE':
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
    elif course == 'UG' and dept == 'EE':
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
    
        content = {'faculties_data': faculties_data
                }
                    
    elif course == 'UG' and dept == 'CV':
        
        faculties_data = civil_dept.objects.all().order_by('image')
        achievements_data = civil_dept_achievements.objects.all()
        activities_data = civil_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = civil_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = civil_dept_major_equipments.objects.all()
        images = civil_dept_gallery.objects.all()
        timetable_data = civil_dept_timetable.objects.order_by('semester', 'section')
        events = civil_dept_events.objects.all()
        classrooms = civil_dept_classroom.objects.all()
        laboratory_facilities_gallary = civil_dept_laboratory_facilities_gallary.objects.all()
        research_scholar_data = civil_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = civil_dept_research_guide.objects.all().order_by('sno')
        book_chapters_data = civil_dept_book_chapters.objects.all()
        publications_data = civil_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))
    
        content = {'faculties_data': faculties_data,
                    'achievements_data': achievements_data,
                    'activities_data': activities_data,
                    'lab_facilities_data': lab_facilities_data,
                    'major_equipments_data': major_equipments_data,
                    'images': images,
                    'timetable_data': timetable_data,
                     'events': events,
                     'classrooms': classrooms,
                    'research_data': research_data,
                    'laboratory_facilities_gallary' : laboratory_facilities_gallary,
                    'book_chapters_data': book_chapters_data,
                    'publications_data': publications_data
                }
    
    elif course == 'UG' and dept == 'ME':
        
        faculties_data = mechanical_dept.objects.all().order_by('image')
        achievements_data = mechanical_dept_achievements.objects.all()
        activities_data = mechanical_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = mechanical_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = mechanical_dept_major_equipments.objects.all()
        images = mechanical_dept_gallery.objects.all()
        timetable_data = mechanical_dept_timetable.objects.order_by('semester', 'section')
        events = mechanical_dept_events.objects.all()
        classrooms = mechanical_dept_classroom.objects.all()
        laboratory_facilities_gallary = mechanical_dept_laboratory_facilities_gallary.objects.all()
        research_scholar_data = mechanical_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = mechanical_dept_research_guide.objects.all().order_by('sno')
        book_chapters_data = mechanical_dept_book_chapters.objects.all()
        publications_data = mechanical_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))
    
        content = {'faculties_data': faculties_data,
                    'achievements_data': achievements_data,
                    'activities_data': activities_data,
                    'lab_facilities_data': lab_facilities_data,
                    'major_equipments_data': major_equipments_data,
                    'images': images,
                    'timetable_data': timetable_data,
                     'events': events,
                     'classrooms': classrooms,
                    'research_data': research_data,
                    'laboratory_facilities_gallary' : laboratory_facilities_gallary,
                    'book_chapters_data': book_chapters_data,
                    'publications_data': publications_data
                }    
    
    elif course == 'UG' and dept == 'CH':
    
        faculties_data = chemical_dept.objects.all().order_by('image')
    
        content = {'faculties_data': faculties_data
                }    
    
    elif course == 'UG' and dept == 'CHE':
        
        faculties_data = chemistry_dept.objects.all().order_by('image')
        achievements_data = chemistry_dept_achievements.objects.all()
        activities_data = chemistry_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = chemistry_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = chemistry_dept_major_equipments.objects.all()
        images = chemistry_dept_gallery.objects.all()
        timetable_data = chemistry_dept_timetable.objects.order_by('semester', 'section')
        events = chemistry_dept_events.objects.all()
        classrooms = chemistry_dept_classroom.objects.all()
        laboratory_facilities_gallary = chemistry_dept_laboratory_facilities_gallary.objects.all()
        research_scholar_data = chemistry_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = chemistry_dept_research_guide.objects.all().order_by('sno')
        book_chapters_data = chemistry_dept_book_chapters.objects.all()
        publications_data = chemistry_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))
    
        content = {'faculties_data': faculties_data,
                    'achievements_data': achievements_data,
                    'activities_data': activities_data,
                    'lab_facilities_data': lab_facilities_data,
                    'major_equipments_data': major_equipments_data,
                    'images': images,
                    'timetable_data': timetable_data,
                     'events': events,
                     'classrooms': classrooms,
                    'research_data': research_data,
                    'laboratory_facilities_gallary' : laboratory_facilities_gallary,
                    'book_chapters_data': book_chapters_data,
                    'publications_data': publications_data
                }    
    
    elif course == 'UG' and dept == 'CS':

        faculties_data = computer_science_dept.objects.all().order_by('sno')
        achievements_data = computer_science_dept_achievements.objects.all()
        activities_data = computer_science_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = computer_science_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = computer_science_dept_major_equipments.objects.all()
        images = computer_science_dept_gallery.objects.all()
        timetable_data = computer_science_dept_timetable.objects.order_by('semester', 'section')


        events = computer_science_dept_events.objects.all()
        classrooms = computer_science_dept_classroom.objects.all()
        laboratory_facilities_gallary = computer_science_dept_laboratory_facilities_gallary.objects.all()

        print(laboratory_facilities_gallary)
        research_scholar_data = computer_science_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = computer_science_dept_research_guide.objects.all().order_by('sno')


        book_chapters_data = computer_science_dept_book_chapters.objects.all()
        publications_data = computer_science_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        accreditation_data = computer_science_dept_accreditation.objects.all().order_by('sno')
        
        content = {'faculties_data': faculties_data,
                    'achievements_data': achievements_data,
                    'activities_data': activities_data,
                    'lab_facilities_data': lab_facilities_data,
                    'major_equipments_data': major_equipments_data,
                    'images': images,
                    'timetable_data': timetable_data,
                    'events': events,
                    'classrooms': classrooms,
                    'research_data': research_data,
                    'laboratory_facilities_gallary' : laboratory_facilities_gallary,
                    'book_chapters_data': book_chapters_data,
                    'publications_data': publications_data,
                    'accreditation_data': accreditation_data
                }

    elif course == 'UG' and dept == 'EC':
        
        faculties_data = electronics_and_communication_dept.objects.all().order_by('image')
        
        content = {'faculties_data': faculties_data
                }
        
    elif course == 'UG' and dept == 'EE':

        faculties_data = electrical_and_electronics_dept.objects.all().order_by('image')

        content = {'faculties_data': faculties_data
                }
                
    elif course == 'UG' and dept == 'EI':
        
        faculties_data = biotechnology_dept.objects.all().order_by('image')
    
        content = {'faculties_data': faculties_data
                }    
    
    elif course == 'UG' and dept == 'IS':
        
        faculties_data = information_science_dept.objects.all().order_by('image')

        content = {'faculties_data': faculties_data
                }

    elif course == 'UG' and dept == 'MAT':
        
        faculties_data = mathematics_dept.objects.all().order_by('image')
        achievements_data = mathematics_dept_achievements.objects.all()
        activities_data = mathematics_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = mathematics_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = mathematics_dept_major_equipments.objects.all()
        images = mathematics_dept_gallery.objects.all()
        timetable_data = mathematics_dept_timetable.objects.order_by('semester', 'section')
        events = mathematics_dept_events.objects.all()
        classrooms = mathematics_dept_classroom.objects.all()
        laboratory_facilities_gallary = mathematics_dept_laboratory_facilities_gallary.objects.all()
        research_scholar_data = mathematics_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = mathematics_dept_research_guide.objects.all().order_by('sno')
        book_chapters_data = mathematics_dept_book_chapters.objects.all()
        publications_data = mathematics_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))
    
        content = {'faculties_data': faculties_data,
                    'achievements_data': achievements_data,
                    'activities_data': activities_data,
                    'lab_facilities_data': lab_facilities_data,
                    'major_equipments_data': major_equipments_data,
                    'images': images,
                    'timetable_data': timetable_data,
                     'events': events,
                     'classrooms': classrooms,
                    'research_data': research_data,
                    'laboratory_facilities_gallary' : laboratory_facilities_gallary,
                    'book_chapters_data': book_chapters_data,
                    'publications_data': publications_data
                }    
    
    elif course == 'UG' and dept == 'PHY':
        
        faculties_data = physics_dept.objects.all().order_by('image')
        achievements_data = physics_dept_achievements.objects.all()
        activities_data = physics_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = physics_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = physics_dept_major_equipments.objects.all()
        images = physics_dept_gallery.objects.all()
        timetable_data = physics_dept_timetable.objects.order_by('semester', 'section')
        events = physics_dept_events.objects.all()
        classrooms = physics_dept_classroom.objects.all()
        laboratory_facilities_gallary = physics_dept_laboratory_facilities_gallary.objects.all()
        research_scholar_data = physics_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = physics_dept_research_guide.objects.all().order_by('sno')
        book_chapters_data = physics_dept_book_chapters.objects.all()
        publications_data = physics_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        content = {'faculties_data': faculties_data,
                    'achievements_data': achievements_data,
                    'activities_data': activities_data,
                    'lab_facilities_data': lab_facilities_data,
                    'major_equipments_data': major_equipments_data,
                    'images': images,
                    'timetable_data': timetable_data,
                     'events': events,
                     'classrooms': classrooms,
                    'research_data': research_data,
                    'laboratory_facilities_gallary' : laboratory_facilities_gallary,
                    'book_chapters_data': book_chapters_data,
                    'publications_data': publications_data
                }

    elif course == 'UG' and dept == 'TX':

        faculties_data = textile_dept.objects.all().order_by('image')

        for faculty_data in faculties_data:
            print(faculty_data.name, faculty_data.designation,
                  faculty_data.image, faculty_data.detail)

        content = {'faculties_data': faculties_data
                }
                
    elif course == 'UG' and dept == 'BM':
        
        faculties_data = physics_dept.objects.all().order_by('image')

        content = {'faculties_data': faculties_data
                }


    return render(request, 'department/'+course+'/' + dept + '/home.html', content)


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
