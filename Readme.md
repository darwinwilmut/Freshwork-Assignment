<!-- PROJECT LOGO -->
<br />
  <h3 align="center">Data Store</h3>
  <p align="center">
    A File based key-value Data Store
    <br />
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

A File based key-value data store that can be used in your project to store data in key value pairs in `json file` in your local machine. The `Data_Store` is very light weight and can be used in a small or medium level projects. The `Time to live` property is a great feature if you don't want the data to be stored permanently. It destroys the data automatically after the time has expired. 
### Built With
* [Python](https://www.python.org/)

### Features
* File stored as json 
* Time to Live 


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darwinwilmut/Freshwork-Assignment.git
   ```
<!-- USAGE EXAMPLES -->
## Usage
1. Copy the `Data_store` package folder into your project.

2. Import the `Data_Store` module into your python file
    
    ```sh  

    from Main_code import * 
    ```

3.  path can be set manually or path will be set default to current working Directory with file name "Sample.json"
    ```sh
    set_path('Your path')   
    ``` 

4. Create data in Data_store.
   ```sh 
    # the key must be string
    # it takes key and value as the parameter
    create('key',value)

    # the default time to live value is 0 which means None.
    # you can set time to live property
    # it takes integer value (seconds) as the parameter
    set_delay(seconds)
   ```

5. Read data from store.
   ```sh 
   # it takes key as the parameter
    read('key')
   ```
5. Delete data in store.
   ```sh 
    # it takes key as the parameter 
    delete('key')
   ```

   

