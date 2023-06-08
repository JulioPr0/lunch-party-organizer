menu_item = "pizza"
guests = 10

print("Welcome to the Party Organizer!")
print("Menu item:", menu_item)
print("Number of guests:", guests)

menu_item = "biryani"

print("Updated menu item is:", menu_item)

biryani_per_person = 1
biryani_needed = biryani_per_person * guests
biryani_prepared = 10

enough_biryani = biryani_prepared >= biryani_needed

print("Biryani per person:", biryani_per_person)
print("Biryani needed:", biryani_needed)
print("Biryani prepared:", biryani_prepared)
print("Enough biryani for all guests?", enough_biryani)

guests += 1

biryani_per_guest = biryani_prepared / guests
print("Biryani per guest:", biryani_per_guest)

guests = 11
biryani_needed = biryani_per_person * guests

print("Updated number of guests:", guests)
print("Updated biryani needed:", biryani_needed)

additional_menu_item = "sushi"
additional_guests = 5

total_guests = guests + additional_guests
total_menu_items = [menu_item, additional_menu_item]

print("Total guests:", total_guests)
print("Total menu items:", ", ".join(total_menu_items))

print("Thank you for using the Party Organizer. Enjoy your event!")
