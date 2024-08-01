def main():
    num_participants = int(input("Enter the number of participants: "))
    
    for i in range(num_participants):
        print(f"\nEnter marks for Participant {i + 1}:")
        subject1 = float(input("  Subject 1 mark: "))
        subject2 = float(input("  Subject 2 mark: "))
        subject3 = float(input("  Subject 3 mark: "))
        
        average = (subject1 + subject2 + subject3) / 3
        
        if average >= 70:
            status = "Qualified"
        else:
            status = "Not Qualified"
        
        print(f"Participant {i + 1}: {status}")

if __name__ == "__main__":
    main()

