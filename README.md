# Mew
package manger translator

![alt text](https://github.com/Bashmug/mew/blob/master/graphics/logo.png "kind of a logo")

## Any package manger command on any distro

## How to install
 * clone https://github.com/Bashmug/mew.git
 * cd mew
 * ./mew
 #### OR
 * will make a package later


 Arch |pacman | Q | Qc | Qi | Ql | Qm | Qo | Qp | Qs | Qu | R | Rn | Rns | Rs | S | Sc | Scc | Sccc | Si | Sii | Sl | Ss | Su | Suy | Sw | Sy | U
 --- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
 Debian/Ubuntu| apt-get / apt |  | | | | | | | | | | | | remove| install| | | | | | | search| | | | |

### apt/apt-get to pacman can
* install package (apt install PACKAGE)/(apt-get install package)
* remove package (apt remove PACKAGE)
* update software database (apt update)
* update all (apt upgrade)


### pacman to apt can
* install package (pacman -S PACKAGE)
* remove package (pacman -R PACKAGE)
* update software database (pacman -Syy)
* show updatable packages (pacman -Qu)
* update all (pacman -Syu)

### yum to apt can
* install package (yum install PACKAGE)
* remove package (yum --nodeps remove PACKAGE)
* remove package+dependencies	(yum remove PACKAGE)
