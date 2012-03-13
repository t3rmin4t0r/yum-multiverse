rpm: 
	tar -czvf /tmp/yum-multiverse.tgz *
	rpmbuild -ta /tmp/yum-multiverse.tgz

