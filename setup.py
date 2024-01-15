from setuptools import setup, find_namespace_packages

setup(
    name='Personal Assistant',
    version='1',
    description='The "Personal Assistant" bot is designed to assist users in managing their contacts, notes, and files through a natural language interface. The bot leverages advanced functionalities to understand user input and provide relevant suggestions based on context.',
    url='https://github.com/ArleKinG44/GOIT_Projekt_group_3',
    author='Hufflepuff',
    packages=find_namespace_packages(),
    install_requires=['prompt_toolkit', 'pygments',],
    entry_points={'console_scripts': ['my_command = main:main']}
)