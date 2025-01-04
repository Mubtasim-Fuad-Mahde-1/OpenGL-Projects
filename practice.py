import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    # Calculate differences in coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Determine increments
    incrementX = 1 if dx > 0 else -1
    incrementY = 1 if dy > 0 else -1

    # Initialize variables
    x = x1
    y = y1
    decisionParameter = 2 * abs(dy) - abs(dx)

    # Plot initial point
    plt.plot(x, y, 'ro')

    # Begin loop
    for i in range(1, abs(dx)):
        # Plot the current point
        plt.plot(x, y, 'ro')
        
        # Increment x
        x += incrementX
        
        # Update decision parameter
        if decisionParameter < 0:
            decisionParameter += 2 * abs(dy)
        else:
            decisionParameter += 2 * abs(dy) - 2 * abs(dx)
            # Increment y
            y += incrementY

    # Plot the final point
    plt.plot(x2, y2, 'ro')
    
    # Display the line
    plt.plot([x1, x2], [y1, y2], 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Midpoint Line Drawing Algorithm')
    plt.grid(True)
    plt.show()

# Example usage:
draw_line(100, 100,100, 200)
