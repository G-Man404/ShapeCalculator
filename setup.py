from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='Shape calculator',
  version='1.0.0',
  author='GMan',
  author_email='anisimovf94@gmail.com',
  description='The Shape Calculator is a Python class designed to simplify geometric calculations such as calculating '
              'the area of a circle and a triangle, as well as checking if a triangle is right-angled.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/G-Man404/ShapeCalculator',
  packages=find_packages(),
  install_requires=[''],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='shapecalculator shape calculator',
  project_urls={
    'GitHub': 'https://github.com/G-Man404/ShapeCalculator'
  },
  python_requires='>=3.11'
)