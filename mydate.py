class MyDate:

    # 각 월에 마지막 날을 담은 리스트
    last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    def __init__(self, year = 0, month = 0, day = 0, hour = 0, minute = 0 , sec = 0):

        
        if not(1 <= month <= 12):
            raise ValueError("오류 발생")
        if not (1 <= day <= self.last_day[month - 1]): 
           raise ValueError("오류")
        if not (0 <= hour <= 23):
            raise ValueError("오류 발생")
        if not (0 <= minute <= 59):
            raise ValueError("오류 발생")
        if not (0 <= sec <= 59):
            raise ValueError("오류 발생")
        
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.sec = sec


    
    def leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    


       
    def __add__(self, other):
            self_date = [self.year, self.month, self.day, self.hour, self.minute, self.sec]
            other_date = [other.year, other.month, other.day, other.hour, other.minute, other.sec]

            # 리스트 더하기
            sum_year = self_date[0] + other_date[0]
            sum_month = self_date[1] + other_date[1]
            sum_day = self_date[2] + other_date[2]
            sum_hour = self_date[3] + other_date[3]
            sum_minute = self_date[4] + other_date[4]
            sum_sec = self_date[5] + other_date[5]

            # 초, 분, 시, 일 반올림
            rounding_minute, sum_sec = divmod(sum_sec, 60)
            rounding_hour, sum_minute = divmod(sum_minute + rounding_minute, 60)
            rounding_day, sum_hour = divmod(sum_hour + rounding_hour, 24)
            
            sum_day += rounding_day 
            rounding_month, sum_day = divmod(sum_day - 1, self.last_day[sum_month - 1])  
            sum_month += rounding_month
            rounding_year, sum_month = divmod(sum_month - 1, 12) 
            sum_year += rounding_year
            
            sum_month += 1  # 1부터 시작
            sum_day += 1    # 1부터 시작

            return (sum_year, sum_month, sum_day, sum_hour, sum_minute, sum_sec) 



    def __sub__(self, other, datetime):
        pass
         

    def __eq__(self, other):
        pass 


    def __lt__(self, other):
        pass 
    
    def __le__(self, other):
        pass 

    def __gt__(self, other):
        pass 

    def __ge__(self, other):
        pass 

if __name__ == '__main__':
    d1 = MyDate(2022, 4, 1, 14, 30, 45)
    d2 = MyDate(2024, 8, 10, 23, 15, 30)
    

    d2 = MyDate(2024, 8, 100, 23, 10) # should raise an error 
    d3 = MyDate(2024, 2, 30) # should raise an error 
    MyDate.__init__(d3, 2024, 2, 30)
    
    result = d1 + d2
    print(result)


    d1+d2
    MyDate.__add__(d1, d2)

    d1-d2
    MyDate.__sub__(d1, d2)


    d1 == d2
    MyDate.__eq__(d1, d2)

    d1 < d2
    MyDate.__lt__(d1, d2)

    d1 <= d2
    MyDate.__le__(d1, d2) 

    d1 > d2
    MyDate.__gt__(d1, d2)

    d1 >= d2
    MyDate.__ge__(d1, d2)


    d3 = MyDate(day = 1) 
    assert d1 + d3 == MyDate(2022, 4, 2, 14, 30)
    assert d1 - d3 == MyDate(2022, 3, 31, 14, 30) 

    assert d1 < d2 


    d4 = MyDate(2023, 1, 31)
    d5 = MyDate(day = 30)
    assert d4 + d5 == MyDate(2023, 3, 2)



    
    
