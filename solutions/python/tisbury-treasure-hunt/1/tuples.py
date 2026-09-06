"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]
    
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """

    pass


def convert_coordinate(coordinate):
    return tuple(coordinate)
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """

    pass


def compare_records(azara_record, rui_record):
    if tuple(azara_record[1]) == rui_record[1]:
        return True
    return False
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """

    pass


def create_record(azara_record, rui_record):
    treasure, azara_coord = azara_record
    location, rui_coord, quadrant = rui_record

    azara_coord_tuple = (azara_coord[0], azara_coord[1])

    if azara_coord_tuple == rui_coord:
        return (treasure, azara_coord, location, rui_coord, quadrant)
    return "not a match"
    
    
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """

    pass


def clean_up(combined_record_group):
    report = ""
    for record in combined_record_group:
        cleaned = (record[0], record[2], record[3], record[4])
        report += str(cleaned) + "\n"
    return report
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """

    pass
