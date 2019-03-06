class Clock(object):
    def __init__(self, hour, minute):
        if not isinstance(hour,int) or not isinstance(minute,int):
            raise ValueError("Only integers are allowed")
        
        remained_hours ,self.minute =  divmod(minute,60)
        self.hour  = (hour + remained_hours)%24

    def __repr__(self):
        return "{0}:{1}".format(str(self.hour).zfill(2),str(self.minute).zfill(2))

    def __eq__(self, other):
        if not isinstance(other,Clock):
            return False
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour,self.minute+minutes)

    def __sub__(self, minutes):
        return Clock(self.hour,self.minute-minutes)
