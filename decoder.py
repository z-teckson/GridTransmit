"""Decoder for GridTransmit library."""

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


def decode(pattern, width, height, prime_size=7):
    """
    Decode a binary pattern back into an image using a grid of prime unit size.
    
    Args:
        pattern: Binary string representing the encoded pattern.
        width: Width of the original image in pixels.
        height: Height of the original image in pixels.
        prime_size: The prime number used for grid unit size (default 7).
    
    Returns:
        A 2D list representing the decoded image pixels.
    
    Raises:
        ValueError: If prime_size is not a prime number.
    """
    if not is_prime(prime_size):
        raise ValueError(f"{prime_size} is not a prime number")
    
    # Compute number of grid cells horizontally and vertically
    cells_x = width // prime_size
    cells_y = height // prime_size
    
    # Ensure pattern length matches expected cells
    expected_len = cells_x * cells_y
    if len(pattern) != expected_len:
        raise ValueError(f"Pattern length {len(pattern)} does not match expected {expected_len}")
    
    # Reconstruct image
    image = [[0] * width for _ in range(height)]
    
    # For each cell, fill the corresponding block with the pattern value
    for idx, bit in enumerate(pattern):
        y_cell = idx // cells_x
        x_cell = idx % cells_x
        pixel_value = int(bit)  # assuming '0' or '1'
        # Fill the entire prime_size x prime_size block with pixel_value
        for dy in range(prime_size):
            for dx in range(prime_size):
                y = y_cell * prime_size + dy
                x = x_cell * prime_size + dx
                if y < height and x < width:
                    image[y][x] = pixel_value
    
    return image


if __name__ == "__main__":
    # Example usage
    dummy_pattern = "0" * (4 * 4)  # for 14x14 image with prime_size=7, cells_x=cells_y=2
    decoded = decode(dummy_pattern, width=14, height=14)
    print(f"Decoded image size: {len(decoded)}x{len(decoded[0])}")