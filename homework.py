import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        today_stats = sum(record.amount if record.date == today 
                          else 0 for record in self.records)
        return today_stats

    def get_week_stats(self):
        today = dt.date.today()
        week_ago = today - dt.timedelta(7)
        week_stats = sum(record.amount if week_ago <= record.date <= today 
                          else 0 for record in self.records)
        return week_stats

    def remained(self):
        return self.limit - self.get_today_stats()


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        colories_remained = self.remained()
        if colories_remained <= 0:
            return 'Хватит есть!'
        return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                f'калорийностью не более {colories_remained} кКал')


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),
        }
        sign = currencies.get(currency)[0]
        rate = currencies.get(currency)[1]
        cash_remained = round(self.remained() / rate, 2)
        if cash_remained == 0:
            return 'Денег нет, держись'
        if cash_remained > 0:
            return f'На сегодня осталось {cash_remained} {sign}'
        if cash_remained < 0:
            cash_remained = abs(cash_remained)
            return f'Денег нет, держись: твой долг - {cash_remained} {sign}'
