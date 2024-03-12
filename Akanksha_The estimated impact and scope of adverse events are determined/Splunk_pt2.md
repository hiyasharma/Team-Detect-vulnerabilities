<h1>Splunk - Monitor Files</h1>
Splunk Enterprise monitors and indexes the file or directory as new data appears. You can also specify a mounted or shared directory, including network file systems, as long as 
Splunk Enterprise can read from the directory. If the specified directory contains subdirectories, the monitor process recursively examines them for new files, as long as the
directories can be read.

we can include or exclude files or directories from being read by using whitelists and blacklists.If you disable or delete a monitor input, Splunk Enterprise does not stop indexing
the files: input references. It only stops checking those files again.

You specify the path to a file or directory and the monitor processor consumes any new data written to that file or directory. This is how you can monitor live application logs
such as those coming from Web access logs, Java 2 Platform or .NET applications, and so on.

<h2>Add files to Monitor</h2>
Using Splunk web interface, we can add files or directories to be monitored. We go to Splunk Home → Add Data → Monitor as shown in the below image −

![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/100219040/09a8652a-e102-4be0-afd1-d77579f4239e)

On clicking this button, we are presented with the screen to select the source and format of the data we plan to push to Splunk for analysis.

![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/100219040/cef87a5f-4c0d-4560-982e-3a62b05db928)

Next, we choose the default values as Splunk is able to parse the file and configure the options for monitoring automatically.After the final step, we see the below result which
captures the events from the file to be monitored.

![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/100219040/d99b71fb-5ac5-4aef-9c70-0ef0f1da4584)

If any of the value in the event changes, then the above result gets updated to show the latest result.

