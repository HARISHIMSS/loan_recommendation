def adjust_weights_on_priority(original_weights, priority_column, priority_weight=1):
    # Create a copy of the weights
    adjusted_weights = original_weights.copy()

    # Calculate the total weight before adjustment
    total_original_weight = sum(original_weights.values())

    # Calculate the remaining weight after setting priority column
    remaining_weight = total_original_weight - original_weights[priority_column]

    # Set the priority column to its new weight
    adjusted_weights[priority_column] = priority_weight

    # Calculate the scaling factor for other weights
    scaling_factor = (total_original_weight - priority_weight) / remaining_weight

    # Adjust other weights
    for col in adjusted_weights:
        if col != priority_column:
            # Scale down the weight proportionally
            adjusted_weights[col] = original_weights[col] * scaling_factor

    return adjusted_weights

