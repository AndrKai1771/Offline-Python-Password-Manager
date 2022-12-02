from time import sleep
import password_algorithms as pass_algs
import pyperclip as pc

# print('''
#             |====
#             |    \\  
#             |    /
#             |====
#             |
#             |
#             |
# ''')
print("********************************")
print("\tPASSWORD MANAGER")
print("********************************")
while True:
    #print("-----------------------------------------------\n|S.No|\t|Option|\n-----------------------------------------------")
    print("\n\n\n\n*******************************\nS.No\tOption\n*******************************")
    option = input("[-] 1\tAdd A New Password\n[-] 2\tUpdate Password\n[-] 3\tDelete Pasword\n[-] 4\tView All Passwords\n[-] 5\tExit\n''''''''''''''''''''''''''''''''\nPlease Choose Any Option From Above(1-5): ")

    if option.isdigit() == True:
        option = int(option)

        if option in range(1,6):

            if option in range(1,4):
                print()

                site = input("Enter The Website: ").lower()
                uname = input("Enter Username: ")
                print()
                # print('===========================')
                state = pass_algs.verifier(site,uname)

                if option == 1:

                    if state == True:
                        print("Password For This Username On This Site Already Exits!\nTry Updating Or Deleting It")
                    
                    else:
                        pw = pass_algs.pass_generator()
                        #print("-------------------------------------------------------\nA New Strong Password For Your Account => ",pw,"\n-------------------------------------------------------")
                        print("A New Strong Password For Your Account => ",pw)
                        add = pass_algs.adder(site, uname, pw)
                        print(add)

                        pc.copy(pw)
                        print('Password Copied To Clipboard')
                        sleep(2)

                elif option == 2:
                    
                    if state == True:
                        pw = pass_algs.pass_generator()
                        retrieved_pass = pass_algs.pass_retriever(site, uname)
                        prompt = input("The Password For '{}' is : {}\nAre You Sure That You Want To Update(Y/N): ".format(uname,retrieved_pass))

                        if prompt.upper() == 'Y' or prompt=='thik vro':
                            updated = pass_algs.updater(site, uname, pw)
                            print("\nPassword Updated\nThe New Password For '{0}' is '{1}'".format(uname,pw))

                            pc.copy(pw)
                            print("Password Coiped To Clipboard")

                        else:
                            print("Password Not Updated.\n")
                    
                    else:
                        print("Any Password For This User Does Not Exist In Database!!!\n")
                
                elif option == 3:

                    if state == True:

                        retrieved_pass = pass_algs.pass_retriever(site, uname)

                        prompt = input("The Password For '{}' is :{}\nAre You Sure That You Want To Delete(Y/N): ".format(uname,retrieved_pass))
                        if prompt.upper() == 'Y':
                            pass_algs.deleter(site, uname)
                            print("User Deleted Successfully")

                        else:
                            print("User Not Deleted.")

                    else:
                        print("User Does Not Exist For This Site.")
            
            elif option == 4:

                pass_algs.data_retriever()          

            elif option == 5:

                print('\nThanks For Using Our Program\nMade By Abdul Aleem Sarfaraz And Bhavya Bhatt Of Class 12-A\nSpecial Thanks To Aditya Pandey And Aviral Chaudhary\n')
                break

            else:
                print("Please Enter Correct Option!!!")

        else:
            print("Please Enter Correct Option!!!")

    elif option == 'Delete Everything':

        confirmation = input('Are You Sure?(Y/N): ')
        if confirmation == 'Sike':
           print(pass_algs.admin_command())

    else:
        print("Please Enter Correct Option!!!")

    sleep(2)
