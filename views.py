from datetime import date

from simba_framework.templator import render
from patterns.сreational_patterns import Engine, Logger

site = Engine()
logger = Logger('main')


# Main page controller
class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


# Content controller
class Content:
    def __call__(self, request):
        return '200 OK', render('content.html', date=request.get('date', None))


# Contacts controller
class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html', date=request.get('date', None))


# About controller
class About:
    # {'method': 'GET', 'request_params': {'id': '1', 'category': '10'}}
    def __call__(self, request):
        return '200 OK', render('about.html', date=request.get('date', None))


# Schedule controller
class StudyPrograms:
    def __call__(self, request):
        return '200 OK', render('study-programs.html', date=date.today())


# 404 controller
class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


# Courses list controller
class CoursesList:
    def __call__(self, request):
        logger.log('Courses list')
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return '200 OK', render('course_list.html',
                                    objects_list=category.courses,
                                    name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


# Create course controller
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

            return '200 OK', render('course_list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create_course.html',
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


# контроллер - создать категорию
class CreateCategory:
    def __call__(self, request):

        if request['method'] == 'POST':
            # метод пост

            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html',
                                    categories=categories)


# контроллер - список категорий
class CategoryList:
    def __call__(self, request):
        logger.log('Categories list')
        return '200 OK', render('category_list.html',
                                objects_list=site.categories)


# контроллер - копировать курс
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

            return '200 OK', render('course_list.html',
                                    objects_list=site.courses,
                                    name=new_course.category.name)
        except KeyError:
            return '200 OK', 'No courses have been added yet'
