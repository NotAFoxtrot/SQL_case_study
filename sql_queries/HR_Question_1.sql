select person.firstname, person.lastname, employee.jobtitle, emailaddress.emailaddress, employee.vacationhours
from person.person
join humanresources.employee
	on person.businessentityid = employee.businessentityid
join person.emailaddress
	on emailaddress.businessentityid = employee.businessentityid
where employee.vacationhours > 40;
--created report that holds: 
    -- firstname
    -- lastname
    -- the position in the company
    -- the email address
    -- how many vacation hours they have (currently limited at 40 but can be changed in the future)
-- joined the employee table and email address table into the person table to gather all relevant information
-- applied the limit of 40 at the end for vacation hours
