# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Constraint propagation explores the idea of applying a constraint as many times as possible in order to limit
the possible choices. In other words, we are trying to limit the number of answers possible in each possible square. 
This is done repeatedly, until the contraint is no longer helpful. Naked Twin is a sudoku strategy that identifies to a pair of boxes that 
belong to the same group of peers. We identify a pair of such boxes and and then eliminate the two numbers from all the other boxes that belong 
same group. 

In my solution, I tried to use the set intersection principle to solve the problem; firstly identifying boxes that have only two elements and then amongst them the
ones that have the same two elements. By  doing so, we get a pair of naked twins. Once this is done, we remove the numbers from all of the peers of the boxes that
are in the pair called naked twins. In other words, the peers of the naked twins have these choices eliminated. 

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: My solution included an additional unit in sudoku - this is called the diagonal unit. By doing this, a diagonal will have other diagonals as peers; thus eliminating solutions that 
do not adhere by this rule. This satisfies constraint propagation, or at least does, in my humble opinion. 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

