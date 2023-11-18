# values: tuple[] | num[]
# frequencies: num[] | None

class FrequencyDistribution:
    def __init__(self, values, frequency=None):
        self.grouped = False
        self.frequency = []
        self.class_mark = []
        self.class_boundary = []
        self.class_size = 1
        self.class_boundary_gap = 0
        self.index_map = None
        self.rows = 0

        if type(values[0]) is tuple:
            self.grouped = True

        position_map = {}
        if not self.grouped:
            values.sort()
            for value in values:
                if value in position_map:
                    position = position_map[value]
                    self.frequency[position] += 1
                    continue

                position_map[value] = len(self.class_mark)
                self.class_mark.append(value)
                self.frequency.append(1)
        else:
            values_frequency = zip(values, frequency)
            values_frequency = sorted(values_frequency)
            values = [v for v, _ in values_frequency]
            frequency = [f for _, f in values_frequency]

            self.class_size = values[1][0] - values[0][0]
            self.class_boundary_gap = (values[1][0] - values[0][1]) / 2.0
            if not frequency:
                frequency = [1 for _ in values]

            for i in range(len(values)):
                lower, upper = values[i]
                class_mark = (lower + upper) / 2.0
                self.class_mark.append(class_mark)
                self.frequency.append(frequency[i])
                self.class_boundary.append((lower, upper))
                position_map[class_mark] = i

        self.index_map = position_map
        self.rows = len(self.class_mark)

class StatCalculator:
    def __init__(self, values, frequency=None, precision=2):
        self.table = FrequencyDistribution(values, frequency)
        self.precision = precision

    def mean(self):
        tb = self.table
        frequency_x = [0 for _ in tb.class_mark]
        for row in range(tb.rows):
            frequency_x[row] = tb.frequency[row] * tb.class_mark[row]

        result = sum(frequency_x) / sum(tb.frequency)
        return round(result, self.precision)

    def mode(self):
        tb = self.table
        modal_index = 0
        for row in range(tb.rows):
            if tb.frequency[row] > tb.frequency[modal_index]:
                modal_index = row
        if tb.grouped == False:
            return tb.class_mark[modal_index]

        lower_class_boundary = tb.class_boundary[modal_index][0] - tb.class_boundary_gap
        diff1 = tb.frequency[modal_index] - (
            0 if modal_index == 0 else tb.frequency[modal_index - 1]
        )
        diff2 = tb.frequency[modal_index] - (
            0 if modal_index == tb.rows - 1 else tb.frequency[modal_index + 1]
        )

        result = lower_class_boundary + ((diff1 / (diff1 + diff2)) * tb.class_size)
        return round(result, self.precision)

    def partition(self, position, size):
        tb = self.table
        partition_index = 0
        partition_size = (position * sum(tb.frequency)) / size
        cummulative_frequency = [tb.frequency[0]]

        for i in range(1, tb.rows):
            cummulative_frequency.append(cummulative_frequency[i - 1] + tb.frequency[i])
        for i in range(tb.rows):
            partition_index = i
            if cummulative_frequency[i] >= partition_size:
                break

        if tb.grouped == False:
            return tb.class_mark[partition_index]

        lower_class_boundary = (
            tb.class_boundary[partition_index][0] - tb.class_boundary_gap
        )
        cummulative_before = (
            0 if partition_index == 0 else cummulative_frequency[partition_index - 1]
        )

        result = lower_class_boundary + (
            ((partition_size - cummulative_before) / tb.frequency[partition_index])
            * tb.class_size
        )
        return round(result, self.precision)

    def median(self):
        return self.partition(1, 2)

    def quartile(self, num):
        valid_nums = {1, 2, 3}
        if num not in valid_nums:
            print("Invalid Quartile Position")
        else:
            return self.partition(num, 4)

    def decile(self, num):
        valid_nums = {n for n in range(1, 11)}
        if num not in valid_nums:
            print("Invalid Decile Position")
        else:
            return self.partition(num, 10)

    def percentile(self, num):
        valid_nums = {n for n in range(1, 101)}
        if num not in valid_nums:
            print("Invalid Percentile Position")
        else:
            return self.partition(num, 100)

    def range(self):
        tb = self.table
        if tb.grouped == False:
            return tb.class_mark[-1] - tb.class_mark[0]

        result = tb.class_boundary[-1][-1] - tb.class_boundary[0][0]
        return result

    def mean_deviation(self):
        tb = self.table
        mean = self.mean()
        freq_deviations = []
        for row in range(tb.rows):
          freq_deviations.append(
            tb.frequency[row] * abs(tb.class_mark[row] - mean)
          )

        result = sum(freq_deviations) / sum(tb.frequency)
        return round(result, self.precision)

    def variance(self, sample=False):
        tb = self.table
        mean = self.mean()
        freq_square_deviations = []
        for row in range(tb.rows):
          freq_square_deviations.append(
            tb.frequency[row] * pow(tb.class_mark[row] - mean, 2)
          )

        sum_square_deviations = sum(freq_square_deviations)
        n = sum(tb.frequency)

        if not sample:  # population variance
            result = sum_square_deviations / n
        else:  # sample variance
            result = sum_square_deviations / (n - 1)

        return round(result, self.precision)

    def standard_deviation(self, sample=False):
        result = pow(self.variance(sample), 0.5)
        return round(result, self.precision)