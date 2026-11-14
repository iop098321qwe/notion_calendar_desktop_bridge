import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "install.py"
SPEC = importlib.util.spec_from_file_location("installer", SCRIPT)
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def test_install_and_update_use_the_same_path(self):
        with tempfile.TemporaryDirectory() as temporary:
            data = Path(temporary)
            destination = installer.install(data)
            source = SCRIPT.parent / "extension"
            for file in source.iterdir():
                self.assertEqual((destination / file.name).read_bytes(),
                                 file.read_bytes())
            (destination / "direct.js").write_text("outdated")
            self.assertEqual(installer.install(data), destination)
            self.assertEqual((destination / "direct.js").read_bytes(),
                             (source / "direct.js").read_bytes())
