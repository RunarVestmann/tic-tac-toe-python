def create_empty_grid():
    return {str(i): " " for i in range(1, 10)}

def display_grid(grid):
    print(grid['7'] + '|' + grid['8'] + '|' + grid['9'])
    print('-+-+-')
    print(grid['4'] + '|' + grid['5'] + '|' + grid['6'])
    print('-+-+-')
    print(grid['1'] + '|' + grid['2'] + '|' + grid['3'])

def is_in_range(value, min, max):
    return min <= value <= max

def get_choice():
    choice = ""
    while not choice.isdigit() or not is_in_range(int(choice), 1, 9):
        choice = input("Enter a number between 1 and 9: ").strip()

    return choice

def check_for_horizontal_win(grid):
    i = 1
    while i < len(grid):
        if grid[str(i)] == grid[str(i+1)] == grid[str(i+2)] != " ":
            return True
        i += 3
    return False 

def check_for_vertical_win(grid):
    i = 1
    while i < 3:
        if grid[str(i)] == grid[str(i+3)] == grid[str(i+6)] != " ":
            return True
        i += 1
    return False 

def check_for_diagonal_win(grid):
    top_left_to_bottom_right = grid["7"] == grid["5"] == grid["3"] != " "
    top_right_to_bottom_left = grid["9"] == grid["5"] == grid["1"] != " "
    return top_left_to_bottom_right or top_right_to_bottom_left

def is_game_won(grid):
    return check_for_horizontal_win(grid) or check_for_vertical_win(grid) or check_for_diagonal_win(grid)

def main():
    grid = create_empty_grid()

    turn = "x"
    turns_passed = 0

    while True:
        display_grid(grid)

        choice = get_choice()

        while grid[choice] != " ":
            print(f"Slot {choice} has already been filled out")
            choice = get_choice()

        grid[choice] = turn
        turns_passed += 1

        if is_game_won(grid):
            display_grid(grid)
            print(f"{turn} won the game")
            break
        elif turns_passed == len(grid):
            display_grid(grid)
            print("It's a tie")
            break

        turn = "o" if turn == "x" else "x"

main()