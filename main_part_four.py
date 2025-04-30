def get_str_data(line):
    line_decoded = line.decode('utf-8').strip()
    wave_length_str, value_str = line_decoded.split('\t')
    wave_length = float(wave_length_str.replace(',', '.'))
    value = float(value_str.replace(",", "."))
    return wave_length, value


def mse(mean_val, file_path="data.txt"):
    sum_val = 0
    amount = 0
    with open(file_path, 'rb') as file:
        for line in file:
            wave_length, value = get_str_data(line)
            sum_val += (value - mean_val) ** 2
            amount += 1
    res = (sum_val / amount) ** 0.5
    return res


def mae(mean_val, file_path="data.txt"):
    sum_val = 0
    amount = 0
    with open(file_path, 'rb') as file:
        for line in file:
            wave_length, value = get_str_data(line)
            sum_val += abs(value - mean_val)
            amount += 1
    res = (sum_val / amount)
    return res


def mean(file_path="data.txt"):
    sum_val = 0
    amount = 0
    with open(file_path, 'rb') as file:
        for line in file:
            wave_length, value = get_str_data(line)
            sum_val += value
            amount += 1
    return sum_val / amount


def solution():
    mean_val = mean()
    mae_val = mae(mean_val)
    mse_val = mse(mean_val)
    print(mae_val)
    print(mse_val)


solution()