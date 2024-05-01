**Steps to execute the code:**

`Use the below syntax to execute the code.`

`python gspann_code.py <paragraph_content> <page_width>`

**Example:** 

`python gspann_code.py "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works." 20`

**Expected output:** 
<pre>
Array [1] = "This  is a sample"
Array [2] = "text    but   a"
Array [3] = "complicated problem"
Array [4] = "to be solved, so we"
Array [5] = "are adding more text"
Array [6] = "to  see  that  it"
Array [7] = "actually   works."
</pre>


**In case any of the argument is missing, following output is expected:**

`Arguments Missing: Usage: python <file_name>.py <first_argument_paragraph> <second_argument_page_width>`


**If any of the word in paragraph exceeds the page_width, code is not supposed to break the word, so below output is expected:**

`Word length is greater than page_width. Erroneous input.`

