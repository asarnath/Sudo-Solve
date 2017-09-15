
assignments = []

#A function that returns a cross product of the two inputs
def cross(A, B):
    return [a + b for a in A for b in B]

rows = 'ABCDEFGHI'
columns = '123456789'
reversed_columns = '987654321'

boxes = cross(rows, columns)

row_units = [cross(r, columns) for r in rows]

column_units = [cross(rows, c) for c in columns]

square_units = [cross(g, h) for g in ('ABC', 'DEF', 'GHI') for h in ('123', '456', '789')]

diagonal1_units = [[rows[i]+columns[i] for i in range(len(rows))]]

diagonal2_units = [[rows[i]+reversed_columns[i] for i in range(len(rows))]]

do_diagonal = 1 # Set this flag = 0 for non-diagonal sudoku

if do_diagonal == 1:
    total_units = row_units + column_units + square_units + diagonal1_units + diagonal2_units
else:
    total_units = row_units + column_units + square_units

#create a dictionary that would allow us to access box: unit by defining how
#these members are dependent on one another
units = dict((s, [u for u in total_units if s in u]) for s in boxes)

#create another dictionary that allows us to access the box in consideration's peers;
#peers is total_units minus the set of the unit in consideration
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    #Don't waste memory appending actions that don't actually change any values
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):

    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """


    '''Suggested by a Code Reviewer, is neater and more efficient, with fewer lines of code than set intersection.
....First, we look at individual units in the unit list '''

    """create a set from the list of twins; the set function in python creates an unordered set of elements
    without repetitions, and then use count() method to count the elements of the set
    this way you'd know exactly the two twins are naked_twins  find a twin by using the .count() method, now we shall know if a twin exists"""

    for unit in total_units:
        #From that list, create a list of twins -- technically, possible twins.
        twins_list = [values[box] for box in unit if len(values[box]) == 2]
        twins_set = set(twins_list)
        #here, val, means elements of the set
        for val in twins_set:
            if twins_list.count(val) == 2:
                # Found a twin, remove from other squares in the units
                for box in unit:
                    if values[box] != val: # criteria of units are fulfilled by the numerical value and replace the digit from other squares
                        for digit in val:
                        # assign_value(values, values[box], values[box].replace(digit, ''))
                            values= assign_value(values, box, values[box].replace(digit, ''))
    return values




def grid_values(grid):
    """
    Convert grid into dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    #Starting out, all the values in each box will be all_digits
    chars = []
    all_digits = '123456789'
    #for c in the grid, we check which one is blank and abide by all_digits rule
    for c in grid:
        if c in all_digits:
            chars.append(c)
    #otherwise if c is a possible solution and a member of all_digits then add c to the solution
        elif c == '.':
            chars.append(all_digits)
    #check that the grid has 81 single units
    assert len(chars) == 81
    #create a dictionary that would later be used to display the values
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in columns))
        if r in 'CF': print(line)
    return

def eliminate(values):
    #Solved Values
    solved_values = [box for box in values.keys() if len(values[box])==1]
    #Sort the boxes in solved_values
    for solved_value in solved_values:
    	#use dictionary key to locate the numerical value of digit
        digit = values[solved_value]
        peers_solved_value = peers[solved_value]
        #find peers in surrounding units and replace the digit with '' which means
        #digit is eliminated from the operation altogether and assigned to solved_values
        for peer in peers_solved_value:
            #values[peer] = values[peer].replace(digit, '')
            #use assign_value instead def assign_value(values, box, value)
            values = assign_value(values, peer, values[peer].replace(digit,''))
    return values

def only_choice(values):
    #Go through all the units
    for unit in total_units:
    	#search if digit is in the required set of numbers
        for digit in '123456789':
    	    #create an array of only possible choice
            choice = [box for box in unit if digit in values[box]]
    	    #check if it is the only choice
            if len(choice) == 1:
    		#assign the only choice as the digit using by obvious choice of indexing
                values = assign_value(values,choice[0],digit)
    #return values as a dictionary
    return values

def reduce_puzzle(values):
    #create an array of solved values
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    #Stop the reduction of puzzle if false
    stalled = False
    #Whilst it is not stopped -
    while not stalled:
    	#check the lenght of the solved_values before reduction
    	solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
    	#update values using the function eliminate which reduces the chances of peers having a particular value
    	values = eliminate(values)
    	#update values using the function only_choice which reduces the function further and ensures that the only possible choices are fulfilled
    	values = only_choice(values)
    	#eliminate twins
    	values = naked_twins(values)
    	#check the lenght of solved_values after reduction
    	solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
    	#if there is no change in the reduction, ie. if the puzzle remains the same there is no need to reduce it as it
    	#would only waste time. This is when we stop it.
    	stalled = solved_values_before == solved_values_after
    	#we also stop it if there are no values implemented due to whatever reason
    	if len([box for box in values.keys() if len(values[box]) == 0]):
          return False
    return values

def search(values):
    #Use Udacity code
    values = reduce_puzzle(values)
    #if the puzzle cannot be further reduced, return False
    if values == False:
        return False
    #if all the values in the boxes are of lenghth 1 (ie. solved) then return the values
    if all(len(values[s]) == 1 for s in boxes):
        return values #Solved!

    #If not solved, now we choose a square with the fewest possibilities
    #Use Udacity code
    n,s = min((len(values[s]), s) for s in boxes if len(values[s])> 1)
    for value in values[s]:
        new_puzzle = values.copy()
        new_puzzle[s] = value
        attempt = search(new_puzzle)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

    values = grid_values(grid)
    solved = search(values)
    if solved:
        return solved
    else:
        return False

solve('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
solve('52...6.........7.13...........4..8..6......5...........418.........3..2...87.....')
solve('6.....8.3.4.7.................5.4.7.3..2.....1.6.......2.....5.....8.6......1....')
solve('.......4...2..4..1.7..5..9...3..7....4..6....6..1..8...2....1..85.9...6.....8...3')
solve('15.3......7..4.2....4.72.....8.........9..1.8.1..8.79......38...........6....7423')

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

