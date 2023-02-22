# CIMS

## Clinic Information Management System

Clinic Information Management System (CIMS) is a fullstack web application, developed using python django. It enables clinic personnel and administrators to not only track patient records but also the doctors and nurses providing health care and treatment to the respective patients.

### Application Goal

To manage patient information and enable tracking of health care services

### Target Audience

* The system administrator who might want to add new personnel in the  CIMS application

* Doctors who might want to treat patients

* Pharmacists who might want to prescribe medicine to patients

* Laboratory technicians who might want to perform tests and diagnosis

* Receptionists who might want to enter patient records and make patient appointments

------

## Features

1. **The Navigation Bar**

* The navigation bar is responsive and is included on all four pages. It provides links to the Home page, Team page, Services page and the login page. It is the same on each page to facilitate easy navigation.

* This section allows users to simply go from page to page across all devices without having to use the ‘back’ button to return to the previous page.

* In addition, the navigation bar highlights the page the user is on in white.

![The Navigation Bar](cim_users/static/cim_users/navigationbar.PNG)

2. **The CIMS landing page**

* The landing or main Home page comprises an image of the services to help the viewer understand what this site is about and how it can be useful. In this case, the CIMS logo and the Home are both linked.


![The landing/home page](cim_users/static/cim_users/landingpage.PNG)

3. **The Footer**

* The footer section includes the copyright information of CIMS.

![The footer](cim_users/static/cim_users/footer.PNG)

3. **The Team page**

* The team page on the CIMS application shows the different persons on the team at the clinic or hospital. These include the doctors, laboratory technicians, receptionists and the pharmacists.

* The team page shown below is that of an unregistered user who is just browsing the site. These users can only view the members on the team but can not perform any actions.

![The team page](cim_users/static/cim_users/teampage1.PNG)

4. **The Services page**

* The services page contains a list of services offered in the CIMS application. These services include patient record management, making appointments, laboratory record management and pharmacy stock and record management.

* The service page below is the view for unregistered users. They can only view and read the services but can not perform any actions. One would be required to register and log in to CIMS to manage the services.

![The services page](cim_users/static/cim_users/servicespage1.PNG)

5. **The Login page**

* The login page for the CIMS application is where users may enter their credentials that is the username and password. The login feature is created for users who are already registered in the system. The page also contains a register link for new users to sign up on the application.

![The Login page](cim_users/static/cim_users/loginpage.PNG)

6. **Register**

* The register link helps new users to signup or create accounts in the CIMS application. The page allows new users to enter their usernames, passwords, emails as well as a field to confirm their passwords.

![The register link](cim_users/static/cim_users/register.PNG)

7.**The flash messages**

* On successful login, the user gets to view a dashboard which is different from the home page. This is one of the differences between the authorized and unauthroized users on the app. Only the authorized or registered users can view the CIMS dashboard.

* On successful login, the site also shows the user who is successfully logged in.

* The flash messages give the users an option to hide them through the close button.

![The successful login message](cim_users/static/cim_users/loginsuccess.PNG)

* When a user enters wrong credentials, that is to say non-existent usernames, the site returns a message that states credentials do not exist.

![The wronglogin credentials](cim_users/static/cim_users/credentials%20do%20not%20exist.PNG)

* When the user enters either an incorrect username or password, the system returns a flash message that reads wrong username or password.

![The wrongusernamepw credentials](cim_users/static/cim_users/wrongusernamepw.PNG)

* When a user tries to enter credentials that already exist in the system, the system returns a message stating Account already exists.

![The already existing credentials](cim_users/static/cim_users/accountalreadyexists.PNG)

* Likewise, when a user wants to log out of the system. The CIMS application returns the message you have logged out, goodbye!

![The logout](cim_users/static/cim_users/logoutmsg.PNG)

### The Dashboard for registered users

* The CIMS dashboard allows the users in the system not only to view but to manage the services on the application such as patients, appointments, diagnosis and medication whose data is stored in their respective custom models which are patient, appointment, diagnosis and medicine.

* The dashboard has arrows within each tab for easy navigation from one service to the next and back to the dashboard. The services on the service page are also linked to the corresponding models for easy management.

![The dashboard](cim_users/static/cim_users/dashboardafterlogin.PNG)

1. **Manage Patients**

* As a registered user, CIMS allows you to manage the patients. Within the patients tab, you can view, add, update and delete patients. You can also view the total number of patients within CIMS in this tab.

