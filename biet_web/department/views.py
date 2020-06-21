from django.shortcuts import render
from .models import mechanical_dept, biotechnology_dept, chemical_dept, chemistry_dept, civil_dept
from .models import computer_science_dept, electronics_and_communication_dept, electrical_and_electronics_dept
from .models import information_science_dept, mathematics_dept, physics_dept, textile_dept, mca_dept, environmental_dept
from .models import civil_depatment_gallery, mechanical_dept_gallery, biotechnology_dept_gallery, chemical_dept_gallery
from .models import chemistry_dept_gallery, computer_science_dept_gallery, electronics_and_communication_gallery
from .models import electrical_and_electronics_gallery, information_science_dept_gallery, mathematics_dept_gallery
from .models import physics_dept_gallery, textile_dept_gallery, mca_dept_gallery, environmental_dept_gallery
from .models import computer_science_dept_lab_facilities, computer_science_dept_major_equipments, computer_science_dept_activities
from .models import computer_science_dept_classroom,computer_science_dept_events
from .models import computer_science_dept_achievements, computer_science_dept_timetable
from .models import computer_science_dept_research_scholars, computer_science_dept_research_guide,computer_science_dept_laboratory_facilities_gallary
from .models import computer_science_dept_book_chapters, computer_science_dept_publications, computer_science_dept_accreditation
from .models import information_science_dept_lab_facilities, information_science_dept_major_equipments, information_science_dept_activities
from .models import information_science_dept_classroom,information_science_dept_events
from .models import information_science_dept_achievements, information_science_dept_timetable
from .models import information_science_dept_research_scholars, information_science_dept_research_guide,information_science_dept_laboratory_facilities_gallary
from .models import information_science_dept_book_chapters, information_science_dept_publications, information_science_dept_accreditation
from .models import electrical_and_electronics_dept_lab_facilities, electrical_and_electronics_dept_major_equipments, electrical_and_electronics_dept_activities
from .models import electrical_and_electronics_dept_classroom,electrical_and_electronics_dept_events
from .models import electrical_and_electronics_dept_achievements, electrical_and_electronics_dept_timetable
from .models import electrical_and_electronics_dept_research_scholars, electrical_and_electronics_dept_research_guide,electrical_and_electronics_dept_laboratory_facilities_gallary
from .models import electrical_and_electronics_dept_book_chapters, electrical_and_electronics_dept_publications, electrical_and_electronics_dept_accreditation
from .models import electronics_and_communication_dept_lab_facilities, electronics_and_communication_dept_major_equipments, electronics_and_communication_dept_activities
from .models import electronics_and_communication_dept_classroom,electronics_and_communication_dept_events
from .models import electronics_and_communication_dept_achievements, electronics_and_communication_dept_timetable
from .models import electronics_and_communication_dept_research_scholars, electronics_and_communication_dept_research_guide,electronics_and_communication_dept_laboratory_facilities_gallary
from .models import electronics_and_communication_dept_book_chapters, electronics_and_communication_dept_publications, electronics_and_communication_dept_accreditation
from .models import biotechnology_dept_lab_facilities, biotechnology_dept_major_equipments, biotechnology_dept_activities
from .models import biotechnology_dept_classroom,biotechnology_dept_events
from .models import biotechnology_dept_achievements, biotechnology_dept_timetable
from .models import biotechnology_dept_research_scholars, biotechnology_dept_research_guide,biotechnology_dept_laboratory_facilities_gallary
from .models import biotechnology_dept_book_chapters, biotechnology_dept_publications, biotechnology_dept_accreditation
from .models import mca_dept_lab_facilities, mca_dept_major_equipments, mca_dept_activities
from .models import mca_dept_classroom,mca_dept_events
from .models import mca_dept_achievements, mca_dept_timetable
from .models import mca_dept_research_scholars, mca_dept_research_guide,mca_dept_laboratory_facilities_gallary
from .models import mca_dept_book_chapters, mca_dept_publications, mca_dept_accreditation
from .models import environmental_dept_lab_facilities, environmental_dept_major_equipments, environmental_dept_activities
from .models import environmental_dept_classroom,environmental_dept_events
from .models import environmental_dept_achievements, environmental_dept_timetable
from .models import environmental_dept_research_scholars, environmental_dept_research_guide,environmental_dept_laboratory_facilities_gallary
from .models import environmental_dept_book_chapters, environmental_dept_publications, environmental_dept_accreditation
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
    elif course == 'UG' and dept == 'ENV':
        faculties_data = environmental_dept.objects.all().order_by('image')
    elif course == 'PG' and dept == 'MCA':
        faculties_data = mca_dept.objects.all().order_by('image')

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
    elif course == 'UG' and dept == 'ENV':
        images = environmental_dept_gallery.objects.all()
    elif course == 'PG' and dept == 'MCA':
        images = mca_dept_gallery.objects.all()


    return render(request, 'department/'+course+'/' + dept + '/gallery.html', {'images': images})


