# Treasure

## GUI AND CLI

### Options
* help - usage
* list - list the encrypted documents (name given by user + path)

## First setup
Give the user two options:
* Create a master password and use random generated strong passwords to encrypt all files (more suitable to transfer files)
    * There will be a generated file containing all passwords for the other files (this file is encrypted using the master password). In other words, these passwords will be encrypted and stored locally.
* Not create a master password and use individual passwords for every file (more suitable for local storage)

Could we give both options at the same time?

## Encryption
Encrypt a treasure and give the following options:
* Where to store
* Delete original file
* Store as archive
* Give the result a name to speed up everything else (sending files, decryption, etc.)

    Example of this idea:
    > python treasure.py encrypt --name something ./test.txt <br>
    > python treasure.py decrypt something

## Decryption
Decrypt a treasure and give the following options:
* (gui) search bar
* ... TODO


## Send file
Open a secure channel to share treasures between two instances of this program
* (gui) drag and drop
* (cli) receiver and sender concept

The hash and salt are sent with the file (inside)

## Behind the scenes
Json of encrypted files should contain:
* Name given by user
* Path to the encrypted content
* Checksum
* Hashed & Salted password
* Salt
* ...?