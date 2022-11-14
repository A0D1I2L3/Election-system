from InquirerPy import prompt

options=[
    {
        "type": "list",
        "name": "Candidates",
        "message": "Select the candidate ",
        "choices": ['Jeff Bezzos','Warren Buffet',"Elon musk"]
        
    }

]
data = prompt(options)