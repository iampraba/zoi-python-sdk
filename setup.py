from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zoi-python-sdk',
    version='1.0.0',
    description='Zoho Office Integrator Python SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iampraba/zoi-python-sdk',
    author='Team - Zoho Office Integrator',
    author_email='support@zohoofficeintegrator.com',
    scripts=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'requests',
        'python-dateutil',
        'urllib3',
        'mysql-connector'
    ],
    keywords=['development', 'zoho', 'api', 'zohosdk', 'sdk', 'Zoho Office Integrator', 'Office Suite Editors', 'Document', 'Presentation', 'Spreadsheet'],
    packages=find_packages(),
    include_package_data=True
)
