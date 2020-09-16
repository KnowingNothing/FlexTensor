dilation_shapes_test = [
    (1, 3, 448, 448, 64, 7, 7, 2, 3, 2, 1), 
    (1, 64, 112, 112, 192, 3, 3, 1, 1, 2, 1),
    (1, 192, 56, 56, 128, 1, 1, 1, 0, 2, 1),
    (1, 128, 56, 56, 256, 3, 3, 1, 1, 2, 1),
]

dilation_shapes = [
    # yolo
    (1, 256, 56, 56, 256, 1, 1, 1, 0, 2, 1),  # conv5   4
    (1, 256, 56, 56, 512, 3, 3, 1, 1, 2, 1),  # conv6   5
    (1, 512, 28, 28, 256, 1, 1, 1, 0, 2, 1),  # conv7   6
    (1, 256, 28, 28, 512, 3, 3, 1, 1, 2, 1),  # conv8   7

    (1, 512, 28, 28, 512, 1, 1, 1, 0, 2, 1),  # conv15      8
    (1, 512, 28, 28, 1024, 3, 3, 1, 1, 2, 1),  # conv16     9
    (1, 1024, 14, 14, 512, 1, 1, 1, 0, 2, 1),  # conv17    10
    (1, 512, 14, 14, 1024, 3, 3, 1, 1, 2, 1),  # conv18     11

    (1, 1024, 14, 14, 1024, 3, 3, 1, 1, 2, 1),  # conv21   12
    (1, 1024, 14, 14, 1024, 3, 3, 2, 1, 2, 1),  # conv22   13
    (1, 1024, 7, 7, 1024, 3, 3, 1, 1, 2, 1),  # conv23     14
]