# web-im-crawlr

Websites image crawler using the Python 3 scrapy module.

## Run the project

### Deploy the vagrant environnement and connect to it

    ```bash
    vagrant up
    vagrant ssh
    ```

### Inside the vagrant, start the database

    ```bash
    sudo /vagrant/database/run-database.sh
    ```

### Run any crawler

    ```bash
    scrapy crawl <spider-name>
    ```

## Export/Import the database

The project only performs "upserts" in the database. Providing it with an old database will never erase any information contained within.

### Dump

    ```bash
    # exports to binary file
    mongodump  --archive=dump.archive --db webimages
    # exports to json file
    mongoexport --db webimages --out export.json
    ```

### Restore

    ```bash
    # restore from binary file
    mongorestore --archive=dump.archive --db webimages
    # restore from json file
    mongoimport --db webimages export.json
    ```
