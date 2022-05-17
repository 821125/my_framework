from jinja2 import Template
from os.path import join


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: template name
    :param folder: templates folder
    :param kwargs: parameters
    :return:
    """
    file_path = join(folder, template_name)
    # Open template by name
    with open(file_path, encoding='utf-8') as f:
        # Read
        template = Template(f.read())
    # Rendering template with parameters
    return template.render(**kwargs)
