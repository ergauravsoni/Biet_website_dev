from django.shortcuts import render
from .models import *
# Create your views here.

def home(request, course, dept):
    print(dept)
    # print(dept)

    if course == 'UG' and dept == 'CV':

        faculties_data = civil_dept.objects.all().order_by('sno')
        achievements_data = civil_dept_achievements.objects.all()
        activities_data = civil_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = civil_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = civil_dept_major_equipments.objects.all()
        images = civil_dept_gallery.objects.all()
        timetable_data = civil_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = civil_dept_learning_materials.objects.all().order_by('semester', 'subject')

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

        grants_patents_data = civil_dept_grants_and_patents.objects.all()
        accreditation_data = civil_dept_accreditation.objects.all().order_by('sno')
        alumni_data = civil_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'ME':

        faculties_data = mechanical_dept.objects.all().order_by('sno')
        achievements_data = mechanical_dept_achievements.objects.all()
        activities_data = mechanical_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = mechanical_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = mechanical_dept_major_equipments.objects.all()
        images = mechanical_dept_gallery.objects.all()
        timetable_data = mechanical_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = mechanical_dept_learning_materials.objects.all().order_by('semester', 'subject')

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

        grants_patents_data = mechanical_dept_grants_and_patents.objects.all()
        accreditation_data = mechanical_dept_accreditation.objects.all().order_by('sno')
        alumni_data = mechanical_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'EE':

        faculties_data = electrical_and_electronics_dept.objects.all().order_by('sno')
        achievements_data = electrical_and_electronics_dept_achievements.objects.all()
        activities_data = electrical_and_electronics_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = electrical_and_electronics_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = electrical_and_electronics_dept_major_equipments.objects.all()
        images = electrical_and_electronics_dept_gallery.objects.all()
        timetable_data = electrical_and_electronics_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = electrical_and_electronics_dept_learning_materials.objects.all().order_by('semester', 'subject')

        events = electrical_and_electronics_dept_events.objects.all()
        classrooms = electrical_and_electronics_dept_classroom.objects.all()
        laboratory_facilities_gallary = electrical_and_electronics_dept_laboratory_facilities_gallary.objects.all()

        research_scholar_data = electrical_and_electronics_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = electrical_and_electronics_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = electrical_and_electronics_dept_book_chapters.objects.all()
        publications_data = electrical_and_electronics_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()

        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        grants_patents_data = electrical_and_electronics_dept_grants_and_patents.objects.all()
        accreditation_data = electrical_and_electronics_dept_accreditation.objects.all().order_by('sno')
        alumni_data = electrical_and_electronics_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'EC':

        faculties_data = electronics_and_communication_dept.objects.all().order_by('sno')
        achievements_data = electronics_and_communication_dept_achievements.objects.all()
        activities_data = electronics_and_communication_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = electronics_and_communication_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = electronics_and_communication_dept_major_equipments.objects.all()
        images = electronics_and_communication_dept_gallery.objects.all()
        timetable_data = electronics_and_communication_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = electronics_and_communication_dept_learning_materials.objects.all().order_by('semester', 'subject')

        events = electronics_and_communication_dept_events.objects.all()
        classrooms = electronics_and_communication_dept_classroom.objects.all()
        laboratory_facilities_gallary = electronics_and_communication_dept_laboratory_facilities_gallary.objects.all()

        research_scholar_data = electronics_and_communication_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = electronics_and_communication_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = electronics_and_communication_dept_book_chapters.objects.all()
        publications_data = electronics_and_communication_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()

        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        grants_patents_data = electronics_and_communication_dept_grants_and_patents.objects.all()
        accreditation_data = electronics_and_communication_dept_accreditation.objects.all().order_by('sno')
        alumni_data = electronics_and_communication_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'CH':

        faculties_data = chemical_dept.objects.all().order_by('sno')
        achievements_data = chemical_dept_achievements.objects.all()
        activities_data = chemical_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = chemical_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = chemical_dept_major_equipments.objects.all()
        images = chemical_dept_gallery.objects.all()
        timetable_data = chemical_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = chemical_dept_learning_materials.objects.all().order_by('semester', 'subject')

        events = chemical_dept_events.objects.all()
        classrooms = chemical_dept_classroom.objects.all()
        laboratory_facilities_gallary = chemical_dept_laboratory_facilities_gallary.objects.all()

        research_scholar_data = chemical_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = chemical_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = chemical_dept_book_chapters.objects.all()
        publications_data = chemical_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()

        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        grants_patents_data = chemical_dept_grants_and_patents.objects.all()
        accreditation_data = chemical_dept_accreditation.objects.all().order_by('sno')
        alumni_data = chemical_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'EI':

        faculties_data = electronics_and_instrumentation_dept.objects.all().order_by('sno')
        achievements_data = electronics_and_instrumentation_dept_achievements.objects.all()
        activities_data = electronics_and_instrumentation_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = electronics_and_instrumentation_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = electronics_and_instrumentation_dept_major_equipments.objects.all()
        images = electronics_and_instrumentation_dept_gallery.objects.all()
        timetable_data = electronics_and_instrumentation_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = electronics_and_instrumentation_dept_learning_materials.objects.all().order_by('semester', 'subject')

        events = electronics_and_instrumentation_dept_events.objects.all()
        classrooms = electronics_and_instrumentation_dept_classroom.objects.all()
        laboratory_facilities_gallary = electronics_and_instrumentation_dept_laboratory_facilities_gallary.objects.all()

        research_scholar_data = electronics_and_instrumentation_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = electronics_and_instrumentation_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = electronics_and_instrumentation_dept_book_chapters.objects.all()
        publications_data = electronics_and_instrumentation_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()

        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        grants_patents_data = electronics_and_instrumentation_dept_grants_and_patents.objects.all()
        accreditation_data = electronics_and_instrumentation_dept_accreditation.objects.all().order_by('sno')
        alumni_data = electronics_and_instrumentation_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'CS':

        faculties_data = computer_science_dept.objects.all().order_by('sno')
        achievements_data = computer_science_dept_achievements.objects.all()
        activities_data = computer_science_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = computer_science_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = computer_science_dept_major_equipments.objects.all()
        images = computer_science_dept_gallery.objects.all()
        timetable_data = computer_science_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = computer_science_dept_learning_materials.objects.all().order_by('semester', 'subject')

        events = computer_science_dept_events.objects.all()
        classrooms = computer_science_dept_classroom.objects.all()
        laboratory_facilities_gallary = computer_science_dept_laboratory_facilities_gallary.objects.all()

        research_scholar_data = computer_science_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = computer_science_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = computer_science_dept_book_chapters.objects.all()
        publications_data = computer_science_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()

        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        grants_patents_data = computer_science_dept_grants_and_patents.objects.all()
        accreditation_data = computer_science_dept_accreditation.objects.all().order_by('sno')
        alumni_data = computer_science_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'IS':

        faculties_data = information_science_dept.objects.all().order_by('sno')
        achievements_data = information_science_dept_achievements.objects.all()
        activities_data = information_science_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = information_science_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = information_science_dept_major_equipments.objects.all()
        images = information_science_dept_gallery.objects.all()
        timetable_data = information_science_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = information_science_dept_learning_materials.objects.all().order_by('semester', 'subject')

        events = information_science_dept_events.objects.all()
        classrooms = information_science_dept_classroom.objects.all()
        laboratory_facilities_gallary = information_science_dept_laboratory_facilities_gallary.objects.all()

        research_scholar_data = information_science_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = information_science_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = information_science_dept_book_chapters.objects.all()
        publications_data = information_science_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()

        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        grants_patents_data = information_science_dept_grants_and_patents.objects.all()
        accreditation_data = information_science_dept_accreditation.objects.all().order_by('sno')
        alumni_data = information_science_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'TX':

        faculties_data = textile_technology_dept.objects.all().order_by('sno')
        achievements_data = textile_technology_dept_achievements.objects.all()
        activities_data = textile_technology_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = textile_technology_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = textile_technology_dept_major_equipments.objects.all()
        images = textile_technology_dept_gallery.objects.all()
        timetable_data = textile_technology_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = textile_technology_dept_learning_materials.objects.all().order_by('semester', 'subject')

        events = textile_technology_dept_events.objects.all()
        classrooms = textile_technology_dept_classroom.objects.all()
        laboratory_facilities_gallary = textile_technology_dept_laboratory_facilities_gallary.objects.all()

        research_scholar_data = textile_technology_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = textile_technology_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = textile_technology_dept_book_chapters.objects.all()
        publications_data = textile_technology_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()

        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        grants_patents_data = textile_technology_dept_grants_and_patents.objects.all()
        accreditation_data = textile_technology_dept_accreditation.objects.all().order_by('sno')
        alumni_data = textile_technology_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'BT':

        faculties_data = bio_technology_dept.objects.all().order_by('sno')
        achievements_data = bio_technology_dept_achievements.objects.all()
        activities_data = bio_technology_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = bio_technology_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = bio_technology_dept_major_equipments.objects.all()
        images = bio_technology_dept_gallery.objects.all()
        timetable_data = bio_technology_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = bio_technology_dept_learning_materials.objects.all().order_by('semester', 'subject')

        events = bio_technology_dept_events.objects.all()
        classrooms = bio_technology_dept_classroom.objects.all()
        laboratory_facilities_gallary = bio_technology_dept_laboratory_facilities_gallary.objects.all()

        research_scholar_data = bio_technology_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = bio_technology_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = bio_technology_dept_book_chapters.objects.all()
        publications_data = bio_technology_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()

        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        grants_patents_data = bio_technology_dept_grants_and_patents.objects.all()
        accreditation_data = bio_technology_dept_accreditation.objects.all().order_by('sno')
        alumni_data = bio_technology_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'PHY':

        faculties_data = physics_dept.objects.all().order_by('sno')
        achievements_data = physics_dept_achievements.objects.all()
        activities_data = physics_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = physics_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = physics_dept_major_equipments.objects.all()
        images = physics_dept_gallery.objects.all()
        timetable_data = physics_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = physics_dept_learning_materials.objects.all().order_by('semester', 'subject')

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

        grants_patents_data = physics_dept_grants_and_patents.objects.all()
        accreditation_data = physics_dept_accreditation.objects.all().order_by('sno')

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'CHE':

        faculties_data = chemistry_dept.objects.all().order_by('sno')
        achievements_data = chemistry_dept_achievements.objects.all()
        activities_data = chemistry_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = chemistry_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = chemistry_dept_major_equipments.objects.all()
        images = chemistry_dept_gallery.objects.all()
        timetable_data = chemistry_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = chemistry_dept_learning_materials.objects.all().order_by('semester', 'subject')

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

        grants_patents_data = chemistry_dept_grants_and_patents.objects.all()
        accreditation_data = chemistry_dept_accreditation.objects.all().order_by('sno')

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'MAT':

        faculties_data = mathematics_dept.objects.all().order_by('sno')
        achievements_data = mathematics_dept_achievements.objects.all()
        activities_data = mathematics_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = mathematics_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = mathematics_dept_major_equipments.objects.all()
        images = mathematics_dept_gallery.objects.all()
        timetable_data = mathematics_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = mathematics_dept_learning_materials.objects.all().order_by('semester', 'subject')

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

        grants_patents_data = mathematics_dept_grants_and_patents.objects.all()
        accreditation_data = mathematics_dept_accreditation.objects.all().order_by('sno')

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'learning_materials_data': learning_materials_data
                }

    elif course == 'UG' and dept == 'BM':

        faculties_data = bio_medical_dept.objects.all().order_by('sno')
        achievements_data = bio_medical_dept_achievements.objects.all()
        activities_data = bio_medical_dept_activities.objects.all().order_by('sno')
        lab_facilities_data = bio_medical_dept_lab_facilities.objects.all().order_by('sno')
        major_equipments_data = bio_medical_dept_major_equipments.objects.all()
        images = bio_medical_dept_gallery.objects.all()
        timetable_data = bio_medical_dept_timetable.objects.order_by('semester', 'section')
        learning_materials_data = bio_medical_dept_learning_materials.objects.all().order_by('semester', 'subject')

        events = bio_medical_dept_events.objects.all()
        classrooms = bio_medical_dept_classroom.objects.all()
        laboratory_facilities_gallary = bio_medical_dept_laboratory_facilities_gallary.objects.all()

        research_scholar_data = bio_medical_dept_research_scholars.objects.all().order_by('guide')
        research_guide_data = bio_medical_dept_research_guide.objects.all().order_by('sno')

        book_chapters_data = bio_medical_dept_book_chapters.objects.all()
        publications_data = bio_medical_dept_publications.objects.all()
        research_data = []
        guide_count = research_guide_data.count()

        for i in range(guide_count):
            research_data.append(research_scholar_data.filter(guide_id=i+1))

        grants_patents_data = bio_medical_dept_grants_and_patents.objects.all()
        accreditation_data = bio_medical_dept_accreditation.objects.all().order_by('sno')
        alumni_data = bio_medical_dept_alumni.objects.all()

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
                    'grants_patents_data': grants_patents_data,
                    'accreditation_data': accreditation_data,
                    'alumni_data': alumni_data,
                    'learning_materials_data': learning_materials_data
                }


    return render(request, 'department/'+course+'/' + dept + '/home.html', content)
