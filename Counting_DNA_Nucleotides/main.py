def count_dna_nucleotides(dna_sequence: str) -> str:
    number_of_a = dna_sequence.count("A")
    number_of_c = dna_sequence.count("C")
    number_of_g = dna_sequence.count("G")
    number_of_t = dna_sequence.count("T")
    return f'{number_of_a} {number_of_c} {number_of_g} {number_of_t}'


def main():
    with open("sequences.txt") as sequences:
        for sequence in sequences:
            print(count_dna_nucleotides(sequence))


if __name__ == '__main__':
    main()
