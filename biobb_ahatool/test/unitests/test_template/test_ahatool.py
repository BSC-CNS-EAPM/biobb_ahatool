from biobb_common.tools import test_fixtures as fx
from biobb_ahatool.ahatool.ahatool import ahatool

class TestAhatool():
    def setup_class(self):
        fx.test_setup(self, 'ahatool')

    def teardown_class(self):
        fx.test_teardown(self)
        pass
    def test_ahatool(self):
        returncode= ahatool(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_file_path'])
        assert fx.equal(self.paths['output_file_path'], self.paths['ref_output_file_path'])
        assert fx.exe_success(returncode)
