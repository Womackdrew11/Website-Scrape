# Website-Scrape


<>This program is designed to take websites with the specific disgn and scrape the article out of them.
I decided to format mine to scrape articles from a website that reviews anime episodes.
The software will go to each url in the "websites.txt" file and download the content from them.
It will only download and save the raw articles with a small amoint of information at the bottom.
The program will create seperate text files for each website visited.
if you intend to take this program and use it for yourself you will have to change some parameters based off of the website structure you are wanting to scrape.
The sites I chose all have the articles locate under the "div class='KonaBody'" tag. I had to pull all "p" tags under that tag to get the raw article without the extra nonsense likes ads and images.


<>I also have the attatched enviorment that I use to run the program.
The enviorment have the packages "BeautiifulSoap" and "requests" installed because they are needed for the program to run.
Download the enviorment and import it using the command line.
Run the program through the command line using the "python My_News_Downloader.py webssites.txt" command.
