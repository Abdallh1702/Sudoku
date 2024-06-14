from tkinter import *
import random

root = Tk()
root.geometry('1390x850')
root.maxsize(1390, 850)
root.minsize(1390, 850)
root.iconbitmap('Alecive-Flatwoken-Apps-Sudoku.ico')
root.title('Sodoku Game')
board_ = []
board = []
colors = []
arr_buttons = []
solve_number = []
filledBoard = []
root['bg'] = '#b4b8ea'
mistakes_counter = 0
mistakes_number = 0
name_mistakes = ''
check_end_game = 0
hint_counter = 0
font_g = 'black'


def isValid(num, pos):
    for i in range(9):
        if filledBoard[pos[0]][i].get() == str(num):
            return False
    for i in range(9):
        if filledBoard[i][pos[1]].get() == str(num):
            return False
    row = pos[0] // 3
    column = pos[1] // 3
    for i in range(row * 3, (row * 3) + 3):
        for j in range(column * 3, (column * 3) + 3):
            if filledBoard[i][j].get() == str(num):
                return False
    return True


class SudokuSolver:
    def __init__(self):
        self.setZero()
        self.solve()

    @staticmethod
    def setZero():
        for i in range(9):
            for j in range(9):
                if filledBoard[i][j].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    filledBoard[i][j].set(0)

    def solve(self):
        findEmpty = self.emptyCell()
        if not findEmpty:
            return True
        else:
            row, column = findEmpty
        for i in range(1, 10):
            if isValid(i, (row, column)):
                filledBoard[row][column].set(i)
                if self.solve():
                    return True
                filledBoard[row][column].set(0)
        return False

    @staticmethod
    def emptyCell():
        for row in range(9):
            for column in range(9):
                if filledBoard[row][column].get() == '0':
                    return row, column
        return None


def entry_get_name_box(button, button_name):
    global get_name_botton, check_box, name_button
    counter = 0
    for i in board_:
        i.configure(bg=colors[counter])
        counter += 1
    check_box = 0
    name_button = button_name
    get_name_botton = button
    if get_name_botton.get() != '':
        check_box = 1
        for i in board_:
            if str(i.cget('text')) == str(name_button.cget('text')):
                i.configure(bg='#d61de0')
    else:
        name_button.configure(bg='#928bcc')


def entry_get_number(button_numbers):
    global get_name_botton, number, button
    button = button_numbers
    number = button_numbers.cget('text')
    if number == '':
        return
    add_number_in_box()


def add_number_in_box():
    global check_box, get_name_botton
    if check_end_game == 1:
        return
    elif check_box == 0:
        get_name_botton.set(number)
        check_number()


def check_numbers_buttons():
    counter = 0
    for i in board_:
        if i.cget('text') == number:
            counter += 1
    if counter == 9:
        button.config(text='')


def restart_def():
    pass


def win_label():
    global check_end_game
    check_end_game = 1
    win_label = Label(root, bg='#b4b8ea', text='You Are Win', fg='green', width=13, font=('Arial', 13))
    win_label.grid(row=20, column=4)


def check_win():
    for i in arr_buttons:
        if i.get() == 0 or i.get() == '':
            return False
    win_label()


def entry_delete():
    get_name_botton.set('')


def mistakes_label():
    global mistakes_counter, mistakes_number, name_mistakes
    mistakes = Label(root, bg='#b4b8ea', text=f'Mistakes: {mistakes_counter}/{mistakes_number}', fg='green',
                        font=('Arial', 8), width=12)
    mistakes.grid(row=0, column=1)
    level = Label(root, bg='#b4b8ea', text=name_mistakes, fg='green', font=('Arial', 10), width=9)
    level.grid(row=0, column=4)


def check_number():
    number_arr_solve_to_check = str('')
    number_in_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in str(get_name_botton):
        if i in number_in_str:
            number_arr_solve_to_check += i
    number_int = int(number_arr_solve_to_check)
    number_to_solve = int(solve_number[number_int])
    number_entry_user = int(number)
    if number_entry_user == number_to_solve:
        print('win')
        name_button.configure(fg='green')
        check_numbers_buttons()
        check_win()
    else:
        name_button.configure(fg='red')
        mistakes()


def game_over():
    global check_end_game
    check_end_game = 1
    mistakes_end = Label(root, bg='#b4b8ea', text='Game Over', fg='red', width=13, font=('Arial', 13))
    mistakes_end.grid(row=20, column=4)


