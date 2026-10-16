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

    is_member = full_name.casefold() in [
        member.casefold() for member in club_members
    ]
    # Chekcks if full name matches a club member
    if is_member:
        message = (
            f"Congratulations, {full_name}! "
            "You are part of the ICT Club."
        )
   # display of message if the person is not club member
    else:
        message = (
            f"Sorry, {full_name}. "
            "Your name is not on the club list."
        )

    document.querySelector("#List").innerText = message