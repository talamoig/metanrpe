## metanrpe

Python script that prints out all the nrpe-callable checks available
on localhost. The checks are obtained from the standard
`/etc/nagios/nrpe.cfg` file (or a file passed as argument) and
recursively from files and directories included with the
`include` and `include_dir` directives.

If the script itself is installed as a nrpe check, it can be used
from a remote host to ask which nrpe
checks can be invoked on the host, in the following way:

	remote-host # /usr/lib64/nagios/plugins/check_nrpe -H nrpe-host -c metanrpe
	check_nis
	check_gmond
	check_crl
	check_funcd
	check_zombie_procs
	check_home
	check_hepspec
	check_crond
	check_total_procs
	metanrpe
	check_homespace
	check_system
	check_load
	check_security
	check_disk

