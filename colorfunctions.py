
# do some testing, do I need this or not
# stop asking, start testing
import numpy as np

def gradient_colors(colors, n):
    """
    Generate a gradient list between multiple colors.

    Parameters:
        colors (list of str): List of hex color strings, e.g. ["#8FA9FF", "#40E0D0", "#CBA6F7"]
        n (int): Total number of steps (including start and end).

    Returns:
        list of str: List of hex colors forming the gradient.
    """

    # Convert hex to RGB
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    # Convert RGB to hex
    def rgb_to_hex(rgb):
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    # Prepare RGB list
    rgbs = [hex_to_rgb(c) for c in colors]
    segments = len(colors) - 1
    steps_per_segment = n - 1  # total divisions
    result = []

    # Generate gradient
    for i in range(n):
        # Find position in full gradient
        t = i / (n - 1)
        seg = min(int(t * segments), segments - 1)
        local_t = (t * segments) - seg

        r = int((1 - local_t) * rgbs[seg][0] + local_t * rgbs[seg + 1][0])
        g = int((1 - local_t) * rgbs[seg][1] + local_t * rgbs[seg + 1][1])
        b = int((1 - local_t) * rgbs[seg][2] + local_t * rgbs[seg + 1][2])

        result.append(rgb_to_hex((r, g, b)))

    return result

def colorlist():
    '''
    Get this exact one from the python animation file.
    Because that shit is fiiiiire.
    '''
    pass

if __name__=='__main__':
    print(gradient_colors(['#ffffff',"#000000"],20))