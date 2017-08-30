from datetime import timedelta
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)

year.total_seconds()
