# Resources

Here you find various sources I ran into as I was working on hacking Star Fox Assault. Some can help for anyone in anygame, others however are more specific to Star Fox Assault

## Table of Contents <br />
1. [Gecko Code Documentation](#GCD) <br />
2. [Gecko Code Writing Help](#GCWH) <br />
3. [Machine Code Help](#MCH) <br />
4. [Real Time Corruptor](#RTC) <br />
5. [Cheat Engine](#CE) <br />
6. [Dan Salvato's Resources for Melee Hacking](#Melee) <br />
7. [Known Gecko Codes for Star Fox Assault](#Public) <br />
8. [Star Fox Assault's Cutting Room Floor Page](#CRF) <br />
9. [Wii Hacking Programs](#Wii) <br />
10. [My Python Script](#Python) <br />

<a name="GCD"/>

## Gecko Code Documentation
* [Here](http://wiigeckocodes.github.io/codetypedocumentation.html) is a half dead website that documents the code types for Gecko Codes in a clean fashion. <br />
* [Here](https://gamehacking.org/faqs/wiicodetypes.html) is more or less the same thing but is written slightly differently and looks worse. <br />
* [Here](https://smashboards.com/threads/guide-to-ar-and-gecko-code-writing-for-complete-noobs.336650/) is a link to a Smashboards page in which ResidentWaffle wrote down more code types comapred to the above to links, but doesn't explain how any of them work.

<a name="GCWH"/>

## Gecko Code Writing help
* Dan Salvato made a [Youtube playlist](https://www.youtube.com/watch?v=IOyQhK2OCs0&list=PL6GfYYW69Pa2L8ZuT5lGrJoC8wOWvbIQv) which acts as an intro to Wii modding. I haven't watched the whole thing but it can most likely help someone. <br />
* On a very well made website, Jimmie1717 made a [webiste](https://www.zeldacodes.org/gecko-to-lua) that converts Gecko Codes into Lua which can help out in understanding how certain code types work (assuming it's correct). <br />
* Pyorot made a Gecko Code complier and posted it on [Github](https://github.com/Pyorot/gecko-compiler), but in my like 3 minute effort I was unable to get it to work. This could possibly help someone who could figure it out though.

<a name="MCH"/>

## Machine Code Help
* [Here](http://math-atlas.sourceforge.net/devel/assembly/ppc_isa.pdf) is a very large pdf of the PowerPC set architecture that I haven't read at all. <br />
* [Here](https://jimkatz.github.io/PowerPC_Examples) is an incomplete guide to Machine Code as Gecko Codes by Jimkatz. <br />
* There exists a [tool](https://code.google.com/archive/p/geckowii/downloads) that converts assembly into a Gecko Code which is very helpful if you use assembly in your gecko codes. <br />
* IBM has [offical documentation](https://www.ibm.com/docs/en/aix/5.3?topic=aix-older-versions#c206690781jeff) of the commands for Machine Code and how it works.

<a name="RTC"/>

## Real Time Corruptor
* If you know of the first person Gecko Code for Star Fox Assault it was found by accident by Impromptunite using the [Real Time Corruptor](https://redscientist.com/rtc).
	* Impromptunite documented his findings in this [Reddit post](https://www.reddit.com/r/starfox/comments/rjbbgt/i_found_an_unused_firstperson_mode_in_star_fox/) and this [Youtube video](https://www.youtube.com/watch?v=ko1B6TX5E5o). <br />
	* Impromptunite also mentions, in great detail, how to set up the Gecko Code in Dolphin and an Offical Wii in his comment in the [Reddit post](https://www.reddit.com/r/starfox/comments/rjbbgt/i_found_an_unused_firstperson_mode_in_star_fox/).
* You also have Vinesauce who used the tool in this [Youtube video](https://www.youtube.com/watch?v=9fi7yLT0mM0&t=262s) if you would like to see what the tool has to offer.

<a name="CE"/>

## Cheat Engine
* There is a branch of Cheat Engine made by Aldelaro5 that is made specifically for Dolphin known as the [Dolphin Memory Engine](https://github.com/aldelaro5/Dolphin-memory-engine/releases)
* You can also use the offical [Cheat Engine](https://www.cheatengine.org/) although I always found the website and installer very sketcky. So be VERY VERY CAREFUL when navigating their website and installer.
	* Punkline on a [Smashboard post](https://smashboards.com/threads/using-cheat-engine-with-dolphin.442909/) explains how to use Cheat Engine with Dolphin. However he doesn't explain how to find the start of the game's memory so I'll do it here. Open Dolphin, right click the game, click "Info", and copy what is inside the "Game ID" box (SFA USA: GF7E01 ; SFA PAL: GF7P01 ; SFA Japan: GF7J01). After doing that search for the Game ID in Cheat Engine as ASCII and find the first memory address that ends with 4 zeros. That address will be the start of the game's memory.

<a name="Melee"/>

## Dan Salvato's Resources for Melee Hacking
* Dan Salvato created a guide for hacking in Melee found [here](https://smashboards.com/threads/assembly-guides-resources-q-a.397941/). While not all of it applies to Star Fox Assault, some of the links are found here, and other links are dead, it may still come in handy.

<a name="Public"/>

## Known Gecko Codes for Star Fox Assault
* All known Gecko Codes for games are publically available at [https://gamehacking.org/](https://gamehacking.org/). I'll list the subpages for Star Fox Assault below
	* [USA (NTSC-U) version](https://gamehacking.org/game/54239)
	* [Europe (PAL) version](https://gamehacking.org/game/54682)
	* [Japan (NTSC-J) version](https://gamehacking.org/game/85479)

<a name="CRF"/>

## Star Fox Assault's Cutting Room Floor Page
* Most games have a [Cutting Room Floor](https://tcrf.net/The_Cutting_Room_Floor) page that contains cut content and backstories to the avaiable games. I'll put the links for Star Fox Assault's page.
	* [The Main Page](https://tcrf.net/Star_Fox:_Assault)
	* [Pre-release Details](https://tcrf.net/Prerelease:Star_Fox:_Assault)
	* [The Discussion Page](https://tcrf.net/Talk:Star_Fox:_Assault)
		* There is one, and only one post here, but he made some interesting discoveries. First off he found a [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1QMK8pJs3ZgFFuoy5y4U-jFw3n6itYhUTZzhprZArSP8/edit#gid=0) of all the audio in the game. He also pointed to an [E3 Demo](https://www.youtube.com/watch?v=prnnf5XEYF4) of the game which I personally don't buy, but what would I know?

<a name="Wii"/>

## Wii Hacking Programs
This will NOT be a tutorial for how to use these programs by the way

* [Homebrew Channel](https://wiibrew.org/wiki/Homebrew_Channel) for various hacking needs. Also I don't know how to install it, someone I know did it for me like 10 years ago.
* [Nintendont](https://github.com/FIX94/Nintendont) for being able to run Gecko Codes on Gamecube games because [Gecko OS](https://wiibrew.org/wiki/Gecko_OS) is only for wii games.
* [Cheat Manager](https://wiibrew.org/wiki/CheatManager) for changing your Gecko Codes (and maybe AR codes but I don't know for sure) into a GCT format.
* Alternatively you can use the online [GCT converter](https://mariokartwii.com/gct/) to make the GCT file.

<a name="Python"/>

## My Python Script
While not the most polished program in the world, if you copy and paste an array of bytes for the inital and final the program will tell you the differences between the both of them along with the memory address. This can be used to find a specific if you know it's somewhere within a certain region.

* [Download (open link than Ctrl+S)](https://github.com/ModSault/General/raw/main/Resources/Hex%20Difference.py)
* [Source Code](https://github.com/ModSault/General/blob/main/Resources/Hex%20Difference.py)
