/* Task 1 */
/* Query 1 */

/* Adding the Returned column in the Rental table */
ALTER TABLE RENTAL
ADD COLUMN Returned int;

/* Update the column with 1 for returned and 0 for no returned rentals */
UPDATE Rental
SET    Returned=1
Where  ReturnDate <> "NULL";

UPDATE Rental
SET    Returned=0
Where  ReturnDate = "NULL";

/* Update the Returned column with 1 for the rentals with payment date and 
0 for the ones without the payment date */

Update Rental
Set    Returned=0
Where  PaymentDate="NULL";

Update Rental
Set    Returned=1
Where  PaymentDate <> "NULL";


/* Query 2 */
CREATE VIEW vRentalInfo(OrderDate,StartDate,ReturnDate,TotalDays,VIN,Vehicle,Type,Category,
CustomerID,CustomerName,OrderAmount,RentalBalance)
AS SELECT   R.OrderDate,R.StartDate,R.ReturnDate,R.RentalType * R.Qty, V.VehicleID,V.Description,
            Case
            When V.Type= 1 Then 'Compact'
            When V.Type= 2 Then 'Medium'
            When V.Type= 3 Then 'Large'
            When V.Type= 4 Then 'SUV'
            When V.Type= 5 Then 'Truck'
            When V.Type= 6 Then 'VAN'
            END Type,
            Case
                When V.Category= 0 Then 'Basic'
                When V.Category= 1 Then 'Luxury'
            END Category,
            C.CustID,
            C.Name,
            R.TotalAmount,
            Case
            When R.PaymentDate='NULL'  Then R.TotalAmount
            When R.PaymentDate<>'NULL' Then 0
            END
FROM       Customer As C, Rental As R, Vehicle As V
Where      C.CustID = R.CustID AND R.VehicleID = V.VehicleID
Order By   R.StartDate asc;

/*Task 2 */
/* Requirement 1*/
Insert into CUSTOMER(Name,Phone)
VALUES ('Anamol','(214)565-0101');

/*Requirement 2*/
INSERT INTO VEHICLE VALUES('19VDE1F3XEE414444','Acura ILX', 2013, 1, 1);

/*Requirement 3*/
SELECT V.VehicleID as VIN, V.Description, V.Year
From VEHICLE as V, RENTAL as R
Where V.type = 1 AND V.Category = 1 AND ((CAST(R.StartDate as DATE) >= CAST('06/01/2019' as DATE)
and CAST(R.StartDate as Date) <= CAST('06/20/2019' as Date) OR (CAST(R.ReturnDate as DATE) >= CAST('06/01/2019' as DATE)
and CAST(R.ReturnDate as Date) <= CAST('06/20/2019' as Date)))AND R.VehicleID = V.VehicleID);


/* Requirement 4 */
Select Name, 
            CASE 
            When R.PaymentDate='NULL' Then  R.TotalAmount
            When R.PaymentDate<>'NULL' Then 0
            END Balance,
            R.VehicleID,C.CustID

From CUSTOMER AS C, RENTAL AS R,Vehicle AS V
Where C.CustID=R.CustID AND V.VehicleID=R.VehicleID AND C.Name= 'G. Clarkson' AND R.ReturnDate='11/15/2019' AND V.Description='Lexus IS 250C';

/*Update the returned attribute */
/* Update the Payment date to the returned date.*/
/*We have used the inputs the from the user to find the corresponding CustID and VehicleID for the given rental and used it to update the rental payment date 
attribute to the returned attribute to confirm the payment for the given rental */

Update Rental
Set    PaymentDate=ReturnDate
Where  CustID='210' AND ReturnDate='11/15/2019' AND VehicleID='JTHFF2C26F135BX45'


/* Requirement 5 - A*/
/* Case 1- Without any filters. Will list all the cutomers with the remaining balance*/
CREATE VIEW CustomerView1(CustID,Name,Balance)
AS SELECT   C.CustID,C.Name,SUM(R.TotalAmount)
From CUSTOMER AS C, RENTAL AS R
Where C.CustID=R.CustID AND R.PaymentDate='NULL' 
Group By C.CustID
Order By SUM(R.TotalAmount);

/*Case 2- With the filters. Searching for balance with the customerID*/
CREATE VIEW CustomerView2(CustID,Name,Balance)
AS SELECT   C.CustID,C.Name,SUM(R.TotalAmount)
From CUSTOMER AS C, RENTAL AS R
Where C.CustID=R.CustID AND R.PaymentDate='NULL' AND C.CustID='210'
Group By C.CustID;

/*Case 3- With the filters. Searching for balance with the customerName*/
CREATE VIEW CustomerView3(CustID,Name,Balance)
AS SELECT   C.CustID,C.Name,SUM(R.TotalAmount)
From CUSTOMER AS C, RENTAL AS R
Where C.CustID=R.CustID AND R.PaymentDate='NULL' AND C.Name='G. Clarkson'
Group By C.CustID;

/*Read This. The way to implement in the Python.
- C.CustID and C.Name are the inputs taken from the user.
- Create a button for Customer View
- In the new window, there should be 2 input fields.i.e. Name and Cust ID
- Take the inputs from the text fields and save it in local variable.
- Use if else.If both are empty use the first querry.
- Else { make another inner if/else - check for the custid first use the second one
else use the customer name and querry the third one.}
- Make sure use the $ sign and float with 2 decimal points while printing the output for the balance amount.

/* Requirement 5 - B*/
/*Read me
- Use the same approach like for the A. Use Float and $ for the Avg daily price.*/

/* Case 1- Without any filters. Will list all the Rental vehicles with the Average Daily Price*/
CREATE VIEW VehicleView1(VIN,Description,AVG_Daily_Price)
AS SELECT   V.VehicleID,V.Description,R.TotalAmount/(R.RentalType*R.Qty) As AVG_Daily_Price
From        Vehicle As V, Rental As R 
Where       V.VehicleID=R.VehicleID
Order By    AVG_Daily_Price;

/* Case 2- Without any filters. Will list Rental vehicles with the Average Daily Price for the given VehicleId*/
CREATE VIEW VehicleView2(VIN,Description,AVG_Daily_Price)
AS SELECT   V.VehicleID,V.Description,R.TotalAmount/(R.RentalType*R.Qty) As AVG_Daily_Price
From        Vehicle As V, Rental As R 
Where       V.VehicleID=R.VehicleID AND V.VehicleID = '19VDE1F3XEE414842';


/* Case 3- Without any filters. Will list Rental vehicles with the Average Daily Price for the given Vehicle Description*/
CREATE VIEW VehicleView2(VIN,Description,AVG_Daily_Price)
AS SELECT   V.VehicleID,V.Description,R.TotalAmount/(R.RentalType*R.Qty) As AVG_Daily_Price
From        Vehicle As V, Rental As R 
Where       V.VehicleID=R.VehicleID AND V.Description= 'Acura ILX';








