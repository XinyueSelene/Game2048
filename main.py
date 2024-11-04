from game_2048 import create_grid, add_tile, shift_left, shift_right, shift_up, shift_down, has_won, is_game_over, print_grid
set
def main():
    # Outer loop to allow restarting the game without exiting the program
    while True:
        # Initialize a new game grid with all cells set to zero
        grid = create_grid()
        # Add two initial '2' tiles at random positions to start the game
        add_tile(grid)
        add_tile(grid)
        # Display the initial state of the grid to the user
        print_grid(grid)

        # Inner game loop, runs until the player wins, exits, or the game ends
        while True:
            # Prompt the player to input a direction for tile movement or type 'exit' to quit
            direction = input("Next Move (w: up, s: down, a: left, d: right, or type 'exit' to quit): ").strip().lower()
            
            # Check if the user wants to exit the game
            if direction == 'exit':
                print("Game ended. Thanks for playing!")
                return  # Exit the function to end the game

            # Check if the input is one of the valid move keys
            if direction in ['w', 's', 'a', 'd']:
                # Move tiles based on the direction input
                if direction == 'w':
                    shift_up(grid)    # Move tiles up
                elif direction == 's':
                    shift_down(grid)  # Move tiles down
                elif direction == 'a':
                    shift_left(grid)  # Move tiles left
                elif direction == 'd':
                    shift_right(grid) # Move tiles right

                # Add a new '2' tile at a random empty position after every move
                add_tile(grid)
                # Display the updated grid state to the player
                print_grid(grid)

                # Check if the player has won the game
                if has_won(grid):
                    print("Congratulations! You've reached 2048!")
                    # Ask if the player wants to restart the game or end
                    choice = input("Would you like to restart the game? (y/n): ").strip().lower()
                    if choice == 'y':
                        # Break out of the inner loop to restart the game
                        break
                    else:
                        # Exit the function to end the game
                        return

                # Check if the game is over (no moves left)
                if is_game_over(grid):
                    print("Game over! No moves left.")
                    # Ask if the player wants to restart the game or end
                    choice = input("Would you like to restart the game? (y/n): ").strip().lower()
                    if choice == 'y':
                        # Break out of the inner loop to restart the game
                        break
                    else:
                        # Exit the function to end the game
                        return
            else:
                # Print an error message if the input is not recognized
                print("Please enter a valid move (w, a, s, d), or type 'exit' to quit.")

# Run the main game loop if the script is executed directly
if __name__ == "__main__":
    main()
