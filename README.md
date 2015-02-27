## metanrpe

Python script that prints out all the nrpe-callable checks available on the localhost.
The checks are obtained from the standard `/etc/nagios/nrpe.cfg` file and following
`include` and `include_dir` directives if any.

This script can be used in another check, to let remote servers (tipically a nagios-like)
ask which nrpe checks can be called on the host.

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

