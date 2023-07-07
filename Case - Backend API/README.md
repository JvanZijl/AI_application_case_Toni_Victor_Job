# Fly with US - Backend API

## Requirements
Python 3. On Appstream, this comes pre-installed.

## Running
In your AppStream instance, open Git Bash in the same folder as this README file (in file explorer, right click empty spot in folder, 'Git Bash here'). Run each of the commands below, one after the other:

```bash
python -m venv ./venv
source ./venv/Scripts/activate
pip install -r requirements.txt
python setup.py install
python -m fly_with_us_server
```

Some of these commands may take some time to finnish. You should see the following line when you're done:

` * Running on http://0.0.0.0:8085/ (Press CTRL+C to quit)`

Now you've installed and launched the Fly-with-US backend! You can find the API documentation at http://localhost:8085/ui .

The next time you want to launch the backend, running only the bellow commands from the same directory will suffice:

```bash
source ./venv/Scripts/activate
python -m fly_with_us_server
```

## Using the API
### Address
The API is hosted locally, on port 8085: http://localhost:8085/.

Endpoint names follow this address. For example, if you would like to retrieve a list of employees, you would send a GET request to http://localhost:8085/employees/.

### API Documentation
The swagger documentation showing endpoints, expected parameters and structure of returned content, is available at http://localhost:8085/ui/.

### Example HTML file
An example of doing a GET request to retrieve a list of employees and showing these in the browser is given in the `example.html` file.