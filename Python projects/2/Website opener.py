import webbrowser

while True:
     guess = input('What do you want to open?(Neave/Github/Scratch/Youtube/Poki/Google)')
     if guess == 'Neave':
          webbrowser.open('https://neave.com')
     elif guess == 'Github':
          webbrowser.open('https://in.search.yahoo.com/search?fr=mcafee&type=E210IN885G0&p=github')
     elif guess == 'Scratch':
          webbrowser.open('https://scratch.mit.edu/')
     elif guess == 'Youtube':
          webbrowser.open('https://www.youtube.com')
     elif guess == 'Poki':
          webbrowser.open('https://poki.com')
     elif guess == 'Google':
          webbrowser.open('https://www.google.com')
     else:
          print('Enter a browser in the list and type the first letter in capital letters' )
     
    
