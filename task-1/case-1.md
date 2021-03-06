Task 1
======

Problem Statement
-----------------

Assuming there are "N" number of devices(having Linux on them) of type
"X" where N &gt; 0, out there in the field(distributed devices all over
the world with limited internet connectivity, so they are not in same
network. Example - a mobile phone, a raspberry pi) .Each device has two
types of network interfaces - One is Ethernet port and second is
wireless interface(wifi adapter) . Each interface would have a MAC
address.

### Case 1:

We have to build a system to collect information from the device at
regular interval. How would you model the system to make this happen?
Following can be the type of information we are collecting from the
devices -

-   Average cpu usage per/day
-   Average memory used per/day
-   disk space of the device
-   ethernet mac id
-   wifi interface mac id

####  Solution:

    Since the have limited access to internet, we could have a
    metrics/information gathering agent running on the devices and a
    service infrastructure to collect this metrics when devices come
    online.

    1.  Agent

        -   The agent stores the data locally on the devices’ filesystem
            in some interexchange data file format.
        -   It should be capable of:
            -   compressing/uncompressing the collected metrics file, or
            -   notify the device owner to purge older metrics data, or
            -   has a directive to configure the storage period of data.
        -   It would push the collected data whenever the agent detects
            access to the service infrastructure.
        -   Each agent would be registered with the service
            infrastructure during the deployment process and provided a
            UID.
            -   agent UID or the device UID could be same.

    2.  Service infrastructure

        -   This service infrastructure may be designed to store the
            data in sql or nosql or object storage.
        -   If the service has is receiving compressed data it should be
            able to uncompress the data before storing it in sql or
            nosql.


