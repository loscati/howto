> WARNING: this is a WIP doc. It might not see the light of a new edit. We'll see if I need a nas

## The computer
Singleboard computer: [Zimaboard](https://www.zimaboard.com/)

Pros:
- Low consumption
- Great connections for expantion
  - 1 PCIe 2.4 x 4 -> one can attach new hardware (NVme, ethernet, etc.)
  - 2 Sata 6.0 Gb
  - 2 LAN Gigabit
  - 1 mini-DisplayPort
  
## Proxmox
0. config BIOS to enable virtualization: turn on intel virtualization and VT-d
1. select zfs in RAID 1 (mirroring)
2. install the system

Configurations:
1. Create container LXC in the first node
2. template: use the guide provided in the tab (must be connected to the internet)
3. Storage: one can add more disks 
4. RAM: 2Gb
5. Static IP (IPv4): 192.168.1.*id_container*/*CIDR* and gateway
6. Enable start at boot (on the option)

# Disks
- [Western Digital Red Pro 2 TB 3.5" 7200 RPM](https://pcpartpicker.com/product/3dNp99/western-digital-internal-hard-drive-wd2001ffsx)
Important: watch out for the fault tolerant, e.g. the WD Red Pro instead of normal Red

# References
- Video series from [MorroLinux (in italian)](https://youtu.be/DrHn9wlyzJ0)
- [MergerFS + SnapRAID (Italian)](https://youtu.be/5QSkDZi9OzY)
- Good [HD buy guide from the DataHoader subreddit](https://www.reddit.com/r/DataHoarder/wiki/hardware/#wiki_nas)