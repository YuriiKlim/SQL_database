CREATE TABLE STUDENT(
	ID INT PRIMARY,--ПЕРВИННИЙ КЛЮЧ(ІДЕНТИФІКАТОР)
	FIRST_NAME VARCHAR(20) NOT NULL, -- НЕ МОЖЕ БУТИ ПОРОЖНІМ
	LAST_NAME VARCHAR(20) NOT NULL, -- НЕ МОЖЕ БУТИ ПОРОЖНІМ
	AGE INT,
	CHECK(AGE>0)
)