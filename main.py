"""
Election Results Processor

This module is designed to process election results data for an election night coverage.
It reads data from a supplied file, which is updated throughout the night as results come in.

Author: Hassan Kashif
"""

PARTY_CODES = {
    "C": "Conservative Party", 
    "L": "Labour Party",
    "UKIP": "UKIP", 
    "LD": "Liberal Democrats", 
    "G": "Green Party", 
    "Ind": "Independent", 
    "SNP": "SNP"}

def load_data(filename: str):
    """
    Load election data from a given text file.

    This function reads an election results file, where each line represents a constituency's election result.
    The file format is expected to have comma-separated values with the constituency name followed by repeating 
    pairs of party codes and the votes cast for each party.

    Parameters:
    filename (str): The path to the election results text file.

    Returns:
    list of str: A list where each element is a line from the file representing a constituency's election data.
    
    Raises:
    IOError: If the file cannot be read or does not exist.
    """
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except IOError as e:
        raise IOError(f"Error reading file {filename}: {e}")


if __name__ == "__main__":
    DATA_FILE_NAME = "sample_results.txt"
    ELECTION_DATA = load_data(DATA_FILE_NAME)
    