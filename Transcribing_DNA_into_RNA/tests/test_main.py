import pytest

from Transcribing_DNA_into_RNA.main import transcribe_dna_to_rna


@pytest.mark.parametrize("dna_seq, expected_output", [
    ("AAA", "AAA"),
    ("AAATTT", "AAAUUU"),
])
def test_replace_all_t_with_u(dna_seq, expected_output):
    assert transcribe_dna_to_rna(dna_seq) == expected_output
