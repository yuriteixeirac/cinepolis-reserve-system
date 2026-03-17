from django.db import models
import datetime


class Session(models.Model):
    class Meta:
        app_label = 'cinema'

        
    date = models.DateField()
    start = models.TimeField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)


    def __get_timedelta(self, timestamp: datetime.time) -> datetime.timedelta:
        return datetime.timedelta(
            hours=timestamp.hour,
            minutes=timestamp.minute,
            seconds=timestamp.second
        )


    def get_end_time(self) -> datetime.time:
        start_datetime = datetime.datetime.combine(self.date, self.start)
        duration_delta = self.__get_timedelta(self.movie.duration)

        return (start_datetime + duration_delta).time()


