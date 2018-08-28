from dna_sequencing import dna_sequencing


class TestClass(object):
    def test_empty(self):
        res = dna_sequencing('')
        assert res == {'A': 0, 'C': 0, 'G': 0, 'Max consecutive As': 0,
                       'Max consecutive Cs': 0, 'Max consecutive Gs': 0,
                       'Max consecutive Ts': 0, 'Other': 0,
                       'Percentage of As': 0.0, 'Percentage of Cs': 0.0,
                       'Percentage of Gs': 0.0, 'Percentage of Ts': 0.0,
                       'Percentage of other characters': 0.0, 'T': 0}

    def test_a(self):
        res = dna_sequencing("A")
        assert res["A"] == 1

    def test_as(self):
        res = dna_sequencing("AAA")
        assert res["A"] == 3

    def test_more_as(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["A"] == 3

    def test_more_as_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["A"] == 4

    def test_more_as_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["A"] == 4

    def test_consec_a(self):
        res = dna_sequencing("A")
        assert res["Max consecutive As"] == 1

    def test_consec_as(self):
        res = dna_sequencing("AAA")
        assert res["Max consecutive As"] == 3

    def test_more_consec_as(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Max consecutive As"] == 1

    def test_more_consec_as_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Max consecutive As"] == 4

    def test_more_consec_as_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Max consecutive As"] == 4

    def test_percent_a(self):
        res = dna_sequencing("A")
        assert res["Percentage of As"] == 1.0

    def test_percent_as(self):
        res = dna_sequencing("AAA")
        assert res["Percentage of As"] == 1.0

    def test_more_percent_as(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Percentage of As"] == 0.25

    def test_more_percent_as_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Percentage of As"] == 0.25

    def test_more_percent_as_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Percentage of As"] == 0.2

    def test_c(self):
        res = dna_sequencing("C")
        assert res["C"] == 1

    def test_cs(self):
        res = dna_sequencing("CCC")
        assert res["C"] == 3

    def test_more_cs(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["C"] == 3

    def test_more_cs_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["C"] == 4

    def test_more_cs_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["C"] == 4

    def test_consec_c(self):
        res = dna_sequencing("C")
        assert res["Max consecutive Cs"] == 1

    def test_consec_cs(self):
        res = dna_sequencing("AAA")
        assert res["Max consecutive Cs"] == 3

    def test_more_consec_cs(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Max consecutive Cs"] == 1

    def test_more_consec_cs_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Max consecutive Cs"] == 4

    def test_more_consec_cs_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Max consecutive Cs"] == 4

    def test_percent_c(self):
        res = dna_sequencing("C")
        assert res["Percentage of Cs"] == 1.0

    def test_percent_cs(self):
        res = dna_sequencing("CCC")
        assert res["Percentage of Cs"] == 1.0

    def test_more_percent_cs(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Percentage of Cs"] == 0.25

    def test_more_percent_cs_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Percentage of Cs"] == 0.25

    def test_more_percent_cs_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Percentage of Cs"] == 0.2
