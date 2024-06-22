from skimage import io
import numpy as np
from numba import jit
import time

RGB_IMAGE = io.imread("dizzymouse.jpg")
print("Shape:", RGB_IMAGE.shape)
print("dtype:", RGB_IMAGE.dtype)
print("Memory usage (bytes):", RGB_IMAGE.size)


def tg_numpy(color_image):
    result = np.round(
        0.299 * color_image[:, :, 0] +
        0.587 * color_image[:, :, 1] +
        0.114 * color_image[:, :, 2]
    )
    return result.astype(np.uint8)


start_time = time.time()
GRAYSCALE = tg_numpy(RGB_IMAGE)
end_time = time.time()

print(f"Time taken (NUMPY): {end_time - start_time} seconds")




@jit
def tg_numba(color_image):
    result = np.round(
        0.299 * color_image[:, :, 0] +
        0.587 * color_image[:, :, 1] +
        0.114 * color_image[:, :, 2]
    )
    return result.astype(np.uint8)


start_time = time.time()
GRAYSCALE2 = tg_numba(RGB_IMAGE)
end_time = time.time()

print(f"Time taken (simple numba): {end_time - start_time} seconds")

assert np.array_equal(GRAYSCALE, GRAYSCALE2)

@jit
def tg_numba_for_loop(color_image):
    result = np.empty(color_image.shape[:2], dtype=np.uint8)
    for y in range(color_image.shape[0]):
        for x in range(color_image.shape[1]):
            r, g, b = color_image[y, x, :]
            result[y, x] = np.round(
                0.299 * r + 0.587 * g + 0.114 * b
            )
    return result

start_time = time.time()
GRAYSCALE3 = tg_numba_for_loop(RGB_IMAGE)
end_time = time.time()

print(f"Time taken (smart numba): {end_time - start_time} seconds")

assert np.array_equal(GRAYSCALE, GRAYSCALE3)

