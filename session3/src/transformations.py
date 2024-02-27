def normalize(data):
    min_value = min(data)
    max_value = max(data)
    

    # Normalize each number in the list
    normalized_numbers = [(x - min_value) / (max_value - min_value) for x in data]

    return normalized_numbers