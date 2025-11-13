class AppointmentList():
    def __init__(self):
        self.appointments = []
        pass



# child
class AppointmentBooking(AppointmentList):
    # Constructor
    def __init__(self):
        super().__init__()


    # book an appointment
    def book_appointment(self,id,patient,doctor,time):
        current_app = {"id":id,"patient" :patient,"doctor" :doctor,"time":time}
        print(self.appointments)


first = AppointmentBooking()
frist.book_appointment(id=1,patient="john",doctor="saravana")