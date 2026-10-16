from pyscript import document

# List of ICT club members
club_members = [
    "Francis Fernandez",
    "Gavin Ruiz",
    "Edrian Correa",
    "Philip Ponce",
    "Julian Anaque",
    "Andrik David",
    "Alexander Floro",
    "Annika De Vera",
    "Eliana Daet",
    "Anthony Aggarao",
    "Nico Crispino",
    "Janna Planas",
    "Khiane Herrera",
    "Algena Cabling",
    "Alexei Janayan",
    "Vihaan Master",
    "Sebastian Fernandez",
    "Peter Reyes",
    "Julian Ante",
    "Kendra Saludar"  
]

grade_7 = []

grade_8 = []

grade_9 = []

grade_10 =


full_name.(add) =  
def check_member(event):
     # formula used to get the first name and last name 
    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()

    # Get the first name and last name from the input fields
    full_name = first_name + " " + last_name

   #checks if either name field is empty
    if not first_name or not last_name:
        document.querySelector("#List").innerText = (
            "Please enter both your first name and last name."
        )
        return

