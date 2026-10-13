from pyscript import document, display


def CheckNum(e):
    name = ["alexander floro", "alexis floring", "5", "6", "9"]

    name1 = document.getElementById("FirstName").value

    name2 = document.getElementById("Lastname").value
    

    Full = (f'{name1.lower()} {name2.lower()}')
   
    comfirm = Full in name

    message = (f'sorry {Full}, your dreams is gone forever', f'Yay! {Full}, you is a ren worshipper.')

    document.getElementById("output1").innerHTML = message[comfirm]

    