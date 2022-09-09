def nearest_position(c_distortion, c_distortion_position):
    temp_near = c_distortion[0]
    temp_position = 0
    for i in range(len(c_distortion)):
        if c_distortion[i] < temp_near:
            temp_near = c_distortion[i]
            temp_position = i
    nearest = c_distortion_position[temp_position]
    return nearest