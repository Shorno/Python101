def attendance_status():
    n = int(input("Enter the total number of attendees: "))
    attendees = list(map(int, input("Enter the attendee IDs, separated by spaces: ").split()))
    m = int(input("Enter the total number of attendees who attended the conference: "))
    attended = list(
        map(int, input("Enter the IDs of attendees who attended the conference, separated by spaces: ").split()))

    attendance = {}

    for attendee in attendees:
        if attendee in attended:
            attendance[attendee] = 'Attended'
        else:
            attendance[attendee] = 'Did not attend'
    total_attendance = {'Attended': 0, 'Did not attend': 0}

    for status in attendance.values():
        total_attendance[status] += 1

    print(attendance)

    print(total_attendance)


attendance_status()
