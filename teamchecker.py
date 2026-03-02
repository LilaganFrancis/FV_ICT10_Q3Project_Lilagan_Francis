registered = True
medical = True

grade = int(input("Enter Grade (7-10): "))
section = input("Enter Section (Ruby, Sapphire, Topaz, Emerald): ")

if registered and medical and 7 <= grade <= 10:

    if section == "Ruby":
        team = "Green Hornets"
        image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0IdCpkC230nyUhZkTbkthRzcpgKkbsy7rrw&s"

    elif section == "Sapphire":
        team = "Yellow Tigers"
        image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhw3JPsDQtqY1MYcLaNF9BjnUzRL4Zs0jwlg&s"

    elif section == "Topaz":
        team = "Blue Bears"
        image = "https://i.pinimg.com/564x/b8/4f/41/b84f41c4183f70700a4a8107372b5ce3.jpg"

    elif section == "Emerald":
        team = "Red Bulldogs"
        image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThivE4zRM0ToaqkwIYKMXZj4kSait2XaYxxQ&s"

    else:
        team = "No Team"
        image = ""

    print("Team:", team)
    print("Image link:", image)

else:
    print("Not eligible.")