This program works with Re and pyperclip library.
This program works with US numbers in 123-123-1234 style, with this variations in the begging: (123) 123-1234; 123-1234. 
And this variations in the end: 123-123-1234 ext. 1234, 123-123-1234 ext 1234, 123-123-1234 x1234.

The program will save what is in your CTRL+C and filter this.
The output will be the numbers and e-mails filtered and save them in your CTRL+C.

The program can output in 2 differents styles:
1- number email
   number email
   ... 
2- number
   number
   ...
   email
   email
   ...
   
To change the style, change the:
   pyperclip.copy(results2)
in the last line to:
   pyperclip.copy(results1)
