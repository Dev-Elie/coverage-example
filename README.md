# Coverage - example
## Set Up
### 1 .Clone the git repo and create an environment 
                    
**Windows**
          
```bash
git clone https://github.com/Dev-Elie/coverage-example.git
cd coverage-example
py -3 -m venv venv
```
          
**macOS/Linux**
          
```bash
git clone https://github.com/Dev-Elie/coverage-example.git
cd coverage-example
python3 -m venv venv
```

### 2 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install the requirements

Applies for windows/macOS/Linux

```pip install -r requirements.txt```


### 4. Reporting
To generate a coverage report, executed the command:

`pytest --cov-report term --cov=app tests/`

Read more about coverage reporting [here](https://pytest-cov.readthedocs.io/en/latest/reporting.html)



