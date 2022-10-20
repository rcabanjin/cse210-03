#Start with a main function
def main():
        #Print the display for a 5 letter word
        print('- - - - -')
        #Start the display class
        class Display():
            #Create a board for the parachute and the man
            board = {
                    1: '', 
                    2: '', 3: '', 
                    4: '', 
                    5: '', 6: '',
                    7: '', 8: '',
                    9: '',
                    10: '', 11: '', 12: '',
                    13: '', 14: ''

            }    
        #Coding the parachute and the man
            def display_parachute(parachute):
                print(parachute[1] +  ' ' +  '__________')
                print(parachute[2] + '/' +  parachute [3] + '________' + parachute[4] +'\x5c')
                print(parachute [5] + '\x5c' + parachute[6] + '         /')
                print(parachute [7] + ' \x5c' + parachute[8] + '       /')
                print(parachute [9] + '     O')
                print(parachute [10] + '   /' + parachute[11] + '|' + parachute[12] + '\x5c')
                print(parachute[13] + '    /' + parachute[14] + '\x5c')
                return
            print(display_parachute)

            parachute_man =[' '] * 15
            display_parachute(parachute_man)


#Code a call to main from the beginning of the program
if __name__ == "__main__":
    main()