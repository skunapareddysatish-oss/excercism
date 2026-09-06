"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    x = [round(y) for y in student_scores]
    return x
    
    
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """

    pass


def count_failed_students(student_scores):
    count = 0
    for i in student_scores:
        if i <= 40:
            count +=1
        else:
            count
    return count
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    pass


def above_threshold(student_scores, threshold):
    x = [score for score in student_scores if score>=threshold]
    return x
    
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    pass


def letter_grades(highest):
    gap = highest - 40
    step = gap // 4
    return [41, 41 + step, 41 + 2 * step, 41 + 3 * step]
    
    
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    pass


def student_ranking(student_scores, student_names):
    rankings = []
    for i, (score, name) in enumerate(zip(student_scores, student_names), start=1):
        rankings.append(f"{i}. {name}: {score}")
    return rankings
    
    
    
    
    
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """

    pass


def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []
    
    
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """

    pass
