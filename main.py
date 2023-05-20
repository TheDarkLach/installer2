import json
import platform
import requests
import patoolib
import os

# Define the URL for the direct download link
url = "https://www.dropbox.com/s/48bz45xi1kafx0k/MBL.rar?dl=1"

if platform.system() == "Windows":
    destination_dir = os.path.expanduser("~\\AppData\\Roaming\\.minecraft\\versions")
    launcher_profiles_path = os.path.expanduser("~\\AppData\\Roaming\\.minecraft\\launcher_profiles.json")
elif platform.system() == "Darwin":
    destination_dir = os.path.expanduser("~/Library/Application Support/minecraft/versions")
    launcher_profiles_path = os.path.expanduser("~/Library/Application Support/minecraft/launcher_profiles.json")
else:
    print("Unsupported operating system.")
    exit(1)


# Send a GET request to download the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Define the path for the downloaded file
    rar_path = os.path.join(destination_dir, "mbl.rar")

    # Save the file to the destination path
    with open(rar_path, "wb") as file:
        file.write(response.content)

    # Extract the contents of the downloaded RAR file
    patoolib.extract_archive(rar_path, outdir=destination_dir)

    # Remove the downloaded RAR file
    os.remove(rar_path)

    with open(launcher_profiles_path, "r+") as file:
        launcher_profiles = json.load(file)

        # Define the client entry
        client_entry = {
            "name": "MBL1.19.2",
            "type": "custom",
            "created": "2023-05-17T00:32:16.770Z",
            "lastUsed": "2023-05-17T00:32:17.770Z",
            "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAACXBIWXMAAA7DAAAOwwHHb6hkAAADAFBMVEVHcEzn6Ozv5+gAGoT7///h5fDdCw8GJIn///9nHR9/jsL29/rdCg7+9/f////////fGx/19fcMKYyAj8MAE4AAFoLqamxgc7TuiIruhojviozw7+8KJ4t6isHcBAkAG4QNKozcBwwAHYUFIohYbLAAGYPj5vHw8vjh5PDdDRH+/v7dDxP9+/z39fXdCxDeFxv////39fXuhIbfGR3////w6Onv5+fu5OT4+Pj///3bAAHX2d/7+/sAAiSdqNDcBAjn6Ozn6O18i8Hm6Ov////gICTo09QAFID+/f3tiYviCAriwsP7+/kAE4D8/P3fGh77///5+Pjzqqz29vbyhobDJjf////6///+/PwgNZD///5BWKXXgo7///////7////qZ2p+jcF6h73///////z///zm5ujU1t3+///j5Oj9///8///9///AyOHx6en8/////v1/jsL0trfoX2JdcLLMztVhdLT29/pidbXt7vLqbG779PVhc7T19voKJ4v////+/v7fGBwTL5DfGx/++/vfGh7wXmD+/f3eFxvcBwwNKoz6+/wIJooNKYzfHCAAFoL+/PwAFYEOKo0LKIv8/f37+/3cBwsOK40AGIP9/f7cBQkCIIfbAAH++vreFRndCQ3dDBDeExffHSEAGoTeERUEIYgMKIsBH4YOKozoWl39/v7qaWyJl8f3w8T6+/3yp6ngJSn52drxoKKUoczsd3qSn8sgO5YdOJURLY/98fHvi43kQkXaAADwX2LwXmHwXWD39/v5+vwrRJolPpf7/P0xSZ1ygrx+jcI4UKF4iL+8xN+Om8nrcnXqbW+DksTtfX85UKHtgoVsfbnuiIr63+Dvj5DyoqQADn3rdXdmeLb99/fwlJZfcrPjNjr99fXvjY/hLTD1t7j3qqtecbPzlJbvkpSMmsnnVVj74+TfGR3/7e1GXKf09fr/9PTV2uvn6vOmstzc4O7/pKXdDxS0v+NKYKztg4b/rK3xm51SZ7D0c3UAG4TdDhL1d3oACXvdCw8QfaBqAAAAfnRSTlMAX1/+1P39/jYB/Hv+e/p7/gL+/P7++vr8/PwB/v77/v78/v76/v36/f17/XuJ/P4Dbvv78WFeNIC5/hTEAvr9YUv8Xun7GvsD/P4SX/v6/mik+1L8/rVf+v7J+vyt6qH5/PzlJikOC5sjwdHE+k/S2/j6+voQ+n36aPp9+nt4cUFkAAAClElEQVQ4y3XTZVgUQRgH8FEUwTgaBCVEEAO7sbu7u7u7971197xdOG6PEzilS1KUkFTs7u7u7u6ZvfV47pD/s89+md/O7Mz7DkI2qF2njl3KGFJWSovmLRFJNdSmLZSS+qJAraF9Z7uKJHZ2k1wnjx3ay8WlqrOzc5N0aIx6IjQEvOzdzXC8zRzsPW1HDevt5+cXVhmnwf2uffAE4z720HoE4ujCX7x+9+ZlQea9O2m3OEZhHdvt1QiEZkz55m6ronAC4x8YVr8RzdAN1W5fZiI01Se3ZnVKD25CyOZUpUZzHS7xDM1Z1/g1GyGLWusriOOU/6ZrECzHn8sj4UIoQ9MDzIvmYFC7GJyHgxI4F6amaYX5nnKWyKJ8MTgsARbOhDEcBruNQLJwzAB2kCUU5huMgFY4AiEi0MBJviRQaYNOwzYJnPoPoHRBWyFABEpIi1FzJUCykAMBoAcpERzNlfyHE4YZ0lMyop6ZAkp1XL8LTAAyM2IZY7BxS24wiONyOWiU8OSD2hQc2EvGRIFTsDOhjjEI379PPwNIhxVdzwQcCiHfYkReLHzmjUFi0lG5BJQsq7z91HSJxKSzAZAq7QHnUYxaXyxDuVX5edlkn0q4mHW58OpdvE2x3P8aRkUFXnEl1WJhewTPR0fhoy5aYImm+eRJLafSCWIxMEiIY8SW+z4XoenjP3nqm5bSBj0mxWAhK0ZB0zSndns/Abf98Lf9dB7+JPk/skm9Wfj6E8/AxEU1fT4Qg74wxt7bwUEQhPjfOWSJSCjc9SeU5/kOD5t1x8ByNCxautzJyWntSq95sv4y2UjZ4iWrHR0dJw6GVqgRvtyzFpZ2eQeJd9cGLVu1opKYdb5Wda3w41uFZM18cvf/Asfnq25DJkeyAAAAAElFTkSuQmCC",
            "lastVersionId": "MBL1.19.2"
        }
        launcher_profiles["profiles"]["MBL1.19.2"] = client_entry
        launcher_profiles["selectedProfile"] = "MBL1.19.2"


        # Write the updated JSON back to the file
        file.seek(0)
        json.dump(launcher_profiles, file, indent=4)
        file.truncate()

        print("File downloaded and extracted successfully!")

        input("Press Enter to exit...")
else:
    print("Failed to download the file.")
    input("Press Enter to exit...")