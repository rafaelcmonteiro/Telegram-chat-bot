def multiplication(top_number_initial, bottom_number_initial):
    values_to_sum = check_signal(top_number_initial, bottom_number_initial)
    float_index = check_float_index(values_to_sum[0]) + check_float_index(values_to_sum[1])

    top_number = values_to_sum[0].replace('.', '')
    bottom_number = values_to_sum[1].replace('.', '')

    bottom_number = bottom_number[::-1]
    multiplied = []
    for digit in bottom_number:
        multiplied.append(multiplying_logic(top_number, digit))
    result = adding_zeros(multiplied)

    result = sum_logic(result)
    new_result = ''
    for index, number in enumerate(str(result)[::-1]):
        if index == float_index and float_index != 0:
            new_result += '.'
            new_result += number
        else:
            new_result += number

    if values_to_sum[2] == '+' or str(new_result) == '0':
        # Sending for formatting.
        formatting_result = formatting_content(top_number_initial, bottom_number_initial, multiplied, new_result[::-1])
        return formatting_result
    else:
        result_string = f'{values_to_sum[2]}{str(new_result)[::-1]}'
        # Sending for formatting.
        formatting_result = formatting_content(top_number_initial, bottom_number_initial, multiplied, result_string)
        return formatting_result


def multiplying_logic(top_number, bottom_number):
    answer = ''
    value = ''
    for x in reversed(range(0, len(top_number))):
        if value.isalnum():
            sum_value = int(value)
        else:
            sum_value = 0

        result = (int(top_number[x:x + 1]) * int(bottom_number)) + sum_value
        if result >= 10:
            value = str(result)[0:1]
            answer = answer + str(result)[1:2]
        else:
            value = ''
            answer = answer + str(result)
    answer = answer + value
    return answer[:: -1]


def sum_logic(initial_list):
    another_list = []
    for number in initial_list:
        another_list.append(int(number))
    result = 0
    for index in reversed(range(0, len(another_list))):
        result += another_list[index]
    return result


# This function, add zeros to the end of each number.
def adding_zeros(values):
    prepare_to_sum = []
    for index, value in enumerate(values):
        if index >= 1:
            adding_zero = index * '0'
            value = value + adding_zero
            prepare_to_sum.append(value)
        else:
            prepare_to_sum.append(value)
    return prepare_to_sum


def check_signal(x, y):
    signal = []
    string_signal = '+'
    if x[0:1] == '-':
        x = x.replace('-', '')
        signal.append('negative')
    if y[0:1] == '-':
        y = y.replace('-', '')
        signal.append('negative')

    if len(signal) > 1:
        string_signal = '+'
    elif len(signal) == 1:
        string_signal = '-'
    result_list = [x, y, string_signal]
    return result_list


def check_float_index(string_number):
    if '.' in string_number[::-1]:
        return string_number[::-1].index('.')
    else:
        return 0


def formatting_content(x, y, list_for_add, result):
    list_1 = sorted([x, y], reverse=True)
    result_length = len(result)
    # Getting the length from each number from list_1, after sorted reverse.
    length_x = len(list_1[0])
    length_y = len(list_1[1])

    # Getting the difference.
    length = length_x - length_y
    x_string = ''
    x_string += f"{(' ' * (result_length - length_x))}{list_1[0]}\n"
    x_string += f"x {list_1[1].rjust(result_length - 1)}\n"
    x_string += f"{'-' * (result_length + 1)}\n"

    for index in range(len(list_for_add)):
        x_string += f"{list_for_add[index]} {('' * index).rjust(result_length + 2)}\n"

    x_string += f"{'-' * (result_length + 1)}\n"
    x_string += f"{result}\n"
    return x_string


if __name__ == '__main__':
    print(multiplication('98765', '-12345'))
    print('')
    print('')
    print('')
    '''
    multiplication('20.2', '2.2')
    print('')
    print('')
    print('')
    multiplication('-98765', '-12345')
    print('')
    print('')
    print('')
    multiplication('594', '-3242343')
    print('')
    print('')
    print('')
    '''
    # multiplication('222.5', '100154.54')
    # multiplication('59454545454545', '32423433454')