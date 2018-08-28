import pytest
from dna_sequencing import dna_sequencing


class TestClass(object):
    def test_empty(self):
        res = dna_sequencing('')
        assert res == {}
