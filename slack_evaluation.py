def are_lists_equal_with_slack(list1, list2, slack=1):
    # Check if the lists have the same length
    if len(list1) != len(list2):
        return False
    
    # Initialize the count of differences
    diff_count = 0
    
    # Iterate through the elements of both lists
    for elem1, elem2 in zip(list1, list2):
        # If the elements are not equal, increment the difference count
        if elem1 != elem2:
            diff_count += 1
            # If the difference count exceeds the slack, return False
            if diff_count > slack:
                return False
    
    # If the difference count is within the slack, return True
    return True
  
def remove_boundary_values(line):
    return line.strip().split()[1:-1]

def calculate_predictions(filename_actual, filename_predicted):
    true_prediction_s1 = 0  # true prediction with slack of 1
    false_prediction_s1 = 0  # false prediction with slack of 1
    true_prediction_s2 = 0  # true prediction with slack of 2
    false_prediction_s2 = 0  # false prediction with slack of 2

    with open(filename_actual, "r") as actual_file, open(filename_predicted, "r") as predicted_file:
        actual_lines = actual_file.readlines()
        predicted_lines = predicted_file.readlines()

    for actual_line, predicted_line in zip(actual_lines, predicted_lines):
        actual_values = remove_boundary_values(actual_line)
        predicted_values = predicted_line.strip().split()
        if are_lists_equal_with_slack(actual_values, predicted_values, slack=1):
            true_prediction_s1 += 1
        else:
            false_prediction_s1 += 1

        if are_lists_equal_with_slack(actual_values, predicted_values, slack=2):
            true_prediction_s2 += 1
        else:
            false_prediction_s2 += 1

    return true_prediction_s1, false_prediction_s1, true_prediction_s2, false_prediction_s2

if __name__ == "__main__":
    # Define the filenames for the actual and predicted data
    actual_filename = "actual.txt"
    predicted_filename = "predicted.txt"
    
    true_pred_s1, false_pred_s1, true_pred_s2, false_pred_s2 = calculate_predictions(actual_filename, predicted_filename)

    print("True predictions with slack of 1:", true_pred_s1)
    print("False predictions with slack of 1:", false_pred_s1)
    print("True predictions with slack of 2:", true_pred_s2)
    print("False predictions with slack of 2:", false_pred_s2)
    
    print(f"Accuracy with slack of 1: {true_pred_s1/(true_pred_s1+false_pred_s1)}")
    print(f"Accuracy with slack of 2: {true_pred_s2/(true_pred_s2+false_pred_s2)}")

    

