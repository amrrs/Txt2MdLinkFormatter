# Txt2MdLinkFormatter
Python code to identify links/URL from a text file and Format it as required in Markdown to have inline Hyperlink

**How this works:**

* Read the input Text file line by line
* Extracting required URLs using *Regex* (also eliminating that are already in Markdown compatible format)
* Using *BeautifulSoup* to scrape the URL *Title* and returning the string in Markdown compatible format
* Writing the source content (that doesn't requires processing as it is) and Markdown compatible format where the URL is processed

*README.md* Markdown of [this repo](https://github.com/amrrs/For-Data-Science-Beginners) has been created with this code! 
