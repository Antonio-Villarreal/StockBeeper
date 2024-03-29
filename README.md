# StockBeeper

**Initially developed it with Cryptocurrency in mind and began experimenting with a first Cryptocurrency option, but I focused more on the Stock option during this second attempt of the project.

Entry 1- August 2021 : Began developing the initial demo of the product with very simple, rudamentary concepts to test if the idea could work. Focused on accessing the stock data and displaying that through a frontend. Program lacked the whole text notification system. The program is able to take in a ticker symbol input from the user and display the current price of that stock which allows the user to determine what limits they want to set. The limit lists are sorted so that the closest one to the current value is at the top of the list and displayed at the top of the list. In addition, you can type in new Ticker symbols to overwrite/delete old progress so that you ca work with a new stock.

Walkthrough of Entry 1:

<img src='http://g.recordit.co/RnSAVcPXQY.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />

<hr>

Entry 2 - August 2021: Developed the notification system and test it with closed market conditions where the price of the stock would remain constant. I am able to add at least a single limit and get notified when the stock reaches that limit. When a line prints in the notification center of the frontend the code before sends the text notification being sent to my personal cellular device.

Walkthrough of Entry 2:

<img src='http://g.recordit.co/x9htOPDY4v.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />

Below is the code I use to send the 'text notification' to my device. In reality since I have not found a free option in Python to text another phone I utilize my email and email my phone number which still sends a text notification to my device (I concealed my login information to protect my email's security):

![image](https://user-images.githubusercontent.com/73606672/130324767-2749213c-fb70-44c7-8ef2-2a6f6bf5eae0.png)

Below is a screenshot from my iPhone which shows what the limit notification looks like from the other end:

<p align="center">
<img src='https://user-images.githubusercontent.com/73606672/130324880-d94e61df-5163-4d83-a045-0878e6faf897.png'  width='450' alt='' />
<p/>

<hr>

Entry 3 - September 2021: Completed a second practice test on my Stock Beeper executable during open market conditions and the system printed the notification to the dashboard and still notified my phone so I have confirmed that the code does indeed work for a single stock and for one notification in open market. Note I am still having issues with the code detecting an open or closed market and that is a problem that I have to solve.

<img src='http://g.recordit.co/BwB6soM7Mm.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />

Entry 4 - July 2022: Containerized the previous program and practiced deploying container with free Microsoft Azure credits on ACR (Playing with Docker)

https://www.youtube.com/watch?v=0UG2x2iWerk&t=200s    

Practiced deploying container with free Microsoft Azure credits on ACR   

https://docs.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-acr   

https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli

