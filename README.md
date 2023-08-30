# Description HashWhisper

HashWhisper is a Python tool dedicated to ethical hackers who want to crack MD5 hashes. It is primarily designed to be used in CTF (Capture The Flag) challenges or penetration testing scenarios where MD5 hashes are employed. This tool allows you to compare MD5 hashes against a list of potential words in order to find matches and retrieve the original passwords.
# Usage
Using HashWhisper is straightforward. Here's an example command:

```sh
$ python3 hashwhisper.py -w /usr/share/wordlist/rockyou.txt -H /home/kali/hash.txt
```
* -w or --wordlist: Path to the wordlist file.
* -H or --hash: Path to the file containing the MD5 hash(es) to crack.

# Features
* Comparison of MD5 hashes against a list of potential words.
* User-friendly command-line interface.
* Support for custom hash files and wordlists.
* Visual progress display using the tqdm library.
* Option to stop searching as soon as a matching password is found.

# Installation
1. Ensure you have Python 3 installed on your system.
1. Clone this repository
1. Navigate to the project directory: 
1. Install the required dependencies: 
```
git clone [https://github.com/your-user/HashWhisper.git](https://github.com/MalwareEZ/HashWhisper.git)
cd HashWhisper
pip install -r requirements.txt
```

# Disclaimer
The use of this tool must comply with applicable laws and ethical hacking guidelines. HashWhisper is intended solely for educational and security testing purposes. The authors are not responsible for any misuse or illegal activities.

# Contributor
@MalwareEZ
