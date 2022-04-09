# perceptron.py

def perceptron(threshold, adjustment_factor, initial_weights, examples, passes):
    """This function implements the perceptron learning model.

    Args:
        threshold: A number represents the threshold.
        adjustment_factor: A number represents how much weights should change when the prediction is different from answer given.
        initial_weights: A list of numbers represents the initial weights.
        examples: A list of pairs, the first element of each pairs is a boolean value, another is a list of "yes or no" answers.
        passes: An integer represents how many times should the model test through the examples.

    Returns: None.

    """

    # print given information
    print("Starting weights: ", end="")
    print(initial_weights)
    print("Threshold: " + str(threshold) + " " + "Adjustment: " + str(adjustment_factor))
    print()

    count = 0
    cur_weights = initial_weights.copy()

    # begin tests until reaching the number of passes
    while count < passes:
        print("Pass " + str(count + 1))
        print()

        # start to test through the examples
        for i in range(len(examples)):
            answer = examples[i][0]
            yes_no_list = examples[i][1]

            # compute the sum
            sum_res = 0
            for k in range(len(yes_no_list)):
                # check if current slot is 1
                if yes_no_list[k] == 1:
                    sum_res += cur_weights[k]

            # get the predication result
            if sum_res > threshold:
                prediction = True
            else:
                prediction = False

            # check if modifies the weights
            if answer and sum_res <= threshold:
                for j in range(len(yes_no_list)):
                    # check if current slot is 1
                    if yes_no_list[j] == 1:
                        cur_weights[j] += adjustment_factor  # increase the corresponding weights

            elif not answer and sum_res > threshold:
                for h in range(len(yes_no_list)):
                    # check if current slot is 1
                    if yes_no_list[h] == 1:
                        cur_weights[h] -= adjustment_factor  # decrease the corresponding weights

            # display information
            print("inputs: ", end="")
            print(yes_no_list)
            print("prediction: ", end="")
            print(prediction, end="")
            print(" ", end="")
            print("answer: ", end="")
            print(answer)
            print("adjusted weights: ", end="")
            print(cur_weights)

        count += 1
        # don't print a new line at the end of the file
        if count < passes:
            print()
