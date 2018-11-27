class StocksCompare:

    def __init__(self, name_a, name_b, list_a, list_b):
        self.name_a = name_a
        self.name_b = name_b
        self.list_a = list_a
        self.list_b = list_b
        self.avg_a = 0.0
        self.avg_b = 0.0
        self.variance_a = 0.0
        self.variance_b = 0.0
        self.deviation_a = 0.0
        self.deviation_b = 0.0
        self.covariance_teacher = 0.0
        self.covariance = 0.0

    def calculate_avg(self):
        for i in range(len(self.list_a)):
            self.avg_a += self.list_a[i]
            self.avg_b += self.list_b[i]
        self.avg_a /= len(self.list_a)
        self.avg_b /= len(self.list_b)
        return "The average of %s is: %s.\nThe average of %s is: %s." % \
               (self.name_a, self.avg_a, self.name_b, self.avg_b)
# Error
    
    def calculate_variance(self):
        for i in range(len(self.list_a)):
            self.variance_a += self.list_a[i] - self.avg_a
            self.variance_b += self.list_b[i] - self.avg_b
        return "The variance of %s is %s.\nThe variance of %s is %s." % \
               (self.name_a, self.variance_a, self.name_b, self.variance_b)
# possible error

    def calculate_deviation(self):
        self.deviation_a = self.variance_a ** 0.5
        self.deviation_b = self.variance_b ** 0.5
        return "The deviation of %s is %s.\nThe deviation of %s is %s." % \
               (self.name_a, self.deviation_a, self.name_b, self.deviation_b)

    def calculate_covariance(self):
        for i in range(len(self.list_a)):
            self.covariance += (self.list_a[i] - self.avg_a) * (self.list_b[i] - self.avg_b)
        self.covariance /= len(self.list_a)
        return "The covariance of the two stocks are: %s." % self.covariance

    def calculate_covariance_teacher(self):
        self.covariance_teacher += (self.list_a[-1] - self.avg_a) * (self.list_b[-1] - self.avg_b)
        return "The covariance like the teacher taught is %s." % self.covariance_teacher


list_1 = [0.4695, 0.4769, 0.659, 0.5904, 0.6659, 0.7489, 0.7909, 0.8665, 0.9556, 0.9662]
list_2 = [0.4549, 0.618, 0.5933, 0.739, 0.745, 0.6519, 0.8309, 0.8436, 0.8851, 0.9876]

compare = StocksCompare("Coca-cola", "PepsiCo", list_1, list_2)
print(compare.calculate_avg())
print(compare.calculate_variance())
print(compare.calculate_deviation())
print(compare.calculate_covariance())
print(compare.calculate_covariance_teacher())
