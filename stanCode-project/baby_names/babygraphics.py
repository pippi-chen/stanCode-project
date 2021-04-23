"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # Get the space that is between the different years.
    available_width = width - 2 * GRAPH_MARGIN_SIZE
    num_line = len(YEARS)

    # Save the x coordinate of the vertical line that behaves different years.
    x_coordinate = []
    for i in range(num_line):
        x_coordinate.append(GRAPH_MARGIN_SIZE + LINE_WIDTH + i * (available_width / num_line))
        if i == year_index:
            return x_coordinate[i]


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    available_width = CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE
    num_line = len(YEARS)

    for i in range(num_line):
        # Draw the vertical lines that behave the different years.
        canvas.create_line(GRAPH_MARGIN_SIZE + i * (available_width / num_line), 0,
                           GRAPH_MARGIN_SIZE + i * (available_width / num_line), CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        # Text the year beside the vertical lines.
        canvas.create_text(GRAPH_MARGIN_SIZE + i * (available_width / num_line) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)

    # Draw the marginal lines of four sides.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # The space that between a rank on the canvas.
    one_rank = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000

    for i in range(len(lookup_names)):
        name = lookup_names[i]

        # The text that we want to print next to the name.
        rank_new = []
        # The rank that we want to display on the canvas.
        rank = []

        if name in name_data:
            # Set the information in the first year at first.
            if str(YEARS[0]) in name_data[name]:
                rank_new.append(name_data[name][str(YEARS[0])])
                rank.append(int(name_data[name][str(YEARS[0])]))
            else:
                rank_new.append('*')
                rank.append(MAX_RANK)

            # Set the first x and y coordinate on the canvas.
            first_x = get_x_coordinate(CANVAS_WIDTH, 0)
            first_y = GRAPH_MARGIN_SIZE + one_rank * (rank[0] - 1)

            # Write the text on the canvas.
            canvas.create_text(first_x + TEXT_DX, first_y, text=name + ' ' + rank_new[0], anchor=tkinter.SW,
                               fill=COLORS[i % 4])

            # Set the information of the rank in the other years.
            for j in range(1, len(YEARS)):
                if str(YEARS[j]) in name_data[name]:
                    rank_new.append(name_data[name][str(YEARS[j])])
                    rank.append(int(name_data[name][str(YEARS[j])]))
                else:
                    rank_new.append('*')
                    rank.append(MAX_RANK)

                # Set the next x and y coordinate on the canvas.
                x = get_x_coordinate(CANVAS_WIDTH, j)
                y = GRAPH_MARGIN_SIZE + one_rank * (rank[j] - 1)

                # Draw the line between the each two ranks of two years.
                canvas.create_line(first_x, first_y, x, y, width=LINE_WIDTH, fill=COLORS[i % 4])

                # Write the text on the canvas.
                canvas.create_text(x + TEXT_DX, y, text=name + ' ' + str(rank_new[j]), anchor=tkinter.SW,
                                   fill=COLORS[i % 4])

                # Reset the first x and y coordinate of the next line that between two years.
                first_x = x
                first_y = y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
