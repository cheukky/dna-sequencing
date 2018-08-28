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
        res = dna_sequencing("CCC")
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

    def test_g(self):
        res = dna_sequencing("G")
        assert res["G"] == 1

    def test_gs(self):
        res = dna_sequencing("Ggg")
        assert res["G"] == 3

    def test_more_gs(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["G"] == 3

    def test_more_gs_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["G"] == 4

    def test_more_gs_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["G"] == 4

    def test_consec_g(self):
        res = dna_sequencing("G")
        assert res["Max consecutive Gs"] == 1

    def test_consec_gs(self):
        res = dna_sequencing("GgG")
        assert res["Max consecutive Gs"] == 3

    def test_more_consec_gs(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Max consecutive Gs"] == 1

    def test_more_consec_gs_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Max consecutive Gs"] == 4

    def test_more_consec_gs_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Max consecutive Gs"] == 4

    def test_percent_g(self):
        res = dna_sequencing("G")
        assert res["Percentage of Gs"] == 1.0

    def test_percent_gs(self):
        res = dna_sequencing("GgG")
        assert res["Percentage of Gs"] == 1.0

    def test_more_percent_gs(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Percentage of Gs"] == 0.25

    def test_more_percent_gs_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Percentage of Gs"] == 0.25

    def test_more_percent_gs_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Percentage of Gs"] == 0.2

    def test_t(self):
        res = dna_sequencing("T")
        assert res["T"] == 1

    def test_ts(self):
        res = dna_sequencing("TtT")
        assert res["T"] == 3

    def test_more_ts(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["T"] == 3

    def test_more_ts_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["T"] == 4

    def test_more_ts_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["T"] == 4

    def test_consec_t(self):
        res = dna_sequencing("T")
        assert res["Max consecutive Ts"] == 1

    def test_consec_ts(self):
        res = dna_sequencing("TtT")
        assert res["Max consecutive Ts"] == 3

    def test_more_consec_ts(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Max consecutive Ts"] == 1

    def test_more_consec_ts_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Max consecutive Ts"] == 4

    def test_more_consec_ts_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Max consecutive Ts"] == 4

    def test_percent_t(self):
        res = dna_sequencing("T")
        assert res["Percentage of Ts"] == 1.0

    def test_percent_ts(self):
        res = dna_sequencing("TtT")
        assert res["Percentage of Ts"] == 1.0

    def test_more_percent_ts(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Percentage of Ts"] == 0.25

    def test_more_percent_ts_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Percentage of Ts"] == 0.25

    def test_more_percent_ts_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Percentage of Ts"] == 0.2

    def test_other(self):
        res = dna_sequencing("H")
        assert res["Other"] == 1

    def test_others(self):
        res = dna_sequencing("fde")
        assert res["Other"] == 3

    def test_more_others(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Other"] == 0

    def test_more_others_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Other"] == 0

    def test_more_others_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Other"] == 4

    def test_percent_other(self):
        res = dna_sequencing("q")
        assert res["Percentage of other characters"] == 1.0

    def test_percent_others(self):
        res = dna_sequencing("qqq")
        assert res["Percentage of other characters"] == 1.0

    def test_more_percent_others(self):
        res = dna_sequencing("ACGTACGTACGT")
        assert res["Percentage of other characters"] == 0.0

    def test_more_percent_others_2(self):
        res = dna_sequencing("AAAACCCCGGGGTTTT")
        assert res["Percentage of other characters"] == 0.0

    def test_more_percent_others_3(self):
        res = dna_sequencing("AaaanCcccdGgggeTTtTf")
        assert res["Percentage of other characters"] == 0.2

    def test_integration(self):
        res = dna_sequencing('AAA')
        assert res == {'A': 3, 'C': 0, 'G': 0, 'Max consecutive As': 3,
                       'Max consecutive Cs': 0, 'Max consecutive Gs': 0,
                       'Max consecutive Ts': 0, 'Other': 0,
                       'Percentage of As': 1.0, 'Percentage of Cs': 0.0,
                       'Percentage of Gs': 0.0, 'Percentage of Ts': 0.0,
                       'Percentage of other characters': 0.0, 'T': 0}

    def test_integration_2(self):
        res = dna_sequencing('CCC')
        assert res == {'A': 0, 'C': 3, 'G': 0, 'Max consecutive As': 0,
                       'Max consecutive Cs': 3, 'Max consecutive Gs': 0,
                       'Max consecutive Ts': 0, 'Other': 0,
                       'Percentage of As': 0.0, 'Percentage of Cs': 1.0,
                       'Percentage of Gs': 0.0, 'Percentage of Ts': 0.0,
                       'Percentage of other characters': 0.0, 'T': 0}

    def test_integration_3(self):
        res = dna_sequencing('GGG')
        assert res == {'A': 0, 'C': 0, 'G': 3, 'Max consecutive As': 0,
                       'Max consecutive Cs': 0, 'Max consecutive Gs': 3,
                       'Max consecutive Ts': 0, 'Other': 0,
                       'Percentage of As': 0.0, 'Percentage of Cs': 0.0,
                       'Percentage of Gs': 1.0, 'Percentage of Ts': 0.0,
                       'Percentage of other characters': 0.0, 'T': 0}

    def test_integration_4(self):
        res = dna_sequencing('TTT')
        assert res == {'A': 0, 'C': 0, 'G': 0, 'Max consecutive As': 0,
                       'Max consecutive Cs': 0, 'Max consecutive Gs': 0,
                       'Max consecutive Ts': 3, 'Other': 0,
                       'Percentage of As': 0.0, 'Percentage of Cs': 0.0,
                       'Percentage of Gs': 0.0, 'Percentage of Ts': 1.0,
                       'Percentage of other characters': 0.0, 'T': 3}

    def test_integration_5(self):
        res = dna_sequencing('ACTGI')
        assert res == {'A': 1, 'C': 1, 'G': 1, 'Max consecutive As': 1,
                       'Max consecutive Cs': 1, 'Max consecutive Gs': 1,
                       'Max consecutive Ts': 1, 'Other': 1,
                       'Percentage of As': 0.2, 'Percentage of Cs': 0.2,
                       'Percentage of Gs': 0.2, 'Percentage of Ts': 0.2,
                       'Percentage of other characters': 0.2, 'T': 1}

    def test_integration_6(self):
        res = dna_sequencing('AaaCccTttGggIjk')
        assert res == {'A': 3, 'C': 3, 'G': 3, 'Max consecutive As': 3,
                       'Max consecutive Cs': 3, 'Max consecutive Gs': 3,
                       'Max consecutive Ts': 3, 'Other': 3,
                       'Percentage of As': 0.2, 'Percentage of Cs': 0.2,
                       'Percentage of Gs': 0.2, 'Percentage of Ts': 0.2,
                       'Percentage of other characters': 0.2, 'T': 3}

    def test_integration_7(self):
        res = dna_sequencing('ACTGIACTGIACTGI')
        assert res == {'A': 3, 'C': 3, 'G': 3, 'Max consecutive As': 1,
                       'Max consecutive Cs': 1, 'Max consecutive Gs': 1,
                       'Max consecutive Ts': 1, 'Other': 3,
                       'Percentage of As': 0.2, 'Percentage of Cs': 0.2,
                       'Percentage of Gs': 0.2, 'Percentage of Ts': 0.2,
                       'Percentage of other characters': 0.2, 'T': 3}
