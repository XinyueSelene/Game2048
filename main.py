import game_2048  # Import all functions from game_2048 module

def main():
    # Outer loop to allow restarting the game without exiting the program
    while True:
        # Initialize a new game grid with all cells set to zero
        grid = game_2048.create_grid()
        # Add two initial '2' tiles at random positions to start the game
        game_2048.add_tile(grid)
        game_2048.add_tile(grid)
        # Display the initial state of the grid to the user
        game_2048.print_grid(grid)

        # Inner game loop, runs until the player wins, exits, or the game ends
        while True:
            try:
                # Prompt the player to input a direction for tile movement or type 'exit' to quit
                direction = input("Choose a move (w: up, s: down, a: left, d: right, or type 'exit' to quit): ").strip().lower()
                
                # Check if the user wants to exit the game
                if direction == 'exit':
                    print("Game ended. Thanks for playing!")
                    return  # Exit the function to end the game

                # Create a copy of the grid to check for changes
                original_grid = game_2048.copy_grid(grid)

                # Check if the input is one of the valid move keys
                if direction in ['w', 's', 'a', 'd']:
                    # Move tiles based on the direction input
                    if direction == 'w':
                        game_2048.shift_up(grid)    # Move tiles up
                    elif direction == 's':
                        game_2048.shift_down(grid)  # Move tiles down
                    elif direction == 'a':
                        game_2048.shift_left(grid)  # Move tiles left
                    elif direction == 'd':
                        game_2048.shift_right(grid) # Move tiles right

                    # Only add a new tile if the grid changed
                    if grid != original_grid:
                        game_2048.add_tile(grid)
                    else:
                        print("No change in grid state. No new tile added.")

                    # Display the updated grid state to the player
                    game_2048.print_grid(grid)

                    # Check if the player has won the game
                    if game_2048.has_won(grid):
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
                    if game_2048.is_game_over(grid):
                        print("Game over! No moves left.")
                        # Ask if the player wants to restart the game
                        choice = input("Would you like to restart the game? (y/n): ").strip().lower()
                        if choice == 'y':
                            # Break out of the inner loop to restart the game
                            break
                        else:
                            # Exit the function to end the game
                            return
                else:
                    # Print an error message if the input is not recognized
                    print("Please enter a valid move (w, a, s, or d), or type 'exit' to quit.")

            except Exception as e:
                # Catch any unexpected errors and print a friendly message
                print(f"An error occurred: {e}. Ending the game.")
                return  # End the game gracefully if an error occurs

# Run the main game loop if the script is executed directly
if __name__ == "__main__":
    main()