![cims patients](cim_users/static/cim_users/cimspatients.PNG)

![Viewing the patients](cim_users/static/cim_users/viewingpatients.PNG)

* The add functionality in manage patients allows users to add the full name, and the symptoms or ailments of the patient.

![The add patient](cim_users/static/cim_users/Addpatient.PNG)

* The update button allows users to update the name, and the ailment fields of the patients while the delete button allows users to delete patients from the CIMS application.

![The update and delete patient](cim_users/static/cim_users/updatepatient.PNG)

2.**Manage Appointments**

* CIMS allows authorized users to manage appointments within the app. Here users can view the existing appointments, add appointments, update and delete appointments.

![cims appointments](cim_users/static/cim_users/cimsappointments.PNG)

![viewing appointments](cim_users/static/cim_users/viewingappointments.PNG)

* The appointment model allows users to add fields like the patient name, select the doctor's  or specialists name and the time of visit when making an appointment.

![add appointment](cim_users/static/cim_users/addappointment.PNG)

* The appointment model also allows registered users to update the appointment fields. They can also choose to delete these appointments if they wish.

![update appointment](cim_users/static/cim_users/updateappointment.PNG)

3.**Manage Diagnosis**

* CIMS allows users to manage diagnosis within the app. Here users can view the existing diagnosis, add, update and delete diagnosis.

![cims diagnosis](cim_users/static/cim_users/cimsdiagnosis.PNG)

![viewing diagnosis](cim_users/static/cim_users/viewingdiagnosis.PNG)

* The diagnosis model allows the users to add fields like patient name, test name, and the diagnosis.

![add diagnosis](cim_users/static/cim_users/adddiagnosis.PNG)

* The diagnosis model further allows the users to upate the diagnosis of the different patients or delete them if they wish.

![update diagnosis](cim_users/static/cim_users/updatediagnosis.PNG)

4.**Manage Medication**

* CIMS allows authorized users to manage medicine or treatment within the app. Here users can view the existing treatments, add, update and delete prescriptions.

![cims pharmacy](cim_users/static/cim_users/cimspharmacy.PNG)

![Viewing prescriptions](cim_users/static/cim_users/viewingprescriptions.PNG)

* The medicine module allows users to add fields like the patient to whom the medicine is prescribed to, the medication and the stock when issuing a prescription.

![add prescription](cim_users/static/cim_users/addprescription.PNG)

* The medicine module also allows to update or delete the fields created.

![update prescription](cim_users/static/cim_users/updateprescription.PNG)

5.**Manage Team Members**

* CIMS app allows authorized users to view members, add, update and delete members from the app.

![manage members](cim_users/static/cim_users/managemembers.PNG)

* CIMS provides users the functionality to add fields like the full name, role and department when adding a new member to the team in CIMS app.

![add members](cim_users/static/cim_users/addmember.PNG)

* CIMS furthermore allows authorized users to update members in the teams module. Users may therefore update or delete members as they see fit.

![update teams](cim_users/static/cim_users/updateteammembers.PNG)

### Features left to implement

* Link the CIMS app to social media platforms like Facebook

* Create logic and UI to separate admins/user views and super admins/superusers

------
## Database Schema

* The CIMS database is comprised of the following custom models;

![The Database Schema](cim_users/static/cim_users/drawSQL-copy-of-django-mysql-export-2023-02-20.png)

1. **Usaz**

* This model was designed to capture user detasuper adminsith the default django User model.

2. **Patient**

* The Patient model captures patient details, including id as the primary key, full_name and symptoms. The model has a one to many relationship with the Diagnosis, Medicine, and Appointment
models. The relationship is enforced by the patient_id foreign key in the different related models.

3. **Appointment**

* This model captures appointment details, including id as the primary key, patient_name, patient_id and
time of appointment. The model has a one to many relationship with the Team and Patient
models. The relationship is enforced by the patient_id and doctor_id foreign key columns
visible in the model.

4. **Diagnosis**

* The Diagnosis model captures all diagnosis details, including id as the primary key, patient_name,
test_name for carried out tests, diagnosis, patient_id, doctor_id and the time of diagnosis as time_of_visit. The model has a one to many relationship with the Patient and Team models. The relationship is enforced by the patient_id and doctor_id foreign key columns in the model.

5. **Medicine**

* This model captures all pharmacy or treatment or medicine details, comprised of id as the primary key, medicine name as drug_name, patient name as prescribed_to, amount of prescription as stock, and patient_id. The model has a one to one relationship with the Patient model, enforced by the patient_id foreign key column in the model.

