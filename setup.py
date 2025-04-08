from setuptools import setup, find_packages

setup(
    name='keypress-app',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pynput',
        # tkinter is included with Python, so it doesn't need to be listed here
    ],
    entry_points={
        'console_scripts': [
            'keypress-app=keypress:main',  # Adjust this if you have a main function
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple application to simulate pressing the F16 key every minute with a counter.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/keypress-app',  # Update with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update if using a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)