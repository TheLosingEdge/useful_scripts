#/bin/bash
# $1 => example.domain
# Requires https://github.com/tomnomnom/hacks/tree/master/filter-resolved
# Requires jq

#AMASS
amass enum --passive -d $1 -o domains_$1
assetfinder --subs-only $1 | tee -a domains_$1

#Subfinder
subfinder -d $1 -o domains_subfinder_$1
cat domains_subfinder_$1 | tee -a domains_$1

#Project Sonar
curl -s https://dns.bufferover.run/dns?q=.$1 | jq -r .FDNS_A[] | cut -d',' -f2| sort -u | jq -r .FDNS_A[] | cut -d',' -f2 | sort -u | tee -a domains_$1

#Filtering the domains
sort -u domains_$1 -o domains_$1
cat domains_$1 | filter-resolved | tee -a domains_$1.txt
