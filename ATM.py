import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_crc_diagram():
    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')  # Turn off the axes

    # Define the classes and their attributes
    classes = [
        {
            "name": "Account",
            "responsibilities": [
                "Store balance and password",
                "Authenticate user",
                "Handle deposits/withdrawals",
                "Manage daily limits"
            ],
            "collaborators": ["ATM"]
        },
        {
            "name": "ATM",
            "responsibilities": [
                "Display a user-friendly menu",
                "Process user actions",
                "Collaborate with Account for operations"
            ],
            "collaborators": ["Account"]
        },
        {
            "name": "Main",
            "responsibilities": [
                "Manage program flow",
                "Authenticate user",
                "Handle user input"
            ],
            "collaborators": ["ATM", "Account"]
        }
    ]

    # Coordinates for drawing boxes
    x_positions = [2, 5, 8]
    y_positions = 6
    box_width = 3
    box_height = 3

    # Draw the CRC cards
    for i, cls in enumerate(classes):
        x = x_positions[i]
        y = y_positions

        # Draw rectangle for the class
        rect = patches.Rectangle((x, y), box_width, box_height, edgecolor="black", facecolor="lightblue", linewidth=2)
        ax.add_patch(rect)

        # Add class name
        ax.text(x + box_width / 2, y + box_height - 0.5, cls["name"], ha="center", va="center", fontsize=12, fontweight="bold")

        # Add responsibilities
        responsibilities = "\n".join(cls["responsibilities"])
        ax.text(x + 0.1, y + box_height - 2, f"Responsibilities:\n{responsibilities}", ha="left", va="top", fontsize=10)

        # Add collaborators
        collaborators = ", ".join(cls["collaborators"])
        ax.text(x + 0.1, y + 0.3, f"Collaborators:\n{collaborators}", ha="left", va="bottom", fontsize=10)

    # Add title
    plt.title("CRC Diagram for ATM Management", fontsize=16, fontweight="bold")

    # Show the plot
    plt.show()

# Call the function to draw the CRC diagram
draw_crc_diagram()
