import pytest

from Counting_DNA_Nucleotides.main import count_dna_nucleotides


@pytest.mark.parametrize("nucleotide_seq, expected_output", [
    ("AAA", "3 0 0 0"),
    ("CCC", "0 3 0 0"),
    ("GGG", "0 0 3 0"),
    ("TTT", "0 0 0 3"),
    ("ACGT", "1 1 1 1"),
    ("ACCGGGTTTT", "1 2 3 4"),
    ("ACAGGTACT", "3 2 2 2"),
    ("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC", "20 12 17 21"),
])
def test_count_number_of_nucleotides(nucleotide_seq, expected_output):
    assert count_dna_nucleotides(nucleotide_seq) == expected_output
