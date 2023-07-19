def smallestSufficientTeam(req_skills, people):
    skill_to_index = {skill: i for i, skill in enumerate(req_skills)}
    n = len(req_skills)
    target = (1 << n) - 1

    # Convert people's skills to bitmasks for efficient operations
    people_bitmasks = []
    for person in people:
        bitmask = 0
        for skill in person:
            bitmask |= 1 << skill_to_index[skill]
        people_bitmasks.append(bitmask)

    # Helper function for backtracking
    def backtrack(index, bitmask):
        if bitmask == target:
            return []

        if index == len(people_bitmasks):
            return None

        # Skip current person
        team1 = backtrack(index + 1, bitmask)

        # Include current person
        team2 = backtrack(index + 1, bitmask | people_bitmasks[index])
        if team2 is not None:
            team2.append(index)

        if team1 is None:
            return team2
        if team2 is None:
            return team1

        # Choose the smaller team
        return team1 if len(team1) < len(team2) else team2

    # Get the indices of the sufficient team
    team_indices = backtrack(0, 0)
    return team_indices

# Example 1
req_skills1 = ["java", "nodejs", "reactjs"]
people1 = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
print(smallestSufficientTeam(req_skills1, people1))  # Output: [0, 2]

# Example 2
req_skills2 = ["algorithms", "math", "java", "reactjs", "csharp", "aws"]
people2 = [
    ["algorithms", "math", "java"],
    ["algorithms", "math", "reactjs"],
    ["java", "csharp", "aws"],
    ["reactjs", "csharp"],
    ["csharp", "math"],
    ["aws", "java"],
]
print(smallestSufficientTeam(req_skills2, people2))  # Output: [1, 2]
