# MLBTheShow-MarketHistory
Downloads a player's market history from theshownation.com 


To get started...
<ol>
  <li> Log in and browse to https://theshownation.com/mlb20/orders/completed_orders </li>
  <li> Open up developer tools in your browser (F12 on Windows) </li>
  <li> Click on the network tab of developer tools </li>
  <li> Scroll down and select the second page </li>
  <li>Right click on the request that says <strong> /completed_orders?page=2&</strong></li>
  <li> Select <strong> Copy > Copy as cURL (cmd) </strong> </li>
  <li> Navigate to https://curl.trillworks.com/ </li>
  <li> Paste the curl command into the window </li>
  <li> Copy the Python headers section. </li>
  <li> You only need the header information. Overwrite the headers in the code on line 68 and you will be good to go. This contains your authentication token and cookies </li>
  <li> Update the other variables on lines 82-85. You will need PostgreSQL installed. If you want to ignore the database part, put # in front of line #92 </li>
  <li> Run code! </li>


<img src="https://github.com/don-shaw/MLBTheShow-MarketHistory/blob/master/Images/sql.PNG" width="100%" height="30%">

<img src="https://github.com/don-shaw/MLBTheShow-MarketHistory/blob/master/Images/by%20day.PNG" width="100%" height="30%">
