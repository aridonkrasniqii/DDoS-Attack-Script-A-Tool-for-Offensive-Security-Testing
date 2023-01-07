# What are DoS and DDoS attacks? 

Denial-of-service (DoS) and distributed denial-of-service (DDoS) attacks are malicious attempts to disrupt the normal operations of a targeted server, service, or network by overwhelming it with a flood of Internet traffic. 

DoS attacks accomplish this disruption by sending malicious traffic from a single machine — typically a computer. </br >
DDoS attacks, meanwhile, use more than one machine to send malicious traffic to their target. Often, these machines are part of a botnet — a collection of computers or other devices that have been infected with malware and can thus be controlled remotely by an individual attacker. </br >
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

![image](https://user-images.githubusercontent.com/77694113/211160738-b6f97d66-b0df-48cc-9745-1970c57d95d6.png)
 
 # Example 
 
 ![image](https://user-images.githubusercontent.com/77694113/211160925-1ea401cb-f00a-4985-b210-d59a8c73190a.png)

 
 
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
