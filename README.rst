Couch PoData Processor
========

These are the set of scripts used to implement the CouchDB-based data processing management and tracking tools used by the Edelweiss experiment. This system is described in the paper: A multi-tiered data structure and process management system based on ROOT and CouchDB. G. A. Cox, et. al. Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment, Volume 684, 21 August 2012, Pages 63–72. http://dx.doi.org/10.1016/j.nima.2012.04.049

These scripts do not form a coherent system as of yet. Also, these scripts are, admittedly, not very elegant and contain a lot of amateurish coding. But perhaps if there is time and interest this can morph into a real product that is more useful and can be used "out of the box". These scripts currently exist within the collaboration as part of the KData library, which is a ROOT-based data structure and analysis toolkit written specifically for Edelweiss data. They were taken from that library and placed here within the "python" directory.

The main reason for the complexity and number of scripts here is because the Edelweiss data processing occurs on two separate computer systems, one near the DAQ in Modane and the other at the Computing Center in Lyon where a large batch-processing computer farm is available. Also, the Modane computer systems sit behind a VPN and we can only automatically push data out from the Modane system. Additionally, we cannot run infinitely long jobs on nodes at the CC in Lyon. This means that a job that continuously polls from the CouchDB _changes feed cannot run in Lyon. Instead, we run these jobs on a machine in Modane.

For Edelweiss, we have raw DAQ files that need to be transfered from Modane to the Lyon (process 0), converted into raw ROOT files (process 1), and then further analyzed (process 2, 3, ...).  For each data file we store a meta-data in a doc in the CouchDB database 'datadb'. This database exists on a local CouchDB server in Modane and at another CouchDB server at KIT. These database servers are continously bi-directionally synchronized (through the CouchDB replication feature).

There are two parts to this project. 
* the CouchApp that defines the filters/views used on the CouchDB server
* the python scripts that use these filters and views to call the processing routines (usually compiled C++ code)

Within these sets of scripts there is definitely a framework that could be "extracted" and recoded for a more general purpose. The framework and implementation here has been mixed together. In the description below I will identify which parts of the code would be a part of that extracted framework and which would be part of an implementation that would hook into that framework. 

*There is a third, completely external app that monitors this database and presents the information on a webpage. The webpage is found here: http://edwdbik.fzk.de/datadb/_design/app/index.html and the code for this is found here: https://github.com/gadamc/daqstatus.*

CouchApp
--------

The filters 'newproc0' and 'statusgood' are used by the python scripts that continuously poll the CouchDB _changes feed. The docs in the CouchDB returned by these filters are then used to run a process on corresponding data.

When a document passes through a filter, a python script is called that accesses a particular View result in order to get the full CouchDB document so that it may update the status of processing.

These filters and views would be a part of the framework, although there would need to be some sort of configuration tool for the user to provide the names of and values of some pieces of these filter and mapReduce view codes and to then automatically generate the filter and mapReduce code based upon that configuration tool.

MetaData Doc KeyWords
---------------------

The entire process is driven by the existence and values of particular keywords in the CouchDB docs. These keywords are "status" and "procX" where X = 0, 1, 2, ...  Additionally, there is a "batchjob" keyword that is attached to the docs to record useful information regarding the submission of batch jobs for that data, such as the process that was run, the batch job number, the location of the standard Out and standard Err from the batch job, and date / time. 

The value of "status" can be "closed", "good", "bad", "queued", "proc X in progress" or "failed". The meaning of these values are
* closed = the DAQ system (or equivalent script) has closed the data file and is ready for processing
* good = the data file is ready for the next step in the processing chain
* bad = something bad happened
* queued = the process has queued in the batch system in Lyon and is waiting
* proc X in progress = the process is running 
* failed = a process failed

Each "procX" keyword contains useful information regarding each process, such as the script or program that was called, the batch process job number if it was called on the batch system, the date / time, the computing node on which the process ran, and the full path of the output data file.


Descripion of Chain of Events for the Edelweiss Implementation
--------------------------------------------------------------

This section describes the full chain of events and the Python scripts used. 

1. Ideally, the DAQ would write a meta-data doc to the CouchDB 'datadb' when the raw data file is opened and data is being written to disk. Upon completion of data acquisition, the DAQ would updated the database document's "status" keyword to "closed". This particular step has not yet been implemented in Edelweiss. Instead, there are a few Python scripts that search the local directory structure, find raw DAQ files that are ready for processing and then create the meta-data docs and place them on the CouchDB 'datadb' database. These are found in the "sambaToCouch" directory.


