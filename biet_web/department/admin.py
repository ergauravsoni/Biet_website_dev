from django.contrib import admin
from .models import civil_dept, mechanical_dept, biotechnology_dept, chemical_dept, chemistry_dept
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
from .models import computer_science_dept_book_chapters, computer_science_dept_publications
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

admin.site.site_header = "BIET Website Administration"

# Register your models here.
admin.site.register(civil_dept)
admin.site.register(mechanical_dept)
admin.site.register(biotechnology_dept)
admin.site.register(chemical_dept)
admin.site.register(chemistry_dept)
admin.site.register(computer_science_dept)
admin.site.register(electronics_and_communication_dept)
admin.site.register(electrical_and_electronics_dept)
admin.site.register(information_science_dept)
admin.site.register(mathematics_dept)
admin.site.register(physics_dept)
admin.site.register(textile_dept)
admin.site.register(mca_dept)
admin.site.register(environmental_dept)
admin.site.register(civil_depatment_gallery)
admin.site.register(mechanical_dept_gallery)
admin.site.register(biotechnology_dept_gallery)
admin.site.register(chemical_dept_gallery)
admin.site.register(chemistry_dept_gallery)
admin.site.register(computer_science_dept_gallery)
admin.site.register(electronics_and_communication_gallery)
admin.site.register(electrical_and_electronics_gallery)
admin.site.register(information_science_dept_gallery)
admin.site.register(mathematics_dept_gallery)
admin.site.register(physics_dept_gallery)
admin.site.register(textile_dept_gallery)
admin.site.register(mca_dept_gallery)
admin.site.register(environmental_dept_gallery)
admin.site.register(computer_science_dept_lab_facilities)
admin.site.register(computer_science_dept_major_equipments)
admin.site.register(computer_science_dept_activities)
admin.site.register(computer_science_dept_achievements)
admin.site.register(computer_science_dept_timetable)
admin.site.register(computer_science_dept_events)
admin.site.register(computer_science_dept_classroom)
admin.site.register(computer_science_dept_research_scholars)
admin.site.register(computer_science_dept_research_guide)
admin.site.register(computer_science_dept_laboratory_facilities_gallary)
admin.site.register(computer_science_dept_publications)
admin.site.register(computer_science_dept_book_chapters)
admin.site.register(civil_dept_lab_facilities)
admin.site.register(civil_dept_major_equipments)
admin.site.register(civil_dept_activities)
admin.site.register(civil_dept_achievements)
admin.site.register(civil_dept_timetable)
admin.site.register(civil_dept_events)
admin.site.register(civil_dept_classroom)
admin.site.register(civil_dept_research_scholars)
admin.site.register(civil_dept_research_guide)
admin.site.register(civil_dept_laboratory_facilities_gallary)
admin.site.register(civil_dept_publications)
admin.site.register(civil_dept_book_chapters)
admin.site.register(mechanical_dept_lab_facilities)
admin.site.register(mechanical_dept_major_equipments)
admin.site.register(mechanical_dept_activities)
admin.site.register(mechanical_dept_achievements)
admin.site.register(mechanical_dept_timetable)
admin.site.register(mechanical_dept_events)
admin.site.register(mechanical_dept_classroom)
admin.site.register(mechanical_dept_research_scholars)
admin.site.register(mechanical_dept_research_guide)
admin.site.register(mechanical_dept_laboratory_facilities_gallary)
admin.site.register(mechanical_dept_publications)
admin.site.register(mechanical_dept_book_chapters)
admin.site.register(physics_dept_lab_facilities)
admin.site.register(physics_dept_major_equipments)
admin.site.register(physics_dept_activities)
admin.site.register(physics_dept_achievements)
admin.site.register(physics_dept_timetable)
admin.site.register(physics_dept_events)
admin.site.register(physics_dept_classroom)
admin.site.register(physics_dept_research_scholars)
admin.site.register(physics_dept_research_guide)
admin.site.register(physics_dept_laboratory_facilities_gallary)
admin.site.register(physics_dept_publications)
admin.site.register(physics_dept_book_chapters)
admin.site.register(chemistry_dept_lab_facilities)
admin.site.register(chemistry_dept_major_equipments)
admin.site.register(chemistry_dept_activities)
admin.site.register(chemistry_dept_achievements)
admin.site.register(chemistry_dept_timetable)
admin.site.register(chemistry_dept_events)
admin.site.register(chemistry_dept_classroom)
admin.site.register(chemistry_dept_research_scholars)
admin.site.register(chemistry_dept_research_guide)
admin.site.register(chemistry_dept_laboratory_facilities_gallary)
admin.site.register(chemistry_dept_publications)
admin.site.register(chemistry_dept_book_chapters)
admin.site.register(mathematics_dept_lab_facilities)
admin.site.register(mathematics_dept_major_equipments)
admin.site.register(mathematics_dept_activities)
admin.site.register(mathematics_dept_achievements)
admin.site.register(mathematics_dept_timetable)
admin.site.register(mathematics_dept_events)
admin.site.register(mathematics_dept_classroom)
admin.site.register(mathematics_dept_research_scholars)
admin.site.register(mathematics_dept_research_guide)
admin.site.register(mathematics_dept_laboratory_facilities_gallary)
admin.site.register(mathematics_dept_publications)
admin.site.register(mathematics_dept_book_chapters)