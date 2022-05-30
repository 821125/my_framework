from datetime import date
# from views import Index, Content, Contacts, About, StudyPrograms, CoursesList, CreateCourse, \
#     CreateCategory, CategoryList, CopyCourse


# Front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

# routes = {
#     '/': Index(),
#     '/content/': Content(),
#     '/study-programs/': StudyPrograms(),
#     '/courses-list/': CoursesList(),
#     '/create-course/': CreateCourse(),
#     '/create-category/': CreateCategory(),
#     '/category-list/': CategoryList(),
#     '/copy-course/': CopyCourse(),
#     '/contacts/': Contacts(),
#     '/about/': About()
# }
