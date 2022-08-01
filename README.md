# WEEKLY (AKA ValleySum)

The Python script is one I wrote for the Nutrition team at TRPDD. One of the team's responsibilities is tracking meals with their various categories
throughout the meal sites. One of the largest categories is Frozen meals, with those numbers coming from a .csv (that file being read using Excel).
This script categorically summarizes the data, with a start date and a last date to the right (based on the least and most recent date found on the file).

The hierarchy of the summary is FROZEN 5PK D2D (MW)/FROZEN 5PK D2D (STATE) > County > Status > DeliveryID (Totals) *

If you want to see an example of this output, look at Sum.xlsx. 
If you want to see a previous version's output that categorized by City instead of county, open OldSum.xlsx.

Below is the instructions that are on a Word doc that I left for the people that use this program.

* (There was a rewrite line to rename that column 'DeliveryID' to 'Totals', but I deleted it somewhere in the process.)  

Get Data
1.	Log on to http://customer.valleyservicesi.com/
2.	In the upper left corner, enter Delivery History for desired day/week/month (Ex. 7/12/2022, 7/19/2022), click "go" 
3.	Select "Export Data"
4.	After exporting data, open File Explorer and open the new file, or open the file location by right clicking on the download from your browser 
5.	Open the .csv file and rename Column L “County”, Column M “Agent”, and Column N “City”.
6. Press the “crtl” and “s” keys simultaneously to save the changes you’ve made.
Creating the Summary
6.	Double click ValleySum.exe to execute
7.	The program will open your downloads folder. Select the newly downloaded file.
8.	After running ValleySum, you should see a new file on your desktop named “Sum.xlsx”. 
9.	Double Click and rename file to time span (Ex. Weekof07042022, MonthofJuly2022, etc.)
