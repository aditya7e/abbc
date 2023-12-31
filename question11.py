def covid_self_test():
    print("COVID-19 Self Assessment")
    print("Answer the following questions with YES or NO.")

    fever = input("Do you have a fever? ").lower() == 'yes'
    cough = input("Do you have a persistent cough? ").lower() == 'yes'
    difficulty_breathing = input("Are you experiencing difficulty breathing? ").lower() == 'yes'
    fatigue = input("Do you feel unusually fatigued? ").lower() == 'yes'
    body_aches = input("Are you experiencing body aches? ").lower() == 'yes'
    sore_throat = input("Do you have a sore throat? ").lower() == 'yes'
    loss_of_taste_smell = input("Have you lost your sense of taste or smell? ").lower() == 'yes'
    congestion_runny_nose = input("Do you have congestion or a runny nose? ").lower() == 'yes'
    nausea_vomiting = input("Are you experiencing nausea or vomiting? ").lower() == 'yes'
    diarrhea = input("Do you have diarrhea? ").lower() == 'yes'

    # Check if any of the symptoms are present
    if (
        fever or cough or difficulty_breathing or fatigue or body_aches or sore_throat or
        loss_of_taste_smell or congestion_runny_nose or nausea_vomiting or diarrhea
    ):
        print("\nBased on your symptoms, it is recommended to consult with a healthcare professional and consider getting a COVID-19 test.")
    else:
        print("\nYour symptoms do not necessarily indicate COVID-19, but it's important to monitor your health.")

if __name__ == "__main__":
    covid_self_test()
