import os
import subprocess

def run_cas_offinder(sgRNA_sequence, genome_file, output_file, mismatches=3):
    """
    Run Cas-OFFinder to generate all possible sgRNA-target site mismatch pairs.

    :param sgRNA_sequence: The sgRNA sequence to search for.
    :param genome_file: Path to the genome file (e.g., hg19.fa).
    :param output_file: Path to the output file where results will be saved.
    :param mismatches: Maximum number of mismatches allowed (default is 3).
    """
    # Create a temporary input file for Cas-OFFinder
    with open("cas_offinder_input.txt", "w") as f:
        f.write(f"{genome_file}\n")
        f.write(f"{sgRNA_sequence} NGG\n")
    
    # Run Cas-OFFinder
    command = [
        "cas-offinder",
        "cas_offinder_input.txt",
        "C",
        str(mismatches),
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Cas-OFFinder completed successfully. Results saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running Cas-OFFinder: {e}")
    finally:
        # Clean up the temporary input file
        if os.path.exists("cas_offinder_input.txt"):
            os.remove("cas_offinder_input.txt")

def preprocess_sgRNA(sgRNA_sequence, genome_file, output_file, mismatches=3):
    """
    Preprocess the sgRNA sequence by generating all possible off-target sites using Cas-OFFinder.

    :param sgRNA_sequence: The sgRNA sequence to search for.
    :param genome_file: Path to the genome file (e.g., hg19.fa).
    :param output_file: Path to the output file where results will be saved.
    :param mismatches: Maximum number of mismatches allowed (default is 3).
    """
    print(f"Preprocessing sgRNA: {sgRNA_sequence}")
    run_cas_offinder(sgRNA_sequence, genome_file, output_file, mismatches)

if __name__ == "__main__":
    # Example usage
    # sgRNA_sequence = "GAGTCCGAGCAGAAGAAGAA"  # Replace with your sgRNA sequence
    # genome_file = "hg19.fa"  # Replace with the path to your genome file
    # output_file = "off_target_results.txt"  # Replace with your desired output file path
    # mismatches = 3  # Maximum number of mismatches

    preprocess_sgRNA(sgRNA_sequence, genome_file, output_file, mismatches)