6. **Team**

*  This last model captures CIMS service providers or team details, comprised of id as the primary key, full_name, position and area of specialisation as department. The model has a one to many relationship with the Appointment and Diagnosis model, enforced by the team primary key (id) as doctor_id foreign key column in the model.

-------
## Testing

1. **Automated tests**

* Using custom class based Django unit testing to ensure that the index views and urls of the services, forexample, appointments, patients, diagnosis and medicine can be accessed without fail and that the custom models within the app can capture user data.

* The results after running tests through "python3 manage.py test cim_users/"

![Console results of the tests](cim_users/static/cim_users/automated%20tests.PNG)

2. **The functionality of the site**

* The CIMS app consists of nine pages namely: the home page/ the landing page before login, the dashboard page after a user logs in, the team, services, patients, appointments, diagnosis/laboratory, pharmacy/medication, log in, register or signup pages.

* The CIMS app has a navigation bar that runs across all the pages of the app for easy navigation.

* The navigation bar has an active menu, when a user opens the CIMS app, they navigate from page to page using this feature. Furthermore, the color of the active menu items is white whereas the inactive pages remain colored yellow. The white color shows which page the user is on.

* Before login, the CIMS app user only has access two forms. One of the forms encourages users to log on to the application. The second form encourages the users to register on to the application. The users will be able to enter their names, emails, passwords and to confirm the passwords chosen. These credentials will then be used to log on to the application to be able to manage the clinical services offered by the application.

* The CIMS application has a team page which shows the different team members available before a user registers on the app. When a user registers, the application will then enable the authorized user/admin to view, add, update or delete the team members.

* The CIMS app has a services page. The service page for users who are just visiting the application before registration is static and only offers a chance to view the services offered. After registration, the users/admins will be able to view and manage the services. This means that the users will be able to fully manage the patients, the appointments, the diagnosis and the medication or prescription on the application.

* I have tested the functionality through code inspection and I'm happy to report that the CIMS app features function as intended.

3. **Responsiveness**

* The CIMS app is responsive to different media devices. Media queries are set for different device views with a maximum width of 768 pixels and 600 pixels or below.

* I have tested the responsiveness of the CIMS app and therefore happy to report that through code inspection, the CIMS app responds well to different device views.

4. **Bugs and Fixes**

**Bug 1:** During the login phase, there was a bug that returned false message for users created that are not in the system. This bug was fixed by simply changing the message to 'credentials do not exist' in the views for the logins.

**Bug 2:** The database was not capturing the registered accounts. The accounts created were not reflecting even though the flash message was showing that they were created. **Fix** Added a user creation method in the user creation logic, right before displaying the success flash message.

-------
## Validation

* Frontend validation was used to ensure that form data being submitted to our views are not empty or null.

![The form validation](cim_users/static/cim_users/blankfields.PNG)

* Serverside validation was used to ensure that the right data was being posted before capturing it to the database.

### Validator Testing

1. **HTML**

2. **CSS**

3. **Python**

4. **Accessibility**

![The lighthouse accessibility score](cim_users/static/cim_users/lighthouseaccesibility.PNG)

**Unfixed Bugs**

-------
## Deployment
-------
### Version Control

* The site was created using the Visual Studio Code editor and pushed to github to the remote repository django-cims.

The following git commands were used throughout development to push code to the remote repo:

* git add <file> - This command was used to add the file(s) to the staging area before they are committed.

* git commit -m "commit message" - This command was used to commit changes to the local repository queue ready for the final step.

* git push - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The following steps were followed to deploy this project to Heroku:

* Go to Heroku and click "New" to create a new app.

* Choose an app name and region region, click "Create app"

* Go to "Settings" and navigate to Config Vars. Add the following config variables:
   * PORT : 8000
   * secret_key:
   * disable_connectstatic:1

* Navigate to "Deploy". Set the deployment method to Github and enter repository name and connect.

* Scroll down to Manual Deploy, select "production" branch and click "Deploy Branch".

* The app will now be deployed to heroku

* The live link can be found here- https://django-cims.herokuapp.com/
------
## Credits
------
* Lecture/ course videos on how to deploy the application

* YouTube tutorials on how to import library in python https://www.youtube.com/watch?v=h0oRPIlnJYQ

* All images are from Pixabay https://pixabay.com/images/search/

* Stackover flow for fixing code bugs https://stackoverflow.com/

