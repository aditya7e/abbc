def calculate_attendence(Record,max_days):
  total_present_required = 0.75*max_days
  res = {}

  for rollno,values in Record.items():
    current_percentage = (sum(values)/len(values))*100
    required_additional_days = total_present_required-values.count(True)

    res.update({rollno:{'Current Percentage': current_percentage,
                        'Additonal Days Needed ':math.ceil(required_additional_days)}})
    
  return res


students = {
    101: [True, True, True, False, True],
    102: [True, True, False, True, True],
    103: [True, True, True, True, True],
    # Add more students as needed
}

max_days = int(input("Enter the maximum number of days: "))

res = calculate_attendence(students,max_days)

print(res)

