# DigiClaim
DigiClaim is an insurance claim validation system which will be extensively beneficial for the insurance companies to validate the insurance claims and warranty claims over the damaged mobile Phones. DigiClaim can also be useful for the Performance and Quality Checking of the various parameters and attributes of the mobile device. DigiClaim will automate the complete process of Insurance claiming for damage done to the mobile screen, thereby saving the time of manual intervention making it cost effective.

## Development Stack
* Front-End Development: HTML,CSS,Bootstrap,Vanilla JS, Android XML
* Data-Processing: Python 3.6.7, Android Java
* Back-End Development: Django-Python Framework, openCV
* Database management: DB SQLite, Firebase

## User Authentication :
The user authentication is carried out by firebase authentication service in Android application 
                            
## Android App parameters testing:
* The app will run on the mobile on which testing is to be done.
* The test will check for the working of main components like GPS, Bluetooth, Wifi, Hotspot, FlashLight along with the list of sensors.
* After the testing is completed the report is generated in the form of pdf and is sent to the application database server hosted on the firebase.
![](https://lh4.googleusercontent.com/twO53XpYxOmuabcyzw_TVhdc2vAQLCfQRhkqk2vP03H29w52K2-MN-RIWGFyDXcZ2zlhCt-pQWaoY7do9SzEt8JUUaOnreMgcsipJxeP0Blau0006GhKe8VpfbqtfLQRPEPMV9Jg = 100x100)
![](https://lh5.googleusercontent.com/NG0pZaMcLyV665eyq4c1If6Es3up6L2FZyvOAB8iqYSDmbZfl5prqHHtjQ3uGDJdXuAiY8rk2qluhi_TcRduADwnvUgvnA6b48e6T_RHb6SLJ4T86RuH63FgcqQgziGyZKNxh0fz)

## Scratch/Crack Detection on Mobile Screen Using Image Processing:
* The user will upload the image on the processing server, the testing will be performed for scratch/crack detection.
* Steps involved in scratch/crack detection
  1. Noise removal using Median blur.
  2. Canny’s Edge detection algorithm is applied to the noiseless image.
  3. Thresholding is done to get a clear view of scratches
  4. According to standards, 18% of total screen size is a body, 9 % from the top, 9% from the bottom so we check for         scratches in the defined region. 
  5. If scratches are present on the main part of the screen then those are detected and the results are saved.
* The detection report is sent to the application server again.
![](https://lh5.googleusercontent.com/IjqbnNhYvTx3p2-ZpmGY9R26fXU9I2iM5TM2MyGB36EIrJsTdW7qULZFaPGSDu2cu_fFywNrclyXe-y2I_mtsXJu0xEP0-aYJqvowc5H)

![](https://lh3.googleusercontent.com/mmx23kgzdslH21yd6aR4URf1FQbn57jioKOBjutjjXIDRPwzTa3z3ieYVEIu5mzkj6CRKRWgFgO1KuHSve9cwDzrMNkPO4fvxAiGBJT0IRy_VyvMLdFzUr78MqhDguTJo4dtPs5S)
	
## Database Management:
* A firebase as a centralised application database server, whereas relational DBSQLite-3 as a database on the processing server for the project.
* The user data and the result of performance and QA testing of the mobile phone are stored on the firebase. While all the processing data required while scratch detection is stored on DBSQLite-3 database server.
* Complete normalization is also achieved in different relations of the database.

## Admin Section:
* This panel is accessed by the administrator of the web portal of DigiClaim.
* All the insurance claims regarding the screen damage are available to view in the admin section.
* These reports will be further sent to the concerned Insurance company or authority by the administrator.


## References
1. ColorCrack: Identifying Cracks in Glass 
  Author: James Max Kanter
          Massachusetts Institute of Technology 77 Massachusetts Ave Cambridge
  from: http://www.jmaxkanter.com/static/papers/ color_crack.pdf

2. https://docs.opencv.org/3.4.3/da/d22/tutorial_py_canny.html
3. https://github.com/itext/itextpdf
4. https://www.altoros.com/blog/automotive-insurance-with-tensorflow-estimating-damage-and-repair-costs/
5. Research Paper: https://www.ee.iitb.ac.in/student/~kalpesh.patil/material/car_damage.pdf


