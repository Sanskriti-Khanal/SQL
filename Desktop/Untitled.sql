Create Database Class;
Use Class;

-- Create Fees table
CREATE TABLE Fees (
    Class_Id INT PRIMARY KEY,
    Class VARCHAR(255),
    Amount DECIMAL(10, 2)
);

-- Create Payment table
CREATE TABLE Payment (
    Payment_Id INT PRIMARY KEY,
    Student_Id INT,
    Amount DECIMAL(10, 2),
    Payment_Date DATE,
    FOREIGN KEY (Student_Id) REFERENCES Student(Student_Id)
);

-- Create Subject table
CREATE TABLE Subject (
    Subject_Id INT PRIMARY KEY,
    Subject VARCHAR(255)
);

-- Create Address table
CREATE TABLE Address (
    Address_Id INT PRIMARY KEY,
    Address VARCHAR(255),
    District VARCHAR(255),
    Province VARCHAR(255)
);

-- Create Teacher table
CREATE TABLE Teacher (
    Teacher_Id INT PRIMARY KEY,
    Name VARCHAR(255),
    DateOfBirth DATE,
    Gender VARCHAR(255),
    Address_Id INT,
    Phone VARCHAR(255),
    Salary DECIMAL(10, 2),
    FOREIGN KEY (Address_Id) REFERENCES Address(Address_Id)
);

-- Create Student table
CREATE TABLE Student (
    Student_Id INT PRIMARY KEY,
    Name VARCHAR(255),
    DateOfBirth DATE,
    Gender VARCHAR(255),
    Address_Id INT,
    FOREIGN KEY (Address_Id) REFERENCES Address(Address_Id)
);

-- Create Class_Subject table
CREATE TABLE Class_Subject (
    Class_Subject_Id INT PRIMARY KEY,
    Class_Id INT,
    Subject_Id INT,
    FOREIGN KEY (Class_Id) REFERENCES Fees(Class_Id),
    FOREIGN KEY (Subject_Id) REFERENCES Subject(Subject_Id)
);

-- Create Attendance table
CREATE TABLE Attendance (
    Attendance_Id INT PRIMARY KEY,
    Student_Id INT,
    Date DATE,
    Status VARCHAR(255),
    FOREIGN KEY (Student_Id) REFERENCES Student(Student_Id)
);

-- Create Result table
CREATE TABLE Result (
    Result_Id INT PRIMARY KEY,
    Student_Id INT,
    Subject_Id INT,
    Exam_Date DATE,
    Score INT,
    FOREIGN KEY (Student_Id) REFERENCES Student(Student_Id),
    FOREIGN KEY (Subject_Id) REFERENCES Subject(Subject_Id)
);

CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,
    EventName VARCHAR(50) NOT NULL,
    Date DATE NOT NULL,
    Location VARCHAR(100) NOT NULL
);


-- Create Library table
CREATE TABLE Library (
    Record_Id INT PRIMARY KEY,
    Student_Id INT,
    BookTitle VARCHAR(255),
    Author VARCHAR(255),
    Issue_Date DATE,
    Return_Date DATE,
    FOREIGN KEY (Student_Id) REFERENCES Student(Student_Id)
);


-- Insert data into Fees table
INSERT INTO Fees (Class_Id, Class, Amount) VALUES
    (1, 'Nursery', 1500),
    (2, 'KG', 2000),
    (3, '1', 2500),
    (4, '2', 3000),
    (5, '3', 3500),
    (6, '4', 4000),
    (7, '5', 4500),
    (8, '6', 5000),
    (9, '7', 5500),
    (10, '8', 6000),
    (11, '9', 6500),
    (12, '10', 7000);


INSERT INTO Payment (Payment_Id, Student_Id, Amount, Payment_Date) VALUES
    (1, 101, 5500, '2080-04-10'),
    (2, 102, 6500, '2080-04-10'),
    (3, 103, 5500, '2080-04-05');
    
    Select * from Payment;


INSERT INTO Subject (Subject_Id, Subject) VALUES
    (1, 'Mathematics'),
    (2, 'Science'),
    (3, 'English'),
    (4, 'Social Studies');

   Select * from Subject;

INSERT INTO Address (Address_Id, Address, District, Province) VALUES
    (1, 'Tansen-8', 'Palpa', 'Lumbini'),
    (2, 'Bhairahawa-1', 'Rupandehi', 'Lumbini'),
    (3, 'Butwal-12', 'Rupandehi', 'Lumbini'),
    (4, 'Taulihawa-5', 'Kapilvastu', 'Lumbini'),
    (5, 'Siddharthanagar-12', 'Bhairahawa', 'Lumbini');
    
       Select * from Address;


INSERT INTO Teacher (Teacher_Id, Name, DateOfBirth, Gender, Address_Id, Phone, Salary) VALUES
    (1, 'Ashok Aryal', '1980-09-05', 'Male', 1, '9867389098', 40000),
    (2, 'Basanta Poudel', '1975-04-25', 'Male', 2, '9876787887', 45000),
    (3, 'Lekhnath Panta', '1985-01-28', 'Male', 3, '9856788993', 60000),
    (4, 'Roman Shrestha', '1990-06-02', 'Male', 3, '9843678567', 55000),
    (5, 'Ritika Banjade', '1992-05-11', 'Female', 1, '9841678939', 50000);
    
   Select * from Teacher;
   

INSERT INTO Student (Student_Id, Name, DateOfBirth, Gender, Address_Id) VALUES
    (101, 'Ramesh Acharya', '2005-03-15', 'Male', 3),
    (102, 'Sita Sharma', '2006-06-20', 'Female', 4),
    (103, 'Asha Rai', '2004-11-10', 'Female', 5);
    
       Select * from Student;


