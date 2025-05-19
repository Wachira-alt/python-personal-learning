# OBJECT RELATIONSHIPS
 #in real world objects are related in complex ways
#There are three relationship types


              #ONE-TO-ONE
# one object from class A is linked to only one object in class B
# example a person has only one passport


class Passport:

  citizens = []

  def __init__(self, number):
    self.number = number

class Person:
  def __init__(self, name, passport):
    self.name = name
    self.passport = passport
  

passport =Passport("A1234")
person = Person("Dennis", passport)


              #ONE -TO- MANY
# 🧪 Real-World Challenge
# Scenario: You are building a hospital system.

# Design the following:

# A Doctor can see many Patients.

# A Patient can only have one assigned Doctor.

# The Hospital owns Rooms, but Rooms can be reassigned.

# Each Room has Beds created at initialization (not reused elsewhere).

# Can you:

# Model the Doctor-Patient relationship with SSOT?

# Show how Hospital aggregates Room?

# Show how Room uses composition to create Beds?
# Perfect, Dennis. Let's tackle the hospital system challenge step-by-step, illustrating:

# ✅ One-to-many using SSOT: Doctor ↔ Patient

# ✅ Aggregation: Hospital ↔ Room

# ✅ Composition: Room ↔ Bed

# ✅ STEP 1: One-to-Many (SSOT) – Doctor and Patient
# ✅ Goal
# A Doctor can have many patients.

# A Patient has only one assigned doctor.

# Doctor owns the relationship (SSOT: Single Source of Truth)

# 🧠 Design Decision
# Keep a list of Patient objects in Doctor.

# The Patient only refers to their Doctor — not a list.

# 🧪 Code

class Doctor:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Must be a Patient")
        if patient not in self.patients:
            self.patients.append(patient)
            patient.doctor = self  # SSOT: set from Doctor side

    def __repr__(self):
        return f"Doctor({self.name})"


class Patient:
    def __init__(self, name):
        self.name = name
        self._doctor = None

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, value):
        if not isinstance(value, Doctor):
            raise TypeError("Doctor must be a Doctor object")
        self._doctor = value  # No circular update to avoid recursion

    def __repr__(self):
        return f"Patient({self.name})"
    
doc = Doctor("Dr. Wachira")
p1 = Patient("John")
p2 = Patient("Mary")

doc.add_patient(p1)
doc.add_patient(p2)

print(doc.patients)         # [Patient(John), Patient(Mary)]
print(p1.doctor.name)       # Dr. Wachira



# ✅ STEP 2: Aggregation – Hospital and Room
# ✅ Goal
# A Hospital owns many rooms.

# Room objects can live independently of Hospital.

# 🧠 Design Decision
# Hospital accepts existing Room objects and tracks them in a list.

# 🧪 Code

class Room:
    def __init__(self, room_number):
        self.room_number = room_number

    def __repr__(self):
        return f"Room({self.room_number})"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        if not isinstance(room, Room):
            raise TypeError("Only Room instances allowed")
        self.rooms.append(room)

    def __repr__(self):
        return f"Hospital({self.name})"

room1 = Room(101)
room2 = Room(102)

hospital = Hospital("Nairobi General")
hospital.add_room(room1)
hospital.add_room(room2)

print(hospital.rooms)  # [Room(101), Room(102)]


# ✅ STEP 3: Composition – Room and Bed
# ✅ Goal
# A Room owns Beds.

# Beds are created inside the Room.

# When Room is deleted, so are its beds.

# 🧠 Design Decision
# Create Bed objects inside the Room constructor.

# 🧪 Code

class Bed:
    def __init__(self, bed_number):
        self.bed_number = bed_number

    def __repr__(self):
        return f"Bed({self.bed_number})"


class ComposedRoom:
    def __init__(self, room_number, bed_count):
        self.room_number = room_number
        self.beds = [Bed(b + 1) for b in range(bed_count)]  # Create beds internally

    def __repr__(self):
        return f"ComposedRoom({self.room_number}, Beds: {len(self.beds)})"
    
room_with_beds = ComposedRoom(201, 3)
print(room_with_beds.beds)  # [Bed(1), Bed(2), Bed(3)]

    
hospital.add_room(room_with_beds)

doc2 = Doctor("Dr. Achieng")
p3 = Patient("Kevin")
doc2.add_patient(p3)

print(f"{doc2.name} is treating: {[p.name for p in doc2.patients]}")
print(f"{hospital.name} has rooms: {hospital.rooms}")





            #MANY-TO-MANY
# many objects in class A relate to many in class B
# 🔍 Real-World Scenario
# A Patient can receive many treatments (e.g. chemotherapy, surgery, physiotherapy).

# A Treatment can apply to many patients.

# We need a bidirectional relationship that updates from one place (SSOT).

# 🧠 Design Choice
# We'll make Patient the SSOT, so:

# Patient keeps a list of Treatments.

# When a Treatment is added to a Patient, it also adds the Patient to itself.

class Treatment:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient instances allowed")
        if patient not in self.patients:
            self.patients.append(patient)

    def __repr__(self):
        return f"Treatment({self.name})"


class Patient:
    def __init__(self, name):
        self.name = name
        self.treatments = []

    def add_treatment(self, treatment):
        if not isinstance(treatment, Treatment):
            raise TypeError("Only Treatment instances allowed")
        if treatment not in self.treatments:
            self.treatments.append(treatment)
            treatment.add_patient(self)  # Mirror the relationship

    def __repr__(self):
        return f"Patient({self.name})"
    
# ✅ Test the Relationship

# Create treatments
t1 = Treatment("Chemotherapy")
t2 = Treatment("Physiotherapy")

# Create patients
p1 = Patient("Dennis")
p2 = Patient("Brenda")

# Add treatments
p1.add_treatment(t1)
p1.add_treatment(t2)

p2.add_treatment(t1)

# Inspect results
print(f"{p1.name}'s treatments:", p1.treatments)  # [Chemo, Physio]
print(f"{p2.name}'s treatments:", p2.treatments)  # [Chemo]

print(f"{t1.name} patients:", [p.name for p in t1.patients])  # [Dennis, Brenda]
print(f"{t2.name} patients:", [p.name for p in t2.patients])  # [Dennis]

# ✅ Visual Summary
# Entity 1	↔	Entity 2	Relationship	SSOT
# Patient	↔	Treatment	Many-to-Many	Patient
