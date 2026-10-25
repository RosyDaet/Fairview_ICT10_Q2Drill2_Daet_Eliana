
from pyscript import document

# ICT club members by grade
grade_7 = {"Julian Ante", "Kendra Saludar", "Francis Fernandez", "Gavin Ruiz"}

grade_8 = {"Vihaan Master", "Sebastian Fernandez", "Peter Reyes"}

grade_9 = {"Anthony Aggarao", "Nico Crispino", "Janna Planas", "Khiane Herrera", "Algena Cabling", "Alexei Janayan"}

grade_10 = {"Edrian Correa", "Philip Ponce", "Julian Anaque", "Andrik David", "Alexander Floro", "Annika De Vera", "Eliana Daet"}

# Combine all grade sets
fullmembers = grade_7 | grade_8 | grade_9 | grade_10


def check_members(event):
    # Get the first and last names
    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()

    # Combine the names
    full_name = first_name + " " + last_name

    # Add the new member
    fullmembers.add(full_name)

    # Create the results message
    message = f"ALL MEMBERS:\n{chr(10).join(sorted(fullmembers))}\nTOTAL MEMBERS: {len(fullmembers)}"

    # Display the results
    document.getElementById("List").innerHTML = message
