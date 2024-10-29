#! /usr/bin/env python3

import contextlib
import numpy as np

def coord(i, n, phase, delta):
    t = np.deg2rad(i / n * 360)

    mul = 0.25 * np.abs(np.sin(t / 2)) ** 0.5

    x = 0.65 * (t - np.pi)
    y = np.sin(np.deg2rad(i / n * 360 - phase)) + mul * delta
    return (x, -y)

snakes = [
    ("#ffdd56"  ,   0,     0, 101, 200, ( 10, 0.01, 0.035)),
    ("#346f9f"    , -90,     0, 200, 200, (190,  -0.02, 0.035) ),
    ("#ffdd56"  ,   0,   100, 200, 200,       None )
]

def render_snake(a, b, n, phase, eye):

    path = []
    for i in range(a, b):

        segment = [ "M", *coord(i    , n, phase, -1),
                    "L", *coord(i + 1, n, phase, -1),
                    "L", *coord(i + 1, n, phase, +1),
                    "L", *coord(i    , n, phase, +1),
                    "Z" ]
        path.extend(segment)

    r_eye = 0.05

    if eye is not None:

        (eye_x, eye_y, eye_r) = eye

        (cx, cy) = coord(eye_x, n, phase, 0)
        segment = [
                    "M", cx - eye_r, cy + eye_y,
                    "A", eye_r * 1.001, eye_r * 1.001, 0,     0, 1, cx + eye_r, cy + eye_y,
                    "A", eye_r * 1.001, eye_r * 1.001, 0,     0, 1, cx - eye_r, cy + eye_y
                  ]
        path.extend(segment)

    return path


with open("pydwf-logo.svg", "w") as fo, contextlib.redirect_stdout(fo):
    print('<svg width="200" height="125" xmlns="http://www.w3.org/2000/svg">')

    for (snake_color, snake_phase, a, b, n, eye) in snakes:

        snake = render_snake(a, b, n, snake_phase, eye)

        snake_path_str = " ".join(str(x) for x in snake)

        print('    <path fill="{}" d="{}" transform="translate(100, 62.5) scale(48)" />'.format(snake_color, snake_path_str))

    print('</svg>')
