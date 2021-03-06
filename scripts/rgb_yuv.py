
def rgb_to_yuv(R, G, B):
    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16
    U = -0.148 * R - 0.291 * G + 0.439 * B + 128
    V = 0.439 * R - 0.368 * G - 0.071 * B + 128
    return Y, U, V


def yuv_to_rgb(Y, U, V):
    Y -= 16
    U -= 128
    V -= 128
    R = 1.164 * Y + 1.596 * V
    G = 1.164 * Y - 0.392 * U - 0.813 * V
    B = 1.164 * Y + 2.017 * U
    return R, G, B


print(rgb_to_yuv(3, 5, 2))
print(yuv_to_rgb(4, 3, 3))
