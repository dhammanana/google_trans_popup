from setuptools import setup, find_packages

setup(
    name='google_trans_popup',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pynput==1.7.7',
        'pyperclip==1.9.0',
        'requests==2.32.3'
    ],
    entry_points={
        'console_scripts': [
            'googletrans = google_trans_popup.google_trans:main',  # Command line entry point
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

