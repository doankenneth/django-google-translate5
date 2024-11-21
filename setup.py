from setuptools import setup

setup(
    name='django-google-translate5',
    package_data={'google_translate_django5': ['templates/translate.html']},
    packages=['google_translate_django5', 'google_translate_django5/templatetags'],
    version='1.0',
    description='A Python Package to include a Google Translate Drop Down in Django Projects',
    author='Kenneth Doan',
)