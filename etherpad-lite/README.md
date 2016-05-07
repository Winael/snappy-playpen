Etherpad-lite
=============

This project is about creating a snap of etherpad-lite, a coillaborative text-editor.

To talk and collaborate, you can join the Telegram group: https://telegram.me/joinchat/BAY0lz6hN_sV9wlfwoNsUg

Architecture
------------

### Composants

To build etherpad-lite we need :

  - A webserver
  - Etherpad-lite itself
  - A better database than dirty-db like MariaDB 
  - A config forms for Webdm [Optional]

### Interfaces

This snap needs to connect to internet, as a client and server, and export documents to the user home folder. 

So basically, the interfaces needed are :

  - network
  - network-bind
  - home
