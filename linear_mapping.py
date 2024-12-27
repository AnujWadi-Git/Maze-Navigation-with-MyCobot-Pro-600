import csv
import os

def getRobotCoordinates(cameraX, cameraY, mx, cx, my, cy):
    """
    Converts camera coordinates (cameraX, cameraY) to robot physical coordinates.
    :param cameraX: Camera X-coordinate
    :param cameraY: Camera Y-coordinate
    :param mx: X-axis scaling factor
    :param cx: X-axis offset
    :param my: Y-axis scaling factor
    :param cy: Y-axis offset
    :return: Physical coordinates (x, y) in robot space
    """
    return (cameraX * mx + cx, cameraY * my + cy)

def main():
    # Step 1: Set transformation parameters
    mx = 0.47049086898776205
    cx = -468.70182575182616
    my = -0.45646660658381577
    cy = -251.3799684090693

    # Step 2: Read x and y coordinates from the input CSV file
    input_file = "E:/ras/project/project/TEST_files/Final_files/mazexy.csv"
    points = []
    with open(input_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            x = float(row['x'])
            y = float(row['y'])
            points.append((x, y))

    # Step 3: Calculate physical coordinates for each point
    physical_coordinates = []
    print("\nPhysical coordinates of the points:")
    for i, (cameraX, cameraY) in enumerate(points):
        physicalX, physicalY = getRobotCoordinates(cameraX, cameraY, mx, cx, my, cy)
        physicalX = physicalX * 0.001  # Convert to desired units (mm to meters, for example)
        physicalY = physicalY * 0.001
        print(f"Point {i+1}: Camera Coordinates ({cameraX}, {cameraY}) -> Physical Coordinates ({physicalX}, {physicalY})")
        physical_coordinates.append((physicalX, physicalY))

    # Step 4: Save the physical coordinates to a CSV file
    folder_name = "output_coordinates"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = os.path.join(folder_name, "physical_coordinates.csv")
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Point", "PhysicalX", "PhysicalY", "PhysicalZ"])  # Write the header
        for i, (physicalX, physicalY) in enumerate(physical_coordinates, start=1):
            writer.writerow([i, physicalX, physicalY, "0.07"])  # Write each point's data

    print(f"\nPhysical coordinates have been saved to {file_name}")

if __name__ == "__main__":
    main()