class Hospital:

    def __init__(self):
        self.patients = {}

    def add_patient(self, pid, name, age, disease):
        self.patients[pid] = {
            "Name": name,
            "Age": age,
            "Disease": disease,
            "Doctor": "Not Assigned",
            "Days": 0,
            "Bill": 0
        }
        return "Patient Added Successfully"

    def assign_doctor(self, pid, doctor):
        if pid in self.patients:
            self.patients[pid]["Doctor"] = doctor
            return "Doctor Assigned"
        else:
            return "Patient ID Not Found"

    def generate_bill(self, pid, days, room_charge, medicine_charge):
        if pid in self.patients:
            bill = (days * room_charge) + medicine_charge
            self.patients[pid]["Days"] = days
            self.patients[pid]["Bill"] = bill
            return bill
        else:
            return "Patient ID Not Found"

    def display_patient(self, pid):
        if pid in self.patients:
            return self.patients[pid]
        else:
            return "Patient ID Not Found"

    def discharge_patient(self, pid):
        if pid in self.patients:
            del self.patients[pid]
            return "Patient Discharged Successfully"
        else:
            return "Patient ID Not Found"
