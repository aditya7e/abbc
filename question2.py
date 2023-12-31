def count_altered_letters(sos_message):
    original_sos = "SOS"
    altered_count = 0

    for i in range(len(sos_message)):
        if sos_message[i] != original_sos[i % 3]:
            altered_count += 1

    return altered_count

received_message = input("Enter the Recieved Message: ")
changes = count_altered_letters(received_message)
print(f"The number of altered letters: {changes}")
