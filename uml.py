
from graphviz import Digraph

# Create a Use Case Diagram
use_case = Digraph('Use Case Diagram', format='png')
use_case.attr(size='8')

# Actors
use_case.node('Admin', shape='actor')
use_case.node('Hospital/Diagnostic Center', shape='actor')
use_case.node('Patient', shape='actor')

# Use Cases
use_case.node('UC1', 'Add Hospital/Diagnostic Center', shape='ellipse')
use_case.node('UC2', 'Upload Medical Records', shape='ellipse')
use_case.node('UC3', 'View Medical Records', shape='ellipse')
use_case.node('UC4', 'Approve Access via OTP', shape='ellipse')
use_case.node('UC5', 'Locate Nearby Hospitals', shape='ellipse')
use_case.node('UC6', 'Disease Analysis', shape='ellipse')

# Relationships
use_case.edge('Admin', 'UC1')
use_case.edge('Hospital/Diagnostic Center', 'UC2')
use_case.edge('Hospital/Diagnostic Center', 'UC3', label="(With OTP)")
use_case.edge('Patient', 'UC3')
use_case.edge('Patient', 'UC4')
use_case.edge('Patient', 'UC5')
use_case.edge('Admin', 'UC6')

# Render the diagram
use_case_path = "use_case_diagram.png"
use_case.render(use_case_path, format="png", cleanup=True)
print(use_case_path)

# Create a Class Diagram
class_diagram = Digraph('Class Diagram', format='png')
class_diagram.attr(size='10')# Create a Sequence Diagram
sequence_diagram = Digraph('Sequence Diagram', format='png')
sequence_diagram.attr(size='10')

# Entities
sequence_diagram.node('P', 'Patient', shape='rectangle')
sequence_diagram.node('H', 'Hospital', shape='rectangle')
sequence_diagram.node('S', 'System', shape='rectangle')
sequence_diagram.node('DB', 'Database', shape='rectangle')

# Interactions
sequence_diagram.edge('H', 'P', 'Request access to medical record')
sequence_diagram.edge('P', 'S', 'Verify OTP & Approve Access')
sequence_diagram.edge('S', 'DB', 'Fetch medical record')
sequence_diagram.edge('DB', 'S', 'Return medical record')
sequence_diagram.edge('S', 'H', 'Grant access to medical record')

# Render the diagram
sequence_diagram_path = "sequence_diagram.png"
sequence_diagram.render(sequence_diagram_path, format="png", cleanup=True)
print(sequence_diagram_path)


# Classes
class_diagram.node('Admin', '''Admin
--------------------
+ addHospital()
+ analyzeDiseases()
''', shape='record')

class_diagram.node('Hospital', '''Hospital/Diagnostic Center
--------------------
+ uploadMedicalRecords()
+ viewMedicalRecords()
+ requestAccess(patientID)
''', shape='record')

class_diagram.node('Patient', '''Patient
--------------------
+ viewMedicalRecords()
+ approveAccess(OTP)
+ locateNearbyHospitals()
''', shape='record')

class_diagram.node('MedicalRecord', '''MedicalRecord
--------------------
+ recordID
+ patientID
+ doctorID
+ scanReports
+ prescriptions
''', shape='record')

# Relationships
class_diagram.edge('Admin', 'Hospital', label='Manages')
class_diagram.edge('Hospital', 'MedicalRecord', label='Uploads/Views')
class_diagram.edge('Patient', 'MedicalRecord', label='Views')
class_diagram.edge('Patient', 'Hospital', label='Grants OTP Access')

# Render the diagram
class_diagram_path = "class_diagram.png"
class_diagram.render(class_diagram_path, format="png", cleanup=True)
print(class_diagram_path)
