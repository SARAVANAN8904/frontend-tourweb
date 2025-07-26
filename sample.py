def count_arrangements(g, y, r):
    def backtrack(current_arrangement, g_left, y_left, r_left, last_color):
        # Base case: If no balls are left, we have a complete valid arrangement
        if g_left == 0 and y_left == 0 and r_left == 0:
            arrangements.append(current_arrangement)
            return

        # Recursive case: Place each type of ball if it's available and not the same as the last one
        if g_left > 0 and last_color != 'G':
            backtrack(current_arrangement + 'G', g_left - 1, y_left, r_left, 'G')
        if y_left > 0 and last_color != 'Y':
            backtrack(current_arrangement + 'Y', g_left, y_left - 1, r_left, 'Y')
        if r_left > 0 and last_color != 'R':
            backtrack(current_arrangement + 'R', g_left, y_left, r_left - 1, 'R')

    # List to store all valid arrangements
    arrangements = []
    # Start the backtracking with an empty arrangement
    backtrack("", g, y, r, "")
    return len(arrangements), arrangements


# Test the function with input values
g, y, r = 1, 1, 1
count, arrangements = count_arrangements(g, y, r)
print("Output:", count)
print("Arrangements:", arrangements)
