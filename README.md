# python_automation
Integral boilerplate python automation project using behave and docker containers. Page object model, UI and API testing, parallel execution, multibrowser support 

## SOLUTION

Code is structured as follows:

```
python_automation
|
|- selenium-grid: Samples to build custom nodes and connect them to the hub. f.e.: Need to support older chrome? Check.
|   |...
|
|- src_code: Base directory containing the actual test code
|   |- context
|   |     |- config.py: Singleton to easily access settings
|   |     |- driver.py: Instantiates the driver according to settings/scenario or feature tags
|   |     |- testsettings.json: Settings used to run the tests.
|   |
|   |- features: files containing the definition of feature and scenarios in gherkin
|   |     |...
|   |
|   |- helpers
|   |     |- before_run_hooks.py: custom hook to be executed before tests, for clean up / data setup
|   |     |- custom_exceptions.py: what the name implies, custom exceptions.
|   |     |- apihelper.py: methods that provide interection with the REST API
|   |
|   |- model
|   |     |- Customer.py: Class representing a customer.
|   |
|   |- pages: Contains the page objects representing different pages or sections of the web application
|   |     |- basepage.py: base page object from which all other PO inherit
|   |     |....
|   |
|   |- steps: Bindings that match each of the steps defined in the feature files. 
|   |     |- api.py
|   |     |- shop.py
|   |     |- users.py
|   |
|   |- behave_parallel.py: A script to circumvent behave single thread execution
|   |- Dockerfile: docker file with the instruction on how to build a python container image fit to run these tests
|   |- environment.py: Hooks, methods to be triggered at certain points of the scenario/feature execution
|   |- main.py: simple script that runs tests using behave
|   |- requirements.txt: list of project dependencies, in order to quick install with pip
|
|- .gitignore
|- docker-compose.yml: A docker compose file, to quickly bring up this whole thing. More info below
|- README.md

```

## DEPLOY & RUN

### Before

After cloning the repository, create the secrets required by the sample app by executing the following commands that require you to init docker swarm first:

```
mkdir certs

openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key -x509 -days 365 -out certs/domain.crt

docker secret create revprox_cert certs/domain.crt

docker secret create revprox_key certs/domain.key

docker secret create postgres_password certs/domain.key
```

Make sure to copy the devscrets folder to the repository, or else edit the docker-compose file to correctly route the path.

Note: The Android emulator works in hosts that have virtualization enabled. Refer to https://github.com/budtmo/docker-android/issues/93

It is recommended to use a docker visualization interface.

### The environment

Consists of a series of docker containers: 
* One group including the selenium (v3) grid hub, firefox and chrome nodes, an appium node and an android emulator node with chrome installed. 
* Another group consisting of a the sample application to test, webapp and database. 
* A docker container based in a python3.8 image with tty where to run the tests.

Deploy the whole environment simply by executing:
```
docker-compose up
```

Once up you can check the status of the grid by checking:
http://localhost:4444/grid/console

The application can be reached at:
http://localhost:8080/

And the android emulator, that has noVNC support, at:
http://localhost:6080/

There's no visualization support for the chrome and firefox nodes. If you need so, you can replace the images and use the 'debug' nones instead. Refer to: https://github.com/SeleniumHQ/docker-selenium/tree/selenium-3


To run the tests, tty to the docker container named 'tests' and execute:

```
python3 main.py
```

### testsettings.json

If you need to check what the application is doing, want to run locally or to experiment with the code you can edit the testsettings file to your needs.

Provided file contains:
```
{
  "url": "http://appserver:8080",
  "api_uri": "http://appserver:8080",
  "default_browser": "chrome",
  "execute_in_grid": true,
  "grid_uri": "http://selenium-hub:4444",
  "driver_timeout": "10"
}
```

Note that host names used work when deployed in docker using the same network. Otherwise localhost should be reachable.

For instance, if you wanted to see the code in action in a local environment you can just deploy the sample app by creating a new docker-compose.yml file and then execute the code from your python ide and see it running in chrome. In this case, the file would look something like this:

```
{
  "url": "http://localhost:8080",
  "api_uri": "http://localhost:8080",
  "default_browser": "chrome",
  "execute_in_grid": false,
  "grid_uri": "http://localhost:4444",
  "driver_timeout": "10"
}
```

### Scenario tags
Use tags to perform custom actions, such as executing a test using a certain browser configuration of your choice. In the code provided, @Browser:firefox would override the default browser set, and try to run the test using firefox, in a node if grid is enable or using a gecko driver if not.

Tags are applied in feature files, and handled in hooks (environment.py)