INSERT INTO Class_Subject (Class_Subject_Id, Class_Id, Subject_Id) VALUES
    (1, 12, 1),
    (2, 12, 2),
    (3, 11, 3),
    (4, 11, 4);
    
       Select * from Class_Subject;


INSERT INTO Attendance (Attendance_Id, Student_Id, Date, Status) VALUES
    (1, 101, '2023-07-01', 'Present'),
    (2, 102, '2023-07-02', 'Absent'),
    (3, 103, '2023-07-03', 'Present'),
    (4, 102, '2023-07-02', 'Present'),
    (5, 103, '2023-07-03', 'Absent');
    
       Select * from Attendance;


INSERT INTO Result (Result_Id, Student_Id, Subject_Id, Exam_Date, Score) VALUES
    (1, 101, 1, '2023-06-15', 85),
    (2, 102, 2, '2023-06-20', 78),
    (3, 103, 3, '2023-06-25', 92),
    (4, 102, 4, '2023-06-15', 78),
    (5, 103, 3, '2023-06-20', 90),
    (6, 103, 1, '2023-06-25', 65);
    
        Select * from Result;
    
INSERT INTO Events (EventName, Date, Location) VALUES
('Annual Day', '2023-08-10', 'School Grounds'),
('Sports Day', '2023-09-20', 'Sports Complex'),
('Science Fair', '2023-10-15', 'Science Lab'),
('Parent-Teacher Meeting', '2023-07-30', 'School Auditorium');

 Select * from Events;


INSERT INTO Library (Record_Id, Student_Id, BookTitle, Author, Issue_Date, Return_Date) VALUES
    (1, 101, 'Java the complete reference (12th edition)', 'Herbert Schildt', '2023-07-05', '2023-07-20'),
    (2, 102, 'Spidering HACKS', 'Tara Calishain', '2023-06-30', '2023-07-10'),
    (3, 103, 'Windows System Programming', 'Johnson M. Hart', '2023-07-10', '2023-07-25'),
    (4, 103, 'C# in Depth', 'Jon Skeet', '2023-07-15', '2023-07-25');
    
     Select * from Result;
     
SET SQL_SAFE_UPDATES = 0;

UPDATE Fees
SET Amount = Amount * 1.20;

SET SQL_SAFE_UPDATES = 1;

Select * from Fees;

-- Creating a temporary table to store student IDs with over 10 consecutive absences
CREATE TEMPORARY TABLE TempAbsentStudents AS
SELECT Student_Id
FROM Attendance
WHERE Status = 'Absent'
GROUP BY Student_Id, YEAR(Date), MONTH(Date)
HAVING COUNT(*) > 10;

DELETE FROM Attendance
WHERE Student_Id IN (
    SELECT Student_Id
    FROM (
        SELECT 
            Student_Id,
            Date,
            Status,
            ROW_NUMBER() OVER (PARTITION BY Student_Id ORDER BY Date) AS row_no
        FROM Attendance
        WHERE Status = 'Absent'
    ) AS t
    WHERE t.Status = 'Absent'
    AND t.row_no > 10
);
Select * from Attendance;


INSERT INTO Student (Student_Id, Name, DateOfBirth, Gender, Address_Id)
VALUES (104, 'Gita Thapa', '2007-09-15', 'Female', 1);


INSERT INTO Payment (Payment_Id, Student_Id, Amount, Payment_Date)
VALUES (4, 104, 5500, '2080-04-15');

Select * from Student;
Select * from P;

SELECT 
    s.Student_Id,
    s.Name,
    sub.Subject,
    SUM(r.Score) AS Total_Marks,
    AVG(r.Score) AS Average_Marks,
    (SUM(r.Score) / (COUNT(DISTINCT sub.Subject) * 100)) * 100 AS Percentage
FROM 
    Result r
JOIN 
    Student s ON r.Student_Id = s.Student_Id
JOIN 
    Subject sub ON r.Subject_Id = sub.Subject_Id
GROUP BY 
    s.Student_Id, sub.Subject;

SET SQL_SAFE_UPDATES = 0;

START TRANSACTION;

UPDATE Result
SET Score = Score - 10;

COMMIT;

SET SQL_SAFE_UPDATES = 1;

Select * From Result;

-- Check data in tables
SELECT * FROM Student;
SELECT * FROM Attendance;
SELECT * FROM Result;
SELECT * FROM Subject;
SELECT * FROM Fees;
SELECT * FROM Teacher;

SELECT
    s.Name AS Student_Name,
    a.Date AS Attendance_Date,
    a.Status
FROM
    Student s
JOIN 
    Attendance a ON s.Student_Id = a.Student_Id
WHERE
    a.Status = 'Present';
    
    SELECT
    s.Name AS Student_Name,
    r.Score,
    sub.Subject
FROM
    Student s
JOIN 
    Result r ON s.Student_Id = r.Student_Id
JOIN 
    Subject sub ON r.Subject_Id = sub.Subject_Id
WHERE
    r.Score > 70;
    
SELECT
    s.Name AS Student_Name,
    f.Amount AS Fee_Amount
FROM
    Student s
JOIN 
    Fees f ON s.Student_Id = f.Class_Id;
    
    SELECT
    s.Name AS Student_Name,
    t.Name AS Teacher_Name,
    sub.Subject,
    r.Score
   
FROM
    Student s
JOIN 
    Attendance a ON s.Student_Id = a.Student_Id
JOIN 
    Result r ON s.Student_Id = r.Student_Id
JOIN 
    Subject sub ON r.Subject_Id = sub.Subject_Id
JOIN 
    Teacher t ON s.Address_Id = t.Address_Id
WHERE
    a.Status = 'Present'
    AND r.Score > 70
ORDER BY
    s.Name, sub.Subject
LIMIT 1000;









