"""Regression for relative output paths in the genuine network runner."""
from pathlib import Path
import os
import tempfile
import unittest
from unittest.mock import patch
import live_real_research_case as live


class LiveRunnerPathTests(unittest.TestCase):
    def test_relative_output_is_resolved_before_download(self):
        with tempfile.TemporaryDirectory() as directory:
            previous = Path.cwd()
            try:
                os.chdir(directory)
                with patch.object(live.fetch, 'download_scifact', side_effect=RuntimeError('stop before network')) as download:
                    with self.assertRaisesRegex(RuntimeError, 'stop before network'):
                        live.run_online('relative-output')
                    download.assert_called_once_with(Path(directory).resolve() / 'relative-output' / 'scifact')
                    self.assertTrue((Path(directory) / 'relative-output').is_dir())
            finally:
                os.chdir(previous)
