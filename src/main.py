from utils.json_storage import load_cv
from services.cv_manager import add_cv, filter_by_top_skills, update_cv, delete_cv, check_email_exists, input_email
from models.cv import CV 



def main():
    """
    Executes the CV Manager program loop
    """
    data = load_cv("../data/cvs.json")
    new_cv = None
    execute = True

    while execute:
        print(f"================ # Developed by Aymard - Phase 2 CV Manager. ==============="
              f"\n1. Add a new CV"
              f"\n2. Display all CVs"
              f"\n3. Search by top skill"
              f"\n4. Update a CV"
              f"\n5. Delete a CV"
              f"\n6. Exit")
        
        choice = input(f"Choose an option from the list below."
                      f"\Press 1 to Add a new CV."
                      f"\nPress 2 to Display all CVs" 
                      f"\netc.\nYour choice: ")

        if choice == "1":
            name = input("Enter Name: ").strip()
            adress = input("Enter address, city: ").strip()
            email = input("Enter email: ").strip().lower()
            phone = input("Enter phone number: ").strip()
            experience = input("Enter work experience (separated by commas): ").strip().split(',')
            skill = input("Enter skills (separated by commas): ").strip().split(',')
            education = input("Enter studies (separated by commas): ").strip().split(',')
            language = input("Enter languages (separated by commas): ").strip().split(',')
            hobbie = input("Enter hobbies (separated by commas): ").strip().split(',')
    
            new_cv = CV(name, adress, email, phone, experience, skill, education, language, hobbie)
            add_cv(new_cv, email)
            print(f"✅ Successfully added CV for: {name}.")
            data = load_cv("../data/cvs.json")
            

        elif choice == '2':
            for item in data:
                if item is None:
                    continue
                for key, value in item.items():
                    print(f"{key}: {value}")
                print(f"-" * 20)
                
        elif choice == '3':
            try:
                result = filter_by_top_skills()
            except NameError: 
                print(f"No CV selected or found. Please create a CV" 
                      f"\nfirst using option 1")
            if not result:
                print(f"No CVs found with top skills.")
            else:
                print(f"\n--- {len(result)} CV(s) Found ---")
                for cv in result:
                    for key, value in cv.items():
                        print(f"{key}: {value}")
                    print(f"-" * 20)

        elif choice == '4':
            email = input(f"Enter email: ")
            if not email:
                print(f"❌ Error: {email} field cannot be empty.")
                input_email() # Return input email
            else:
                name = input("Enter Name: ").strip()
                adress = input("Enter address, city: ").strip()
                email = input("Enter email: ").strip().lower()
                phone = input("Enter phone number: ").strip()
                experience = input("Enter work experience (separated by commas): ").strip().split(',')
                skill = input("Enter skills (separated by commas): ").strip().split(',')
                education = input("Enter studies (separated by commas): ").strip().split(',')
                language = input("Enter languages (separated by commas): ").strip().split(',')
                hobbie = input("Enter hobbies (separated by commas): ").strip().split(',')
                new_cv_to_dict = CV(name, adress, email, phone, experience, skill, education, language, hobbie)
                update_cv(new_cv_to_dict, email)
                print(f"✅ Successfully updated CV for: {name}.")
                data = load_cv("../data/cvs.json")

        elif choice == '5':
            email = input(f"Enter email: ")
            if not email:
                print(f"❌ Error: {email} field cannot be empty.")
                input_email() # Return input email
            
            else:
                delete_cv(email)
            print(f"✅ Successfully deleted CV with email: {email}.")
        
    
        elif choice == '6':
            break
        else: 
            print("🛑 Invalid option")

if __name__ == "__main__":
    main()