def hint_def():
    counter = 0
    for i in board_:
        if i.cget('text') == '':
            print(i)
            number = (solve_number[counter])
            i.config(text=number)
            i.configure(bg='#928bcc')
            return
        counter += 1


def mistakes():
    global mistakes_counter
    mistakes_counter += 1
    if name_mistakes == 'Fast':
        if mistakes_counter == 2:
            game_over()
    if name_mistakes == 'Easy':
        if mistakes_counter == 4:
            game_over()
    elif name_mistakes == 'Medium':
        if mistakes_counter == 6:
            game_over()
    elif name_mistakes == 'Hard':
        if mistakes_counter == 8:
            game_over()
    elif name_mistakes == 'Extreme':
        if mistakes_counter == 11:
            game_over()
    elif name_mistakes == 'Giant':
        if mistakes_counter == 16:
            game_over()
    mistakes_label()


def new_game_2_def():
    global mistakes_counter, mistakes_number, name_mistakes, check_end_game, board
    arr_buttons.clear()
    filledBoard.clear()
    solve_number.clear()
    board.clear()
    mistakes_counter = 0
    name_mistakes = ''
    check_end_game = 0
    start_game()


class Interface:
    def __init__(self, window):
        global solve, clear, delete, restart, hint, new_game, board, button_numbers
        self.window = window
        font = ('Arial', 23)
        delete = Button(window, text='Delete', width=10, height=1, font=('Arial', 15), fg='black', bg='#b4b8ea',
                        borderwidth=4)
        delete.config(command=lambda button_delete=delete: entry_delete())
        delete.grid(column=0, row=20, pady=3, padx=3)
        clear = Button(window, text='Clear', command=self.Clear, width=10, height=1, font=('Arial', 15), fg='black',
                        bg='#b4b8ea', borderwidth=4)
        clear.grid(column=1, row=20, pady=3, padx=3)
        hint = Button(window, text='Hint', command=hint_def, width=10, height=1, font=('Arial', 15), fg='black',
                        bg='#b4b8ea', borderwidth=4)
        hint.grid(column=2, row=20, pady=3, padx=3)
        solve = Button(window, text='Solve', command=self.Solve, width=10, height=1, font=('Arial', 15), fg='black',
                        bg='#b4b8ea', borderwidth=4)
        solve.grid(column=6, row=20, pady=3, padx=3)
        new_game = Button(window, text='New Game', command=new_game_2_def, width=10, height=1, font=('Arial', 15),
                            fg='black', bg='#b4b8ea', borderwidth=4)
        new_game.grid(column=7, row=20, pady=3, padx=3)
        restart = Button(window, text='Restart', command=restart_def, width=10, height=1, font=('Arial', 15),
                            fg='black', bg='#b4b8ea', borderwidth=4)
        restart.grid(column=8, row=20, pady=3, padx=3)
        for row in range(9):
            board += [["", "", "", "", "", "", "", "", ""]]
        row_pos = 1
        for row in range(9):
            for col in range(9):
                if (row < 3 or row > 5) and (col < 3 or col > 5):
                    color = 'white'
                    font_n = 'black'
                elif (3 <= row < 6) and (3 <= col < 6):
                    color = 'white'
                    font_n = 'black'
                else:
                    color = 'black'
                    font_n = 'white'
                board[row][col] = Button(window, width=7, font=font, bg=color, cursor='arrow', borderwidth=2,
                highlightcolor='green', highlightthickness=0, highlightbackground='black',
                textvariable=filledBoard[row][col], fg=font_n, height=0)
                arr_buttons.append(filledBoard[row][col])
                board_.append(board[row][col])
                colors.append(color)
                board[row][col].config(command=lambda button=filledBoard[row][col],
                                            button_name=board[row][col]: entry_get_name_box(button, button_name))
                board[row][col].bind('<FocusIn>', self.gridChecker)
                board[row][col].bind('<Motion>', self.gridChecker)
                board[row][col].grid(row=row_pos, column=col, padx=1, pady=1)
            row_pos += 1
        column_pas = 0
        for i in range(1, 10):
            button_numbers = Button(window, text=i, font="Helvetica 15", padx=0, pady=0, width=11, height=1, fg='black',
                                    background='#b4b8ea', borderwidth=5)
            button_numbers.config(command=lambda button_numbers=button_numbers: entry_get_number(button_numbers))
            button_numbers.grid(row=10, column=column_pas, padx=3, pady=3)
            column_pas += 1

    def gridChecker(self, event):
        for row in range(9):
            for col in range(9):
                if filledBoard[row][col].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    filledBoard[row][col].set('')

    @staticmethod
    def Solve():
        SudokuSolver()

    @staticmethod
    def Clear():
        for row in range(9):
            for col in range(9):
                filledBoard[row][col].set('')


