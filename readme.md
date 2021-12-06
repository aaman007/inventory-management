## Installation and Setup

### 1. Create .env file
Run the following command `cp .env.example .env`               
Environment [`DEVELOPMENT,` `STAGING`, `PRODUCTION`] and `SECRET_KEY` could be changed optionally.         
Changing the Environment Mode to anything else would require `PostgreSQL` db configuration to be updated as well.       
As, In `DEVELOPMENT` mode, `SQLite` is used as db this is not required

### 2. Creating virtual environment
Run ```virtualenv venv``` command inside the project directory       
Run ```source venv/bin/activate``` to activate the environment          
If you are using PyCharm, you can do the same thing using GUI

### 3. Installing Dependencies
All the dependencies are in ```requirements.txt``` file. Run the following command to install them -             
``` pip install -r requirements.txt ```

### 4. Database Migration
Run the following command to migrate changes to the db           
``` python manage.py migrate ```        
I have used SQLite for simplicity, So using PostgreSQL or MySQL is not required in this step

### 5. Running the application
``` python manage.py runserver ```         
or    
``` python manage.py runserver 0:PORT ``` to run on a specific port


### 6. [Optional] Create a Superuser
To access the admin panel, a superuser account is required.             
Run the following command to create one -             
``` python manage.py createsuperuser ```

### 7. Running Unit Tests
The tests for status code of the 3 required urls are in ```inventory/tests``` and ```inventory/api/tests``` folder      
To run the tests run the following command      
```python manage.py test```        
or        
```python manage.py test inventory```      
NOTE: I have used `TestCase` class provided by django for tests which uses `unittest` module internally

### 8. [Optional] Creating Test Data
Fake data can be created by running -          
`python manage.py create_test_data`       
20 Suppliers and 100 Inventories will be created using factory boy      
In case you want to override this, you can pass values `--num-suppliers` and `--num-inventories` flag in the command          
Example:      
`python create_test_data --num_suppliers 10 --num_inventories 50`
