# Txt2MdLinkFormatter
Python code to identify links/URL from a text file and Format it as required in Markdown to have inline Hyperlink

**How this works:**

* Read the input Text file line by line
* Extracting required URLs using *Regex* (also eliminating that are already in Markdown compatible format)
* Using *BeautifulSoup* to scrape the URL *Title* and returning the string in Markdown compatible format
* Writing the source content (that doesn't requires processing as it is) and Markdown compatible format where the URL is processed

**Advantage:**

My *README.md* Markdown of [this repo](https://github.com/amrrs/For-Data-Science-Beginners) has been created with this code (which otherwise must have been done manually)

**Disadvantage**

The current code is a bit slow as it scrapes the entire website

**BottomLine**

Nevertheless, This code has released me from a boring manual task of adding [](), a few tab opens and Copy+paste

## Feel free to fork this and play with the code! 

