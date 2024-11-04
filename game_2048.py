import random  # Import random module to place new tiles in random empty cells

def create_grid():
    """Create an empty 4x4 grid initialized with zeros."""
    # Initialize a 4x4 grid with all cells set to 0 (representing empty cells)
    return [[0 for _ in range(4)] for _ in range(4)]

def print_grid(grid):
    """Print the grid in a formatted way with dynamic cell width for large numbers."""
    # Find the largest number in the grid to set the cell width dynamically
    max_number = max(cell for row in grid for cell in row)
    cell_width = len(str(max_number)) + 2  # Set cell width based on largest number's length

    # Create the border line based on the calculated cell width
    border_line = "+" + ("-" * cell_width + "+") * 4

    # Print each row with borders and dynamic cell spacing
    print(border_line)
    for row in grid:
        row_str = "|"
        for cell in row:
            # If cell is 0 (empty), display as a space; otherwise, display the number
            cell_value = str(cell) if cell != 0 else " "
            # Center-align the cell content within the cell width
            row_str += f" {cell_value:^{cell_width - 2}} |"
        print(row_str)  # Print the row with cells separated by borders
        print(border_line)  # Print the border line after each row

def add_tile(grid):
    """Add a random '2' tile to an empty position in the grid."""
    # Find all empty positions in the grid (cells with a value of 0)
    empty_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_positions:
        # Randomly select an empty cell and place a '2' tile there
        i, j = random.choice(empty_positions)
        grid[i][j] = 2

def shift_left(grid):
    """Shift all tiles in each row to the left and combine them if possible."""
    for row in grid:
        slide(row)      # Slide tiles to the left
        combine(row)    # Combine adjacent tiles with the same value
        slide(row)      # Slide again to remove any gaps created by combining

def shift_right(grid):
    """Shift all tiles in each row to the right and combine them if possible."""
    for row in grid:
        row.reverse()   # Reverse row to treat right shift as left shift
        slide(row)      # Slide tiles to the left (original right)
        combine(row)    # Combine adjacent tiles if they match
        slide(row)      # Slide again to fill any gaps
        row.reverse()   # Reverse back to the original order after shifting

def shift_up(grid):
    """Shift all tiles in each column up and combine them if possible."""
    for col in range(4):
        # Extract the column into a temporary list
        column = [grid[row][col] for row in range(4)]
        slide(column)       # Slide tiles to the top
        combine(column)     # Combine adjacent tiles if they match
        slide(column)       # Slide again to fill gaps
        # Write back the updated column to the grid
        for row in range(4):
            grid[row][col] = column[row]

def shift_down(grid):
    """Shift all tiles in each column down and combine them if possible."""
    for col in range(4):
        # Extract and reverse the column for down shift (treated as up)
        column = [grid[row][col] for row in range(4)]
        column.reverse()    # Reverse column to handle down shift
        slide(column)       # Slide tiles to the top (original bottom)
        combine(column)     # Combine adjacent tiles if they match
        slide(column)       # Slide again to fill gaps
        column.reverse()    # Reverse back to original order after shifting
        # Write back the updated column to the grid
        for row in range(4):
            grid[row][col] = column[row]

def slide(row):
    """Slide all non-zero values in a row to the left, filling empty spaces with zeros."""
    # Filter out all zeros, leaving only non-zero values
    non_zero = [cell for cell in row if cell != 0]
    # Place non-zero values at the start of the row and fill the rest with zeros
    row[:len(non_zero)] = non_zero
    row[len(non_zero):] = [0] * (4 - len(non_zero))

def combine(row):
    """Combine adjacent tiles in a row if they have the same value."""
    for i in range(3):
        # If two adjacent cells have the same value, combine them
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2  # Double the value of the first cell
            row[i + 1] = 0  # Set the next cell to zero to indicate it was combined

def has_won(grid):
    """Check if any cell has reached 2048, indicating a win."""
    # Scan the grid to see if any cell contains 2048
    for row in grid:
        if 2048 in row:
            return True  # Return True if a winning cell is found
    return False  # Return False if no cell contains 2048

def is_game_over(grid):
    """Check if there are no valid moves left, indicating game over."""
    # Check if any cell is empty, meaning moves are still possible
    for row in grid:
        if 0 in row:
            return False  # Game is not over if there's at least one empty cell
    # Check for possible merges in each row and column
    for i in range(4):
        for j in range(4):
            # Check for adjacent cells with the same value vertically
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False  # Game is not over if a vertical merge is possible
            # Check for adjacent cells with the same value horizontally
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False  # Game is not over if a horizontal merge is possible
    # If no empty cells or merges are possible, return True for game over
    return True
