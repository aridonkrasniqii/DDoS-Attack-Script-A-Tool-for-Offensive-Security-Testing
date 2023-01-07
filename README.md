# What are DoS and DDoS attacks? 

`Denial-of-service` (DoS) and distributed denial-of-service (DDoS) attacks are malicious attempts to disrupt the normal operations of a targeted server, service, or network by overwhelming it with a flood of Internet traffic. 

`DoS` attacks accomplish this disruption by sending malicious traffic from a single machine — typically a computer. </br >
`DDoS` attacks, meanwhile, use more than one machine to send malicious traffic to their target. Often, these machines are part of a botnet — a collection of computers or other devices that have been infected with malware and can thus be controlled remotely by an individual attacker. </br >
</br > </br > 
We have build an application that can attack websites that are not protected from cloudflare and also protected from cloudflare </br > 

# Command Line Usage 

* `--help` => Show possible commands
* `--host` => Specifies the host that you want to attack
* `-d` => Website path
* `--ssl` => HTTP/HTTPS
* `--port` => Port e.g. 80/443 
* `-t`  => Number of threads
* `-x` => Specify proxy file 

![Screenshot from 2023-01-07 17-27-50](https://user-images.githubusercontent.com/77694113/211161139-be6f81b4-5834-4e41-8340-af8853a731f6.png)

 # Example 
 ```bash 
 # Run the script 
 python ddos-attack/main.py --host merrfryme.com
 ```
 
![Screenshot from 2023-01-07 17-33-48](https://user-images.githubusercontent.com/77694113/211161145-cb25aa48-14ae-4be6-97ac-38c6666ab809.png)

 
 # Building 
 
 * You can use `git` to build this project. The following should work:
 
 ```bash
 # Clone repository via Git.
 git clone https://github.com/aridonkrasniqii/ddos-attack.git
 
 # Change directory to repository.
 cd ddos-attack 
 
 # Run the script. 
 python ddos-attakc/main.py 
 ```
 
## Authors
* [Bleranda Azemi](https://github.com/Blesaza)
* [Besarta Kurtaj](https://github.com/besartakurtaj)
* [Aridon Krasniqi](https://github.com/aridonkrasniqii)


