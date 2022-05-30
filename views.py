from datetime import date

from simba_framework.templator import render
from patterns.сreational_patterns import Engine, Logger
from patterns.structural_patterns import AppRoute, Debug

site = Engine()
logger = Logger('main')

routes = {}


# Controller - Main page
@AppRoute(routes=routes, url='/')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)


# Controller - Content
@AppRoute(routes=routes, url='/content/')
class Content:
    @Debug(name='Content')
    def __call__(self, request):
        return '200 OK', render('content.html')


# Controller - Contacts
@AppRoute(routes=routes, url='/contacts/')
class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html')


# Controller - About
@AppRoute(routes=routes, url='/about/')
class About:
    @Debug(name='About')
    def __call__(self, request):
        return '200 OK', render('about.html')


# Controller - Schedule
@AppRoute(routes=routes, url='/study-programs/')
class StudyPrograms:
    @Debug(name='StudyPrograms')
    def __call__(self, request):
        return '200 OK', render('study-programs.html', data=date.today())


# Controller - 404
class NotFound404:
    @Debug(name='NotFound404')
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


# Controller - Courses list
@AppRoute(routes=routes, url='/courses-list/')
class CoursesList:
    def __call__(self, request):
        logger.log('Courses list')
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return '200 OK', render('courses-list.html',
                                    objects_list=category.courses,
                                    name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


# Controller - Create course
@AppRoute(routes=routes, url='/create-course/')
class CreateCourse:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render('courses-list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create-course.html',
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


# Controller - Create category
@AppRoute(routes=routes, url='/create-category/')
class CreateCategory:
    def __call__(self, request):

        if request['method'] == 'POST':
            # Method - POST

            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render('content.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create-category.html',
                                    categories=categories)


# Controller - Category list
@AppRoute(routes=routes, url='/category-list/')
class CategoryList:
    def __call__(self, request):
        logger.log('Category list')
        return '200 OK', render('category-list.html',
                                objects_list=site.categories)


@AppRoute(routes=routes, url='/copy-course/')
# Controller - Copy course
class CopyCourse:
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']

            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', render('courses-list.html',
                                    objects_list=site.courses,
                                    name=new_course.category.name)
        except KeyError:
            return '200 OK', 'No courses have been added yet'
