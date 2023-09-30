class Solution:
    def reformatDate(self, date: str) -> str:
        months = { 
            "Jan": '01', "Feb": '02', "Mar": '03', 
            "Apr": '04', "May": '05', "Jun": '06', 
            "Jul": '07', "Aug": '08', "Sep": '09', 
            "Oct": '10', "Nov": '11', "Dec": '12'
        }

        date = date.split(' ')
        day, month, year = date[0], date[1], date[2]

        day = day[:2] if len(day) == 4 else '0' + day[:1]
        month = months[month]

        return f"{year}-{month}-{day}"


        