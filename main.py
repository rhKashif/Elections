"""
Election Results Processor

This module is designed to process election results data for an election night coverage.
It reads data from a supplied file, which is updated throughout the night as results come in.

Author: Hassan Kashif
"""



def load_data(filename: str) -> list:
    """
    This function reads an election results file, where each line represents a constituency's election result.

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

def parse_election_results(line: str, error_log: list) -> dict:
    """
    Each line contains a constituency name followed by party-vote pairs. This function
    extracts these details and returns a structured dictionary.

    Parameters:
    line (str): A line from the election results file.

    Returns:
    dict: A dictionary with the constituency name and a dictionary of party-vote pairs.
    """
    elements = line.strip().split(', ')
    constituency = elements.pop(0)
    votes = {}

    for i in range(1, len(elements)-1, 2):
        party = elements[i]
        try:
            vote_count = int(elements[i + 1])
            if vote_count > 0:
                votes[party] = vote_count
            else:
                votes[party] = 0
        except ValueError:
            error_log.append(f"Invalid vote count for party '{party}' in line: {line}")
    
    return {"constituency": constituency, "votes": votes}

def calculate_vote_shares(votes: dict):
    """
    Calculates the vote share of each party in a constituency.

    Parameters:
    votes (dict): A dictionary of party-vote pairs.

    Returns:
    dict: A dictionary with parties and their vote share percentages.
    """
    total_votes = sum(votes.values())
    vote_shares = {party: (votes[party] / total_votes) * 100 for party in votes}
    return vote_shares



if __name__ == "__main__":
    DATA_FILE_NAME = "sample_results.txt"

    PARTY_CODES = {
        "C": "Conservative Party", 
        "L": "Labour Party",
        "UKIP": "UKIP", 
        "LD": "Liberal Democrats", 
        "G": "Green Party", 
        "Ind": "Independent", 
        "SNP": "SNP"}

    PARTY_VOTES = {
        "Conservative Party": 0, 
        "Labour Party": 0,
        "UKIP": 0, 
        "Liberal Democrats": 0, 
        "Green Party": 0, 
        "Independent": 0, 
        "SNP": 0} 

    ELECTION_DATA = load_data(DATA_FILE_NAME)

    ERROR_LOG = []

    for line in ELECTION_DATA:
        parsed_votes = parse_election_results(line, ERROR_LOG)
        print(parsed_votes)
        # vote_shares = calculate_vote_shares(parsed_votes)
        # print(vote_shares)

    
