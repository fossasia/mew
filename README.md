# Mew

package manager translator

![alt text](https://github.com/fossasia/mew/blob/master/graphics/logo.png "kind of a logo")

## Any package manager command on any distro

## How to install

   * clone `https://github.com/fossasia/mew.git`
   * cd mew
   * ./mew

Arch | pacman | Q | Qc | Qi | Ql | Qm | Qo | Qp | Qs | Qu | Rn | Rns | Rs | S | Sc/Scc | Si | Sii | Sl | Ss | Syu | Sw | Sy | U
:--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--:
**Debian / Ubuntu** | apt / apt-get | dpkg -l | changelog | dpkg -s / aptitude show| dpkg -L|aptitude purge '~o'| dpkg -S / dlocate| dpkg -I | aptitude search '~i(~n $name\|~d $description)'| apt-get upgrade -> n| | | apt remove | apt install --reinstall |  apt autoclean/ apt clean |apt-cache show / aptitude show |apt-cache rdepends / aptitude search ~D$pattern|apt-cache dumpavail apt-cache dump (Cache only) apt-cache pkgnames |apt search| apt update && apt upgrade | apt install --download-only (into the package cache) apt download (bypass the package cache)|  apt-get update| apt install|
**Red Hat / Fedora** | dnf/rpm |qa |   -q --changelog|qi|ql |package-cleanup --orphans|rpm -qf (installed only) or dnf provides (everything) | rpm -qp |  rpm -qa '*\<str>\*'| dnf list updates, dnf check-update | | |dnf remove   |  dnf reinstall | dnf clean all| dnf info|dnf repoquery --alldeps --whatrequires  |  dnf list available|dnf search |  dnf upgrade | dnf download |dnf clean expire-cache && dnf check-update | dnf install |
**SLES/openSUSE**| zypper/rpm |search -s/ qa|   -q --changelog|info/qi |ql | | zypper search -f  | | |zypper list-updates zypper patch-check (just for patches)  | | |zypper remove / zypper rm | zypper install --force |  zypper clean | zypper info| zypper search --requires |zypper packages| zypper search zypper se [-s] | zypper update zypper up| zypper --download-only |zypper refresh zypper ref| zypper in|
**Gentoo** | emerge/equery |  -e world  |  changes -f  |-pv and -S|files | | equery belongs| |eix -S -I |emerge -uDNp world  | | |emerge -C | emerge -1O  |  eclean distfiles |emerge -pv and emerge -S |equery depends |emerge -ep world  |emerge -S  |emerge -u world |emerge --fetchonly |emerge --sync;layman -S  | emerge |


## Adding Packages to Mew

To create a Package Manager's data follow these steps:

* Create a `{{Package Manager}}.json` file.
* The `Package Manager` can be any out of `['apt-get','apt','pacman','dnf','rpm','zypper','emerge','equery']`
* Add relevant data for distros `['debian','ubuntu','redhat','fedora','sles','opensuse','gentoo']`
* Now add data to the JSON file
	```javascript
	{
		"command_1" : {
			"distro_1" : "translated command_1 in distro_1",
			"distro_2" : "translated command_1 in distro_2",
			.
			.
		},
		"command_2" : {
			"distro_1" : "translated command_2 in distro_1",
			"distro_2" : "translated command_2 in distro_2",
			.
			.
		},
		.
		.
		.
	}
	```
* Save the `{{Package Manager}}.json` file into `data' folder.
* Done
