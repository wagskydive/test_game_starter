import os
import unittest

class TestSetupScript(unittest.TestCase):
    SCRIPT_PATH = os.path.join('scripts', 'setup.bat')

    def test_script_exists(self):
        self.assertTrue(os.path.isfile(self.SCRIPT_PATH), f"{self.SCRIPT_PATH} does not exist")

    def test_contains_venv_creation(self):
        with open(self.SCRIPT_PATH) as f:
            content = f.read().lower()
        self.assertIn('python -m venv venv', content)

    def test_creates_directories(self):
        with open(self.SCRIPT_PATH) as f:
            content = f.read().lower()
        for d in ['src', 'scripts', 'docs', 'config']:
            self.assertIn(d, content, f"{d} directory creation not found")

    def test_installs_requirements(self):
        with open(self.SCRIPT_PATH) as f:
            content = f.read().lower()
        self.assertIn('pip install -r requirements.txt', content)

if __name__ == '__main__':
    unittest.main()
