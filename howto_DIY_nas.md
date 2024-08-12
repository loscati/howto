> WARNING: this is a WIP doc. It might not see the light of a new edit. We'll see if I need a nas

# What I need
This isntructions and information are tuned for my needs. There is no attempt to have a omnibus guide or a step-by-step one. Therefore, please have a look to what are my needs from a NAS and see if these align with yours before read!
- Backup: backupping the phone data and computer files
- Great attention to Photos!
- RAID 1 config. for photos and files, i.e. most important data. "One copy is not a copy" - CGPGrey
- Plex server: being able to stream movies
- Immich: being able to stream photos with metadata


# Basics
### RAID 0 and 1
RAID is a configuration for multiple disks. RAID 0 is a configuration where the data is split between the disks. This means that if one disk fails, all data is lost. RAID 1 is a configuration where the data is mirrored between the disks. This means that if one disk fails, the data is still available in the other disk.

An inportant note is that RAID is not backup. RAID is a scheme that can help you backup you data, but it does not garanties you the safety of your data.
For example, you could have 2 SSDs in RAID 1 to have a mirror image of you data. In the case of a double disk failure (which can happens due to environmental factors such as a fire, but also with the EOF of both disks, see [the disk section](#disks)), you would lose all your data.

### [Samba](https://wiki.archlinux.org/title/Samba)
A software suite that allows to share files in the local network, especially with Windows machines.
### LXC vs Docker
- Purpose:
  - LXC: More suitable for scenarios where a complete operating system environment with isolation is desired.
  - Docker: Focuses on the development, deployment, and scaling of applications.
- Isolation:
  - LXC provides system-level isolation similar to traditional virtualization.
  - Docker offers application-level isolation, making it easier to share resources between containers.
In summary, Docker can be taught as built upon LXC.
### ZFS
ZFS (Zettabyte File System) is a high-performance and highly scalable file system and logical volume manager. It is designed to provide robust data protection, efficient data storage, and powerful data management features.
1. Data Integrity:
   - End-to-End Checksumming: ZFS uses checksums to detect and correct silent data corruption, ensuring data integrity from disk to disk.
   - Self-Healing: Automatically detects and repairs data corruption using redundant data copies.
2. Snapshots and Clones:
   - Snapshots: ZFS allows the creation of read-only snapshots of the file system at any point in time, useful for backups and data protection.
   - Clones: Writable copies of snapshots can be created without consuming additional storage space initially, enabling efficient data replication and testing.
3. Data Compression:
   - ZFS supports built-in data compression algorithms, allowing for reduced storage space usage and potentially increased performance due to reduced I/O.
4. RAID-Z:
   - Integrated RAID: Unlike traditional RAID setups, ZFS includes its own RAID implementation called RAID-Z, offering better protection against data loss.
   - No Write Hole: RAID-Z eliminates the RAID write hole issue, where data can become inconsistent if a system crash occurs during write operations.
5. Copy-on-Write (COW):
   - Atomic Transactions: ZFS uses a copy-on-write mechanism, which ensures that updates to data are made atomically, preventing data corruption in case of a system failure during a write operation.

### [3-2-1 backup strategy](https://www.backblaze.com/blog/the-3-2-1-backup-strategy/)
### Backup
Backup strategy for services: [MorroLinux video in Italian](https://youtu.be/DrHn9wlyzJ0?si=zcHjihLMb_g523Ju)

# The computer
### Zimaboard
Singleboard computer: [Zimaboard](https://www.zimaboard.com/)
Pros:
- x84! easly expanable without aiting for a ARM compatible hw
- Low consumption
- Great connections for expantion
  - 1 PCIe 2.4 x 4 -> one can attach new hardware (NVme, ethernet, etc.)
  - 2 Sata 6.0 Gb
  - 2 LAN Gigabit
  - 1 mini-DisplayPort

Why not a Raspberry Pi?
- ARM architecture
- less I/O connections
- less expandable (no PCIe)

### ZimaBlade
Similar to Zimboard but cheaper.
Cons:
- More consumption on the CPU side
- dissipation on the BOTTOM part


# Distro

### CasaOS
The one coming with the Zima. Morro: "not ready because it requires a lot of CLI interaction".

#### Problems
- every user can access (fully! hence 777) files. See [this issue](https://github.com/IceWhaleTech/CasaOS/issues/1113) an the workarounds in it.

### OpenMediaVault
Debian-based distribution.
  
### Proxmox
Debian-based distribution that allows for virtualizations (containers LXC and VMs).
Pros:
- allows for snapshot for each containers, hence saving its state

Installation:
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

# Software

## Immich
Self-hosting for photos. Setup: run in a container in proxmox, with expandable (virtual) storage.
Pros:
- fast
- map for photos with geo metadata
- possibility to have a backup from the phone directly. Possiility to have a photo on the NAS only, on the phone only, or on both. 

The installation is quite straight forard, use `docker compose`.

Cons:
- do not put it on the internet, becaue everything is clear and it uses `http`. If you want to access it, setup a VPN.

## Jellinfin / Plex

# Disks
General tip: do not buy the same type of disks, from the same loot, and at the same time. The chances of having both disks failing at the same time are higher.

1. HD

   Generally are cheper, but high-end ones does not seems significantly more convinient than SSDs. 
   - [Western Digital Red Pro 2 TB 3.5" 7200 RPM](https://pcpartpicker.com/product/3dNp99/western-digital-internal-hard-drive-wd2001ffsx)
   Important: watch out for the fault tolerant, e.g. the WD Red Pro instead of normal Red
2. SSD

   Watch out for the TbW (TeraBytes Written) value. This is the amount of data that can be written to the disk before it starts to fail.
   - Samsung 870 QVO

# References
- Video series from [MorroLinux (in italian)](https://youtu.be/DrHn9wlyzJ0)
- [Proxmox and RAID (italian)](https://youtu.be/5I2aw_yVcRM?si=vI8t3RRjuVTiQmsf)
- [MergerFS + SnapRAID (Italian)](https://youtu.be/5QSkDZi9OzY)
- Good [HD buy guide from the DataHoader subreddit](https://www.reddit.com/r/DataHoarder/wiki/hardware/#wiki_nas)
- [Transcoding](https://www.reddit.com/r/PleX/comments/11ih0gs/plex_hardware_transcoding_explained/)