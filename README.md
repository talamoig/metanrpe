## metanrpe

Python script that prints out all the nrpe-callable checks available
on localhost. The checks are obtained from the standard
`/etc/nagios/nrpe.cfg` file (or a different) file is passed as
argument and recursively from files and directories included with the
`include` and `include_dir` directives.

This script can be used to let remote servers (tipically a
nagios-like server) ask which nrpe checks can be invoked on the host.

Eg.:

	nagios-server # /usr/lib64/nagios/plugins/check_nrpe -H remote-host -c metanrpe
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