def isValid_2(num, pos):
    for i in range(9):
        if filledBoard[pos[0]][i].get() == str(num):
            return False
    for i in range(9):
        if filledBoard[i][pos[1]].get() == str(num):
            return False
    row = pos[0] // 3
    column = pos[1] // 3
    for i in range(row * 3, (row * 3) + 3):
        for j in range(column * 3, (column * 3) + 3):
            if filledBoard[i][j].get() == str(num):
                return False
    return True


def add_number():
    number_buttons = random.randint(5, 15)
    for i in range(number_buttons):
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        number = random.randint(1, 9)
        button_number = filledBoard[row][column]
        if isValid_2(number, (row, column)):
            button_number.set(number)
    SudokuSolver()


def create_border():
    global filledBoard, filledBoard_check
    for row in range(9):
        filledBoard += [["", "", "", "", "", "", "", "", ""]]
    for row in range(9):
        for col in range(9):
            filledBoard[row][col] = StringVar(root)


def delete_in_border():
    number_buttons = random.randint(then, into)
    for i in range(number_buttons):
        t = True
        while t:
            row = random.randint(0, 8)
            column = random.randint(0, 8)
            button_number = filledBoard[row][column]
            if button_number.get() != '':
                button_number.set('')
                t = False


def add_solve_number():
    for row in range(9):
        for column in range(9):
            solve_number.append(filledBoard[row][column].get())


def fast_def():
    global then, into, name_mistakes, mistakes_number
    then = 15
    into = 25
    name_mistakes = 'Fast'
    mistakes_number = 1
    delete_start_game()
    coll_game()


def easy_def():
    global then, into, name_mistakes, mistakes_number
    then = 30
    into = 31
    name_mistakes = 'Easy'
    mistakes_number = 3
    delete_start_game()
    coll_game()


def medium_def():
    global then, into, name_mistakes, mistakes_number
    then = 42
    into = 43
    name_mistakes = 'Medium'
    mistakes_number = 5
    delete_start_game()
    coll_game()


def hard_def():
    global then, into, name_mistakes, mistakes_number
    then = 45
    into = 50
    name_mistakes = 'Hard'
    mistakes_number = 7
    delete_start_game()
    coll_game()


def extreme_def():
    global then, into, name_mistakes, mistakes_number
    then = 51
    into = 60
    name_mistakes = 'Extreme'
    mistakes_number = 10
    delete_start_game()
    coll_game()


def giant_def():
    global then, into, name_mistakes, mistakes_number
    then = 61
    into = 65
    name_mistakes = 'Giant'
    mistakes_number = 15
    delete_start_game()
    coll_game()


def start_game():
    global fast, easy, medium, hard, extreme, giant
    fast = Button(root, text='Fast', width=10, height=1, font=('Arial', 15), fg='black', bg='#b4b8ea',
                    command=fast_def)
    fast.grid(column=2, row=1, padx=3, pady=3)
    easy = Button(root, text='Easy', width=10, height=1, font=('Arial', 15), fg='black', bg='#b4b8ea',
                    command=easy_def)
    easy.grid(column=2, row=1, padx=3, pady=3)
    medium = Button(root, text='Medium', width=10, height=1, font=('Arial', 15), fg='black', bg='#b4b8ea',
                    command=medium_def)
    medium.grid(column=2, row=2, padx=3, pady=3)
    hard = Button(root, text='Hard', width=10, height=1, font=('Arial', 15), fg='black', bg='#b4b8ea',
                    command=hard_def)
    hard.grid(column=2, row=3, padx=3, pady=3)
    extreme = Button(root, text='Extreme', width=10, height=1, font=('Arial', 15), fg='black', bg='#b4b8ea',
                    command=extreme_def)
    extreme.grid(column=2, row=4, padx=3, pady=3)
    giant = Button(root, text='Giant', width=10, height=1, font=('Arial', 15), fg='black', bg='#b4b8ea',
                    command=giant_def)
    giant.grid(column=2, row=5, padx=3, pady=3)


def delete_start_game():
    fast.destroy()
    easy.destroy()
    medium.destroy()
    hard.destroy()
    extreme.destroy()
    giant.destroy()


def coll_game():
    global number
    create_border()
    add_number()
    Interface(root)
    mistakes_label()
    add_solve_number()
    delete_in_border()

start_game()
root.mainloop()

