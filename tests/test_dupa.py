import os
import unittest

from unittest.mock import patch, MagicMock
from tests.conftest import template_variables

from click.testing import CliRunner
from hypothesis import given

from dupa.cli import main as ClickApp
from dupa.dupa import Variable


def read(f):
    with open(f) as fo:
        return fo.read()


class TestVariable(unittest.TestCase):
    """Test Variable object."""

    @given(template_variables())
    def test_message(self, variables):
        """Test for message formatting

        GIVEN variable name is 'text_text'
        WHEN Variable object is initiated with such string
        THEN Variable.message will contain string 'text text'
        """
        assert Variable(variables[0]).message == variables[1]

    @given(variables=template_variables())
    def test_read(self, variables):
        """Test read function
        """

        mock = MagicMock(return_value=variables[1].strip())
        with patch('builtins.input', mock):
            assert Variable(variables[0]).read() == variables[1].strip()


class TestProcessingFunctions(unittest.TestCase):
    template = "{{Example_Value}} is {{Another_Value}}"
    not_a_template = "Example_Value is Another_Value"
    template_output = "Example Value is Another Value"

    def test_extract_variables(self):
        from dupa.dupa import extract_variables

        value_bag = extract_variables(self.template)

        assert len(value_bag) == 2
        assert 'Example_Value' in value_bag

    def test_context(self):
        from dupa.dupa import context

        def new_read(s): return s.message

        with patch('dupa.dupa.Variable.read', new_read):
            ctx = context(self.template)

            assert len(ctx) == 2
            assert ctx['Example_Value'] == 'Example Value'

    def test_main_function(self):
        """Test main_function"""
        from dupa.dupa import main_function

        def new_read(s): return s.message

        with patch('dupa.dupa.Variable.read', new_read):

            mock = MagicMock(return_value=self.template)
            with patch('dupa.dupa.load', mock):

                output = main_function('not_important_in_this_test')
                assert output == self.template_output

            mock = MagicMock(return_value=self.not_a_template)
            with patch('dupa.dupa.load', mock):
                output = main_function('not_important_in_this_test')
                assert output == self.not_a_template

    def test_e2e(self):
        """Make final e2e tests"""
        import tempfile

        sample_input = "Value 1\nValue 2\n".encode()

        paczek = tempfile.NamedTemporaryFile(mode='w', delete=False)
        paczek.write(self.template)
        paczek.close()

        filled_paczek = '/tmp/paczek1'

        # test the happy path
        runner = CliRunner()
        result = runner.invoke(
            ClickApp, [paczek.name, filled_paczek], input=sample_input)

        assert result.exit_code == 0
        assert os.path.exists(filled_paczek)
        assert "1" in read(filled_paczek)
        assert "2" in read(filled_paczek)

        # lets check the first bad path
        result = runner.invoke(ClickApp, [paczek.name])
        assert result.exit_code == 2
        assert "Missing argument 'OUTPUT_FILE'" in result.output

        os.unlink(filled_paczek)
        os.unlink(paczek.name)

        # lets start push jibberish
        result = runner.invoke(ClickApp, ['nothing'])
        assert result.exit_code == 2
        assert "Missing argument 'OUTPUT_FILE'" in result.output

        filled_paczek = "/tmp/another"
        result = runner.invoke(ClickApp, ['nothing', filled_paczek])
        assert result.exit_code == 1
        assert "Error loading template file" in result.output

        if os.path.exists(filled_paczek):
            os.unlink(filled_paczek)