def home(request, course, dept):
    print(dept)
    # print(dept)

    if course == 'UG' and dept == 'BT':
       
        faculties_data = biotechnology_dept.objects.all().order_by('image')
        achievements_data = biotechnology_dept_achievements.objects.all()
        activities_data = biotechnology_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = biotechnology_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = biotechnology_dept_major_equipments.objects.all()
        images = biotechnology_dept_gallery.objects.all()
        timetable_data = biotechnology_dept_timetable.objects.order_by('semester', 'section')
        events = biotechnology_dept_events.objects.all()
        classrooms = biotechnology_dept_classroom.objects.all()
        laboratory_facilities_gallary = biotechnology_dept_laboratory_facilities_gallary.objects.all()

        print(laboratory_facilities_gallary)
        research_scholar_data = biotechnology_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = biotechnology_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = biotechnology_dept_book_chapters.objects.all()
        publications_data = biotechnology_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        accreditation_data = biotechnology_dept_accreditation.objects.all().order_by('sno')
        
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
                       
    elif course == 'UG' and dept == 'CV':
        
        faculties_data = civil_dept.objects.all().order_by('image')
    
        content = {'faculties_data': faculties_data
                }
    
    elif course == 'UG' and dept == 'ME':
        
        faculties_data = mechanical_dept.objects.all().order_by('image')
    
        content = {'faculties_data': faculties_data
                }    
    
    elif course == 'UG' and dept == 'CH':
    
        faculties_data = chemical_dept.objects.all().order_by('image')
    
        content = {'faculties_data': faculties_data
                }    
    
    elif course == 'UG' and dept == 'CHE':
        
        faculties_data = chemistry_dept.objects.all().order_by('image')
    
        content = {'faculties_data': faculties_data
                }    
    
    elif course == 'UG' and dept == 'CS':

        faculties_data = computer_science_dept.objects.all().order_by('sno')
        achievements_data = computer_science_dept_achievements.objects.all()
        activities_data = computer_science_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = computer_science_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = computer_science_dept_major_equipments.objects.all()
        images = computer_science_dept_gallery.objects.all()
        timetable_data = computer_science_dept_timetable.objects.order_by(
            'semester', 'section')


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
        achievements_data = electronics_and_communication_dept_achievements.objects.all()
        activities_data = electronics_and_communication_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = electronics_and_communication_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = electronics_and_communication_dept_major_equipments.objects.all()
        images = electronics_and_communication_dept_gallery.objects.all()
        timetable_data = electronics_and_communication_dept_timetable.objects.order_by('semester', 'section')
        events = electronics_and_communication_dept_events.objects.all()
        classrooms = electronics_and_communication_dept_classroom.objects.all()
        laboratory_facilities_gallary = electronics_and_communication_dept_laboratory_facilities_gallary.objects.all()

        print(laboratory_facilities_gallary)
        research_scholar_data = electronics_and_communication_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = electronics_and_communication_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = electronics_and_communication_dept_book_chapters.objects.all()
        publications_data = electronics_and_communication_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        accreditation_data = electronics_and_communication_dept_accreditation.objects.all().order_by('sno')
        
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

    elif course == 'UG' and dept == 'EE':

        faculties_data = electrical_and_electronics_dept.objects.all().order_by('image')
        achievements_data = electrical_and_electronics_dept_achievements.objects.all()
        activities_data = electrical_and_electronics_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = electrical_and_electronics_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = electrical_and_electronics_dept_major_equipments.objects.all()
        images = electrical_and_electronics_dept_gallery.objects.all()
        timetable_data = electrical_and_electronics_dept_timetable.objects.order_by('semester', 'section')
        events = electrical_and_electronics_dept_events.objects.all()
        classrooms = electrical_and_electronics_dept_classroom.objects.all()
        laboratory_facilities_gallary = electrical_and_electronics_dept_laboratory_facilities_gallary.objects.all()

        print(laboratory_facilities_gallary)
        research_scholar_data = electrical_and_electronics_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = electrical_and_electronics_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = electrical_and_electronics_dept_book_chapters.objects.all()
        publications_data = electrical_and_electronics_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        accreditation_data = electrical_and_electronics_dept_accreditation.objects.all().order_by('sno')
        
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
                        
    elif course == 'UG' and dept == 'EI':
        
        faculties_data = biotechnology_dept.objects.all().order_by('image')
    
        content = {'faculties_data': faculties_data
                }    
    
    elif course == 'UG' and dept == 'IS':
        
        faculties_data = information_science_dept.objects.all().order_by('image')
        achievements_data = information_science_dept_achievements.objects.all()
        activities_data = information_science_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = information_science_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = information_science_dept_major_equipments.objects.all()
        images = information_science_dept_gallery.objects.all()
        timetable_data = information_science_dept_timetable.objects.order_by('semester', 'section')
        events = information_science_dept_events.objects.all()
        classrooms = information_science_dept_classroom.objects.all()
        laboratory_facilities_gallary = information_science_dept_laboratory_facilities_gallary.objects.all()

        print(laboratory_facilities_gallary)
        research_scholar_data = information_science_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = information_science_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = information_science_dept_book_chapters.objects.all()
        publications_data = information_science_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        accreditation_data = information_science_dept_accreditation.objects.all().order_by('sno')
        
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
       
    elif course == 'UG' and dept == 'MAT':
        
        faculties_data = mathematics_dept.objects.all().order_by('image')
    
        content = {'faculties_data': faculties_data
                }    
    
    elif course == 'UG' and dept == 'PHY':
        
        faculties_data = physics_dept.objects.all().order_by('image')

        content = {'faculties_data': faculties_data
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

    if course == 'UG' and dept == 'ENV':
       
        faculties_data = environmental_dept.objects.all().order_by('image')
        achievements_data = environmental_dept_achievements.objects.all()
        activities_data = environmental_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = environmental_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = environmental_dept_major_equipments.objects.all()
        images = environmental_dept_gallery.objects.all()
        timetable_data = environmental_dept_timetable.objects.order_by('semester', 'section')
        events = environmental_dept_events.objects.all()
        classrooms = environmental_dept_classroom.objects.all()
        laboratory_facilities_gallary = environmental_dept_laboratory_facilities_gallary.objects.all()

        print(laboratory_facilities_gallary)
        research_scholar_data = environmental_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = environmental_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = environmental_dept_book_chapters.objects.all()
        publications_data = environmental_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        accreditation_data = environmental_dept_accreditation.objects.all().order_by('sno')
        
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
    

    elif course == 'PG' and dept == 'MCA':
       
        faculties_data = mca_dept.objects.all().order_by('image')
        achievements_data =mca_dept_achievements.objects.all()
        activities_data = mca_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = mca_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = mca_dept_major_equipments.objects.all()
        images = mca_dept_gallery.objects.all()
        timetable_data = mca_dept_timetable.objects.order_by('semester', 'section')
        events = mca_dept_events.objects.all()
        classrooms = mca_dept_classroom.objects.all()
        laboratory_facilities_gallary = mca_dept_laboratory_facilities_gallary.objects.all()

        print(laboratory_facilities_gallary)
        research_scholar_data = mca_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = mca_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = mca_dept_book_chapters.objects.all()
        publications_data = mca_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()
        
        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        accreditation_data = mca_dept_accreditation.objects.all().order_by('sno')
        
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
