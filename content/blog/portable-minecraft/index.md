## Introduction

Recently, I acquired a Raspberry PI 5 and was eager to find a practical use for it. I am a fan of Minecraft and I have experience in server development (and I am currently working on an exciting project related to it). Therefore, I decided to create a project on this topic to potentially help others.


## Relevance

I know many people who are not programmers but want to create their own Minecraft server to play with friends. They prefer not to rent a server permanently and want minimal connection latency. One solution to the latter issue is to use an affordable portable device, such as a Raspberry Pi. However, the process of installing and configuring an operating system on the Raspberry Pi, as well as creating an optimized Minecraft server, can be complex for the average user. This is where my project can help.


## Advantages

This project has several advantages, including:
- Simple and fast installation
  
- Clear and easy-to-follow instructions that do not require any programming or system administration knowledge
  
- Portability (due to the small size of the Raspberry Pi). 
- The recommended Raspberry Pi model provides the best gaming experience, but the software is supported on `4GB` and `8GB` models of 4 and 5 versions.

- The customization process is simple and convenient.

While it may not provide a significant advantage, it can enhance your appearance among friends who are not familiar with programming or system administration.


## Unique amenities

This project has quite a large set of unusual but very handy functional features, including:
- Support for all the latest Minecraft versions (can be customized in the control panel)

- Ability to allocate not all available RAM to the server, but only a part of it (can be customized in the control panel).

- Ability to select and automatically install the server kernel (can be customized in the control panel, available kernels are listed on the project page)

- Ability to connect to the server via **SFTP** (e.g. to install plugins or modify server.properties file)

- Ability to connect to the server console via **RCON** (batch script for connection is also available on the project page)

- Ability to enable support for Minecraft Bedrock clients. (If enabled, all necessary files will be downloaded automatically)

- Convenient interface to connect to the new Wi-Fi network, as well as the ability to use Ethernet cable


## Technical implementation

* The project was implemented using the resources and capabilities of the balenaCloud service. This simplifies the user interface greatly, as the balenaCloud control panel interface is straightforward and works seamlessly with balenaEtcher.
 
* The Raspberry Pi listens on ports `25565`, `25575`, `19132` and `22`.

* Both Raspberry Pi 4 and Raspberry Pi 5 devices are supported.

* The system operates within Docker containers, with automatic installation of Java 17. File downloads are facilitated through the wget utility,

* SSH support is provided by openssh-server.


## Setup

The project page provides a comprehensive guide to the installation and initial setup process. Therefore, it is unnecessary to review and describe it in this overview article.


## Testing Process and Results

I have conducted multiple tests on this project. 

In this regard,
  I tested the server on my Raspberry Pi 5 (`8GB`) and it handled the tasks well. The initial setup took approximately `1.5` minutes while connected via Wi-Fi at `500mbit/sec`. I used 12 Minecraft Java accounts and 2 Minecraft Bedrock accounts, each jumping in different chunks. The server was able to handle the load without any issues, maintaining a stable TPS of `20`. 
  Additionally, I conducted a TNT explosion test on the server, albeit not on a large scale as seen in older YouTube videos. No performance problems occurred during testing.

  A good friend of mine also tested the server on his Raspberry Pi 4 (`4GB`) board. He did not use many accounts and did not perform any performance measurements, but he shared that everything installed within 3-4 minutes while connected via Wi-Fi at `100mbit/sec`. Gameplay in creative mode was good.

  A friend brought a Raspberry Pi to our educational institution, claiming it had `8GB` of memory. However, it turned out to only have 1GB. The installation process took over an hour due to a very unstable connection on a mobile device hotspot with a speed of 5mbit/sec. Although we were able to start the server, we were unable to play. Despite the limited technical capabilities of the Raspberry Pi 4 (`1GB`), we attempted to perform the necessary testing.


## Conclusions

I found this project interesting in design and use. It is useful, as confirmed by my friends who assisted me in testing. Its ease of use is a significant advantage. 

Based on the conducted tests, I recommend the following:
- Use a Raspberry Pi with a minimum of 4GB or 8GB.

- Ensure a stable internet connection during the initial installation to avoid lengthy delays.

- For optimal performance, it is recommended to use a stable internet connection. However, a mobile hotspot can also be used.

- Please ensure that the Wi-Fi network specified in balenaCloud is operational to avoid installation issues. If the network is not available, Ethernet can be used for the first installation and the network can be changed later.    

- If you have slow or unstable internet or if you prefer to play from unlicensed accounts, you can set online-mode to false.


- To ensure optimal performance, it is recommended to use original or recommended Raspberry Pi power supplies. Using other power supplies may result in degraded performance.    

- For fast and reliable storage, it is recommended to use good quality SD disks such as **ADATA EXTREME PRO** or other similar devices.
