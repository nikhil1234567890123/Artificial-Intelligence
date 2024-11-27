import turtle
import math

# Function to apply scaling transformation
def scale_point(x, y, sx, sy):
    return x * sx, y * sy

# Function to apply rotation transformation
def rotate_point(x, y, angle):
    angle_rad = math.radians(angle)
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return new_x, new_y

# Function to apply translation transformation
def translate_point(x, y, tx, ty):
    return x + tx, y + ty

# Function to draw a transformed shape
def draw_transformed_shape(t, points, sx, sy, angle, tx, ty):
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    
    # Apply scaling, rotation, and translation to each point and draw the transformed shape
    transformed_points = []
    for (x, y) in points:
        # Apply scaling
        x_scaled, y_scaled = scale_point(x, y, sx, sy)
        # Apply rotation
        x_rotated, y_rotated = rotate_point(x_scaled, y_scaled, angle)
        # Apply translation
        x_translated, y_translated = translate_point(x_rotated, y_rotated, tx, ty)
        transformed_points.append((x_translated, y_translated))
    
    # Draw the transformed shape
    for (x, y) in transformed_points:
        t.goto(x, y)

    # Close the shape
    t.goto(transformed_points[0][0], transformed_points[0][1])

def main():
    screen = turtle.Screen()
    screen.title("Composite Transformation (Rotation, Scaling, Translation)")
    screen.setup(width=600, height=600)

    t = turtle.Turtle()
    t.speed(1000)  # Fastest drawing speed

    # Define the points of a square
    points = [(-50, -50), (50, -50), (50, 50), (-50, 50), (-50, -50)]
    
    # Draw original shape (without transformations)
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    t.color("blue")
    for (x, y) in points:
        t.goto(x, y)
    
    # Parameters for the composite transformation
    sx, sy = 1.5, 1.5  # Scale factors
    angle = 45         # Rotation angle in degrees
    tx, ty = 100, 100  # Translation factors

    # Draw the transformed shape
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color("red")
    draw_transformed_shape(t, points, sx, sy, angle, tx, ty)

    t.hideturtle()
    turtle.done()

# Run the main function
main()
