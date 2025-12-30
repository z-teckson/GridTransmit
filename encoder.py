"""Encoder for GridTransmit library."""

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def encode(image, prime_size=7):
    """
    Encode an image into a binary pattern using a grid of prime unit size.
    
    Args:
        image: A 2D list representing the image pixels.
        prime_size: The prime number used for grid unit size (default 7).
    
    Returns:
        A binary string representing the encoded pattern.
    
    Raises:
        ValueError: If prime_size is not a prime number.
    """
    if not is_prime(prime_size):
        raise ValueError(f"{prime_size} is not a prime number")
    
    # For demonstration, we'll just simulate encoding.
    # In real implementation, you would divide the image into grid of size prime_size.
    # Each square is encoded as black (1) or white (0).
    # Then row-by-row or column-by-column into a long pattern.
    # Here we'll just produce a dummy pattern.
    
    # Let's assume image dimensions are multiples of prime_size for simplicity.
    height = len(image)
    width = len(image[0]) if height > 0 else 0
    
    # Compute number of grid cells horizontally and vertically
    cells_x = width // prime_size
    cells_y = height // prime_size
    
    # Generate pattern: for each cell, compute average intensity and threshold
    pattern = []
    for y in range(cells_y):
        for x in range(cells_x):
            # Dummy: just take first pixel of cell
            pixel = image[y * prime_size][x * prime_size]
            # Assume pixel is 0 or 1 for simplicity
            pattern.append(str(pixel) if isinstance(pixel, int) else '0')
    
    return ''.join(pattern)


if __name__ == "__main__":
    # Example usage
    dummy_image = [[0] * 14 for _ in range(14)]  # 14x14 image, prime_size=7 divides evenly
    encoded = encode(dummy_image)
    print(f"Encoded pattern length: {len(encoded)}")