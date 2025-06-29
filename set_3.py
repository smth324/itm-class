"""Programming Set 3

This assignment will develop your ability to manipulate data.
"""

def relationship_status(from_member, to_member, social_graph):
    """Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    """
    if (
        to_member in social_graph[from_member]["following"]
        and from_member in social_graph[to_member]["following"]
    ):
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    """Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    """
    cross_wins = False
    circle_wins = False
    size = len(board)

    for x in range(size):
        # checks horizontally
        cross = 0
        circle = 0
        for y in range(size):
            if board[x][y] == "O":
                circle += 1
            elif board[x][y] == "X":
                cross += 1
        if cross == size:
            cross_wins = True
        elif circle == size:
            circle_wins = True

        # checks vertically
        cross = 0
        circle = 0
        for y in range(size):
            if board[y][x] == "O":
                circle += 1
            elif board[y][x] == "X":
                cross += 1
        if cross == size:
            cross_wins = True
        elif circle == size:
            circle_wins = True

    # checks diagonally
    cross = 0
    circle = 0
    for x in range(size):
        if board[x][x] == "O":
            circle += 1
        elif board[x][x] == "X":
            cross += 1

        if cross == size:
            cross_wins = True
        elif circle == size:
            circle_wins = True

    # checks diagonally the other way
    cross = 0
    circle = 0
    for x in range(size):
        if board[size - x - 1][x] == "O":
            circle += 1
        elif board[size - x - 1][x] == "X":
            cross += 1

        if cross == size:
            cross_wins = True
        elif circle == size:
            circle_wins = True

    # checks winner
    if cross_wins:
        return "X"
    elif circle_wins:
        return "O"
    else:
        return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    """ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    """
    current = first_stop
    time = 0
    temp = ""

    while True:
        for route in route_map:
            if route[0] == current:
                temp = route[1]
                time += route_map[route[0], route[1]]["travel_time_mins"]

        current = temp
        if current == second_stop:
            break
    return time

