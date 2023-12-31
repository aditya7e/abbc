diseases = {
        'Cold': ['runny nose', 'sneezing', 'cough', 'sore throat'],
        'Flu': ['fever', 'body aches', 'fatigue', 'cough'],
        'COVID-19': ['fever', 'cough', 'shortness of breath', 'loss of taste or smell'],
        'Allergies': ['sneezing', 'itchy eyes', 'runny nose'],
    }

def identify_diseases(symptoms, diseases):
    possible_diseases = []
    for disease, disease_symptoms in diseases.items():
        if all(symptom in symptoms for symptom in disease_symptoms):
            possible_diseases.append(disease)

    return possible_diseases

def add_new_disease(diseases):
    new_disease = input("Enter the name of the new disease: ")
    new_symptoms = input("Enter the symptoms of the new disease (comma-separated): ").lower().split(',')
    diseases[new_disease] = new_symptoms
    print(f"\nNew disease '{new_disease}' added with symptoms: {', '.join(new_symptoms)}")



def main():
  

    while True:
        print("\nOptions:")
        print("1. Enter Symptoms to Identify Diseases")
        print("2. Add New Disease to Dictionary")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            print("\nEnter the symptoms you are experiencing (comma-separated):")
            user_input = input().lower().split(',')
            possible_diseases = identify_diseases(user_input, diseases)

            if possible_diseases:
                print("\nPossible diseases based on symptoms:")
                for disease in possible_diseases:
                    print(f"- {disease}")
            else:
                print("\nNo matching diseases found based on the given symptoms.")

        elif choice == '2':
            add_new_disease(diseases)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
