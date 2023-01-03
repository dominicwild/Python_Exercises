import pytest

from Counting_DNA_Nucleotides.main import count_dna_nucleotides


@pytest.mark.parametrize("nucleotide_seq, expected_output", [
    ("AAA", "3 0 0 0"),
])
def test_count_number_of_nucleotides(nucleotide_seq, expected_output):
    assert count_dna_nucleotides(nucleotide_seq) == expected_output
