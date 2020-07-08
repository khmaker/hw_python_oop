import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit
        self.today = dt.date.today()

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        for i in self.records:
            if i.date == self.today:
                today_stats += i.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        for i in self.records:
            if 0 <= (self.today - i.date).days <= 7:
                week_stats += i.amount
        return week_stats


class Record:
    today = dt.date.today().strftime('%d.%m.%Y')

    def __init__(self, amount, comment, date=today):
        self.amount = amount
        self.comment = comment
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

    def __repr__(self):
        return f'{self.amount}\n{self.comment}\n{self.date}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        colories_remained = self.limit - self.get_today_stats()
        if colories_remained <= 0:
            return f'Хватит есть!'
        return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {colories_remained} кКал')


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def get_today_cash_remained(self, currency):
        cash_remained = self.limit - self.get_today_stats()
        sign = 'руб'
        if currency == 'usd':
            cash_remained = round(cash_remained / self.USD_RATE, 2)
            sign = 'USD'
        elif currency == 'eur':
            cash_remained = round(cash_remained / self.EURO_RATE, 2)
            sign = 'Euro'
        if cash_remained == 0:
            return f'Денег нет, держись'
        if cash_remained > 0:
            return f'На сегодня осталось {cash_remained} {sign}'
        if cash_remained < 0:
            return f'Денег нет, держись: твой долг - {abs(cash_remained)} {sign}'


if __name__ == '__main__':
    pass