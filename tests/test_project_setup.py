import os
import subprocess
import shutil

SCRIPT_PATH = os.path.join('scripts', 'project-setup.bat')
DIRECTORIES = ['src', 'docs', 'config', 'logs']  # directories script should create besides scripts/tests


def run_script():
    subprocess.check_call(['bash', SCRIPT_PATH])


def remove_dirs():
    for d in DIRECTORIES:
        if os.path.isdir(d):
            shutil.rmtree(d)


def test_script_creates_directories():
    remove_dirs()
    run_script()
    for d in ['src', 'scripts', 'docs', 'config', 'tests', 'logs']:
        assert os.path.isdir(d)


def test_requirements_file_exists():
    remove_dirs()
    if os.path.exists('requirements.txt'):
        os.remove('requirements.txt')
    run_script()
    assert os.path.isfile('requirements.txt')
    with open('requirements.txt') as f:
        content = f.read()
    assert 'pytest' in content
