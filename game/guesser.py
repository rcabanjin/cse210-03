

class Guesser():
    """Get text input and display text output.
    
    Attributes:
        prompt (string): The prompt to display on each line.
    """
     
    def read(self, prompt):

        return input(prompt)

    def read_letter(self, prompt):

        return float(input(prompt))
        
    def write(self, text):

        print(text)
