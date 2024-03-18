from setuptools import setup, find_packages

setup(
    name='Geva',
    version='1.0.2',
    author='yangjinbao',
    author_email='ruoyu1123@outlook.com',
    description='A genomic assement tools including Completeness and Accuracy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/panlab-bioinfo/Geva.git',
    packages=find_packages(),
    scripts=['geva.py'],
    python_requires='>=3.7',
    install_requires=[
        'pandas',
        # Add any other dependencies here
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

