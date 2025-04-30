import math

N = 10_000


def line_circle_dist(x, y, a, b, c):
    return abs(a * x + b * y + c) / math.sqrt(a**2 + b**2)


def main():
    rectangle_width = float(input("rectangle_width: "))
    rectangle_height = float(input("rectangle_height: "))
    ox_offset = float(input("ox_offset: "))
    circle_x_coord = float(input("circle_x_coord: "))
    circle_y_coord = float(input("circle_y_coord: "))
    circle_radius = float(input("circle_radius: "))
    movement_angle = float(input("movement_angle: "))
    line_a = math.tan(math.radians(movement_angle))
    line_b = -1
    line_c = -line_a * ox_offset
    current_coord_x = ox_offset
    current_coord_y = 0
    for i in range(N):
        next_boundary_right = (current_coord_x // rectangle_width + 1) * rectangle_width
        next_boundary_top = (current_coord_y // rectangle_height + 1) * rectangle_height
        offset_in_cur_height = ((next_boundary_top - current_coord_y) * (1 / math.tan(math.radians(movement_angle))))

        cur_circle_coord_x = next_boundary_right - rectangle_width + circle_x_coord
        cur_circle_coord_y = next_boundary_top - rectangle_height + circle_y_coord
        if (next_boundary_top / rectangle_height) % 2 == 0:
            cur_circle_coord_y = next_boundary_top - circle_y_coord
        if (next_boundary_right / rectangle_width) % 2 == 0:
            cur_circle_coord_x = next_boundary_right - circle_x_coord

        if line_circle_dist(cur_circle_coord_x, cur_circle_coord_y, line_a, line_b, line_c) <= circle_radius:
            print(f"The ray touched the circle after {i} reflections")
            return

        if next_boundary_right - current_coord_x < offset_in_cur_height:
            current_coord_y += (next_boundary_right - current_coord_x) * math.tan(math.radians(movement_angle))
            current_coord_x = next_boundary_right
        if next_boundary_right - current_coord_x == offset_in_cur_height:
            current_coord_x = next_boundary_right
            current_coord_y = next_boundary_top
        else:
            current_coord_x += (1 / math.tan(math.radians(movement_angle))) * (next_boundary_top - current_coord_y)
            current_coord_y = next_boundary_top

    print("Never intersects")


if __name__ == "__main__":
    main()