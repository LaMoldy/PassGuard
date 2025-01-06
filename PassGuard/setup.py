from setuptools import setup, find_packages
from cx_Freeze import Executable

build_exe_options = {
    'packages': ['os', 'platform'],
    'includes': [],
    'include_files': ['assets'],
    'build_exe': '../build'
}

setup(
    name= 'PassGuard',
    version='0.0.1',
    author='Nikkolas "LaMoldy" Jackson',
    author_email='NikkolasJ@Outlook.com',
    description='A simple password manager that generates and saves passwords',
    long_description=open('../README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lamoldy/pass-guard',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License V3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.12',
    install_requires=[
        'bcrypt',
        'customtkinter',
        'cryptography',
    ],
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            'main.py',
            base='Win32GUI' if __import__('sys').platform == 'win32' else None,
            target_name='PassGuard.exe',
        )
    ]
)
