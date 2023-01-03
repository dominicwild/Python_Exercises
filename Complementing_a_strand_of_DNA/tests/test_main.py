import pytest

from Complementing_a_strand_of_DNA.main import reverse_complement_dna


@pytest.mark.parametrize("dna_seq, expected_output", [
    ("A", "T"),
    ("T", "A"),
    ("C", "G"),
    ("G", "C"),
    ("AT", "AT"),
    ("CG", "CG"),
    ("CGAT", "ATCG"),
    ("AAAACCCGGT", "ACCGGGTTTT"),
])
def test_reverse_complement_dna(dna_seq, expected_output):
    assert reverse_complement_dna(dna_seq) == expected_output
