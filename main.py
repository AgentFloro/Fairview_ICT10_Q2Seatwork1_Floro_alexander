from pyscript import document, display


def CheckNum(e):
    name = ["alexander floro", "cameron bufford", "isaias berdin", "angelo gloria", "hans arada"]

    name1 = document.getElementById("FirstName").value

    name2 = document.getElementById("Lastname").value
    

    Full = (f'{name1.lower()} {name2.lower()}')
   
    comfirm = Full in name

    message = (f'sorry {Full}, youre not part of the kalimbayan. and probably never will be.', f'Yay! {Full}, You are part of the Kalimbayan.')

    document.getElementById("output1").innerHTML = message[comfirm]

    