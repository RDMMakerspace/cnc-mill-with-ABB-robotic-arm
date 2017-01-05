This server is a Multithreaded TFTP Server based on Trivial File Transfer Protocol
and is normally used for PXE Boot or storing/retrieving router images. It supports advance
options like tsize, blksize, interval and Port Ranges.

MultiThreaded server (TFTPServerMT V1.6x) listens on listening port for new requests,
however further communication is done on any free server port (from specified port range),
using new independent thread.

If you are not able to open multiple ports in firewall, other than listening port, you
can try single port version (TFTPServerSP V1.6x) of this server. Single port version responds
on same port where it listens. Single port version can also serve multiple clients
at same time despite single port/thread being used. It is only little slower than
multithreaded server.

If you are accessing TFTP Server using NAT Gateway, your request will go to the server
but server may not be able to send response back to to you. This is true with this MT Server.
In this case too, you have to download and use Single Port version (TFTPServerSP V1.6x) 
of this server.

This is stable Release 1.64

CHANGES in 1.64

1) The Server do not anymore listens on 0.0.0.0, it detects the interfaces dynamically
   and listens on each of them. This causes better performance.

CHANGES in 1.61

1) Can listen on 0.0.0.0 this would allow listening on all interfaces
2) File buffering has been improved

CHANGES in Release 1.5

1) Bug about filename being too large is fixed
2) Read, Write and Overwrite permissions can be configured independently

BUGS FIXED in Release 1.41

1) LogFile bug fixed.
2) Multiple Messages on Stopping Fixed.
3) Thread Looping on Socket No. being 0 Fixed.

ENHANCEMENTS in Release 1.4

1) This release supports Thread Pool.
2) log file, ini file and state files locations can be overridden.

BUGS FIXED in Release 1.31
1) Max Block Size is 65464, bug fixed for setting this.
2) Code Cleanup and More Error Handling

NEW FEATURES in Release 1.3

1) Listening ports can also be specified. Ports more than 1024 do not need root account
2) Block size can now be as large as 65503.
3) Block Number rollover added, allowing transfer of files of any size.

NEW FEATURES in Release 1.2

1) Multiple Listening Interfaces can be specified.
2) Logging has been added.
3) Multiple directories can be added to home using aliases
4) Permitted Hosts can be specified
   
DOWNLOAD

The latest version can be downloaded from http://tftp-server.sourceforge.net/

INSTALLATION

Installer automatically installs the program.
For Windows NT/XP/2K/Vista/7 it should be installed as Service (recommended).

CONFIGURATION

You need home directory to be set in TFTPServer.ini file,
you can ignore other parameters like blksize, timeout and interval.

You can use single directory as HOME directory. That case, all paths are 
appended to HOME directory. For example, your entry under [HOME] is:-

[HOME]
e:\opt\bootfiles

Then any request would be translated as
"get myfile/bootfile.boot" to e:\opt\bootfiles\myfile\bootfile.boot on server.
it would be simply prepended to requested file path.

But if you use an alias like

[HOME]
a=c:\bootfiles
b=d:\sdf\sfsd
c=f:\sfrd\dsfr

Then your requests would be translated as:-

"get a/myfile/bootfile.boot" to c:\bootfiles\myfile\bootfile.boot
"get b/myfile/bootfile.boot" to d:\sdf\sfsd\myfile\bootfile.boot
"get c/myfile/bootfile.boot" to f:\sfrd\dsfr\myfile\bootfile.boot

on server (alias would be substituted with it's value)

In this case any request, not starting with any of alias a,b,c would be errored out.
The advantage of using alias is you can specify multiple locations.

LICENSE

1) This program is released under GNU GENERAL PUBLIC LICENSE, Version 2, June 1991
2) This document is also released under above license.

DEBUG

If program is not responding:-

1) Check network hardware.
2) Check the log file or Run StandAlone, it will provide all debug information
   as it verbatim the activities.
3) Errors like "bind failed" means another tftpserver is running and listening
   at port 69. You can only have one tftp server running at a time. This error may also
   come if interface specified under [LISTEN-ON] is not physically available on Server.
   If you have specified [LISTEN-ON] IPs, check that IP and interface.
4) Max size of file being transferred depends on block size, the max block count being 65536,
   it would be 512*65536 or 32MB. This limitation can be increased by increasing block size
   upto 65464 which makes the max file size to 4.2 GB. However setting the block size also de pent
   on if client supports it. Some clients like Linux support block number rollover, which make
   the max file size unlimited, irrespective of block size.
5) If you are accessing TFTP Server using NAT Gateway, your request will go to the server
   but server may not be able to send response back to to you. This is true with MT Server.
   In this case you have to download and use Single Port version of this server.

UNINSTALLATION

Goto Control Panel and uninstall the program.

BUGS

If you find any problem with this program or need more features, please send mail to achaldhir@gmail.com.
You may also send thanks email if it works fine for you.
	
DONATIONS

If you find that this program is suitable for your production environment and you are using it, Please
consider some donation for this project. Please dont be lazy about it. I have spent more than 200 hours
on this project but no donation has been received so far.