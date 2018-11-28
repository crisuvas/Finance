class StocksCompare:

    def __init__(self, initial_investment, name_a, name_b, stock_to_a, stock_to_b, list_a, list_b):
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
        self.correlation = 0.0
        self.correlation_teacher = 0.0
        self.profitability_without_risk = 0.0
        self.variance_of_portfolio = 0.0
        self.portfolio_risk = 0.0
        self.beta_a = 0.0
        self.portfolio_performance = 0.0
        self.initial_investment = initial_investment
        self.stock_to_a = stock_to_a
        self.stock_to_b = stock_to_b
        self.calculate_avg()
        self.calculate_variance()
        self.calculate_deviation()
        self.calculate_covariance()
        self.calculate_covariance_teacher()
        self.calculate_correlation()
        self.calculate_correlation_teacher()
        if self.stock_to_a < 1:
            self.change_percentage()
        self.calculate_profitability_without_risk()
        self.calculate_variance_portfolio()
        self.calculate_risk_portfolio()
        self.calculate_beta_a()
        self.calculate_portfolio_performance()

    def calculate_avg(self):
        for i in range(len(self.list_a)):
            self.avg_a += self.list_a[i]
            self.avg_b += self.list_b[i]
        self.avg_a /= len(self.list_a)
        self.avg_b /= len(self.list_b)
    
    def calculate_variance(self):
        for i in range(len(self.list_a)):
            self.variance_a += (self.list_a[i] - self.avg_a) ** 2
            self.variance_b += (self.list_b[i] - self.avg_b) ** 2
        self.variance_a /= len(self.list_a)
        self.variance_b /= len(self.list_b)

    def calculate_deviation(self):
        self.deviation_a = self.variance_a ** 0.5
        self.deviation_b = self.variance_b ** 0.5

    def calculate_covariance(self):
        for i in range(len(self.list_a)):
            self.covariance += (self.list_a[i] - self.avg_a) * (self.list_b[i] - self.avg_b)
        self.covariance /= len(self.list_a)

    def calculate_covariance_teacher(self):
        self.covariance_teacher += (self.list_a[-1] - self.avg_a) * (self.list_b[-1] - self.avg_b)

    def calculate_correlation(self):
        self.correlation = self.covariance/(self.deviation_a * self.deviation_a)

    def calculate_correlation_teacher(self):
        self.correlation_teacher = self.covariance_teacher/(self.deviation_a * self.deviation_b)

    def change_percentage(self):
        self.stock_to_a *= self.initial_investment
        self.stock_to_b *= self.initial_investment

    def calculate_profitability_without_risk(self):
        self.profitability_without_risk = (self.stock_to_a * self.avg_a + self.stock_to_b * self.avg_b) / self.initial_investment

    def calculate_variance_portfolio(self):
        self.variance_of_portfolio = (self.avg_a ** 2 * self.deviation_a ** 2) + \
                                     2*(self.avg_a * self.deviation_a * self.avg_b *
                                        self.deviation_b * self.correlation_teacher) + \
                                     (self.avg_b ** 2 * self.deviation_b ** 2)

    def calculate_risk_portfolio(self):
        self.portfolio_risk = self.variance_of_portfolio ** 0.5

    def calculate_beta_a(self):
        self.beta_a = self.covariance_teacher / self.variance_b

    def calculate_portfolio_performance(self):
        self.portfolio_performance = self.avg_b + self.beta_a * (self.avg_a - self.avg_b)


list_1 = [0.4695, 0.4769, 0.659, 0.5904, 0.6659, 0.7489, 0.7909, 0.8665, 0.9556, 0.9662]
list_2 = [0.4549, 0.618, 0.5933, 0.739, 0.745, 0.6519, 0.8309, 0.8436, 0.8851, 0.9876]

compare = StocksCompare(22614800, "Coca-cola", "PepsiCo", 8132500, 14482300, list_1, list_2)
print(compare.portfolio_performance)
