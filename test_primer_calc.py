from primer_calc import *

# Testing Primer class initialization
def test_normal_primer_init_str():
    primer = Primer('Test', 'aaacccgggttt')
    assert primer.name == 'Test'
    assert primer.sequence == 'aaacccgggttt'

def test_abnormal_primer_init():
    primer = Primer('Test Primer', 'qewropiuqerattdfcgckljaaaafd')
    assert primer.name == 'Test Primer'
    assert primer.sequence == 'attcgcaaaa'

    primer = Primer('test numbers', 123456)
    assert primer.name == 'test numbers'
    assert primer.sequence == 'Invalid sequence entered'

    primer = Primer('Test letter case', 'aAacCcgGgtTt')
    assert primer.sequence == 'aaacccgggttt'

def test_primer_calc(capsys):
    primer = Primer('test', 'acgtacgtacgt')
    # run calculations and assign values of results
    primer.calc_all()
    # tests
    assert primer.trip_upper == 'ACG-TAC-GTA-CGT-'
    assert primer.mw == 3643.44
    assert primer.gc == 50.0
    assert primer.std_tm == 36
    assert primer.__len__() == 12
    assert primer.__str__() == "test: 5'-ACG-TAC-GTA-CGT-3'"

def test_primer_printout(capsys):
    primer = Primer('test', 'acgtacgtacgt')
    # run calculations and assign values of results
    primer.calc_all()

    # sysout testing
    primer.print_mw()
    out, err = capsys.readouterr()
    assert out == "3643.44 daltons (g/M)\n"

    primer.print_gc()
    out, err = capsys.readouterr()
    assert out == "50.0 % GC\n"

