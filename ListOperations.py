seats = []

for seat_number in range(1, 21):
    seats.append(seat_number)

selected_seat = -1

while selected_seat != 0:
    if len(seats) == 0:
        print("All seats have been sold.")
        break
    
    print("List of seats:", seats)

    selected_seat = int(input("Please enter select the seat number you would like (1-20) or enter 0 to finish your purchase: "))

    if selected_seat in seats:
        seats.pop(seats.index(selected_seat))
    elif selected_seat == 0:
        break
    else:
        print("Seat is not available, please choose a different one.")