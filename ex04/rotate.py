from load_image import ft_load
from PIL import Image
from numpy import ndarray, array


def manual_transpose(arr: 'ndarray') -> 'ndarray':
    """
    Manually transpose a 2D or 3D numpy array (no numpy transpose).
    Args:
        arr: NumPy array to transpose.
    Returns:
        Transposed NumPy array.
    """
    if arr.ndim == 3 and arr.shape[2] == 1:
        arr2d = arr[:, :, 0]
        transposed = [[arr2d[j][i] for j in range(arr2d.shape[0])]
                      for i in range(arr2d.shape[1])]
        return array(transposed)
    elif arr.ndim == 2:
        transposed = [[arr[j][i] for j in range(arr.shape[0])]
                      for i in range(arr.shape[1])]
        return array(transposed)
    else:
        raise ValueError("Unsupported array shape for transpose.")


def main():
    arr = ft_load("../animal.jpeg")
    if arr is None:
        return
    transposed = manual_transpose(arr)
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)
    # Display the image
    img = Image.fromarray(transposed.astype('uint8'))
    img.show()


if __name__ == "__main__":
    main()
