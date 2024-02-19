class Plateau:
    def __init__(self, upper_right_x, upper_right_y):
        self.upper_right_x = upper_right_x
        self.upper_right_y = upper_right_y
    
    def is_within_bounds(self, x, y):
        return 0 <= x <= self.upper_right_x and 0 <= y <= self.upper_right_y


class Rover:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading
    
    def move(self):
        if self.heading == "N":
            self.y += 1
        elif self.heading == "S":
            self.y -= 1
        elif self.heading == "E":
            self.x += 1
        elif self.heading == "W":
            self.x -= 1
    
    def rotate_left(self):
        if self.heading == "N":
            self.heading = "W"
        elif self.heading == "W":
            self.heading = "S"
        elif self.heading == "S":
            self.heading = "E"
        elif self.heading == "E":
            self.heading = "N"
    
    def rotate_right(self):
        if self.heading == "N":
            self.heading = "E"
        elif self.heading == "E":
            self.heading = "S"
        elif self.heading == "S":
            self.heading = "W"
        elif self.heading == "W":
            self.heading = "N"


class MovementCommand:
    def __init__(self, command):
        self.command = command
    
    def execute(self, rover):
        if self.command == "L":
            rover.rotate_left()
        elif self.command == "R":
            rover.rotate_right()
        elif self.command == "M":
            rover.move()


def process_rover_instructions(plateau, rover_position, instructions):
    x, y, heading = rover_position.split()
    rover = Rover(int(x), int(y), heading)
    
    for instruction in instructions:
        command = MovementCommand(instruction)
        command.execute(rover)
        
        if not plateau.is_within_bounds(rover.x, rover.y):
            # Handle rover going out of bounds
            break
    
    return rover.x, rover.y, rover.heading


def main():
    # Read the coordinates
    upper_right_coords = input("Enter plateau upper-right coordinates (e.g., 5 5): ").split()
    plateau = Plateau(int(upper_right_coords[0]), int(upper_right_coords[1]))
    
    rovers = []
    
    # Get the rover position
    while True:
        rover_position = input("Enter rover position (e.g., 1 2 N): ")
        instructions = input("Enter rover movement instructions (e.g., LMLMLMLMM): ")
        
        rovers.append((rover_position, instructions))
        
        choice = input("Do you want to add another rover? (Y/N): ")
        if choice.upper() != "Y":
            break
    
    # Process the  rover instruction and output final position
    for i, rover_data in enumerate(rovers, start=1):
        rover_position, instructions = rover_data
        final_position = process_rover_instructions(plateau, rover_position, instructions)
        print(f"Rover {i} final position: {final_position[0]} {final_position[1]} {final_position[2]}")


if __name__ == "__main__":
    main()