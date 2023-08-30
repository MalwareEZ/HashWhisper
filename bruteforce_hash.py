import hashlib
import os
import argparse
import banner_md5
from colorama import Fore
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser(description="tool to crack an md5 hash")
    parser.add_argument("-w", "--wordlist", dest="wordlist", help="wordlist path", required=True)
    parser.add_argument("-H", "--hash", dest="hash", help="file hash path", required=True)
    args = parser.parse_args()

    wordlist_path = args.wordlist
    hash_path = args.hash

    if os.path.exists(hash_path) and os.path.exists(wordlist_path):
        os.system("cls" if os.name == "nt" else "clear")

        print(f"{Fore.GREEN}{banner_md5.banner_md5}")

        with open(hash_path, "r") as hash_file:
            hash_lines = hash_file.readlines()

        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wordlist_file:
            wordlist_lines = wordlist_file.readlines()

        print(f"{Fore.BLUE}[*]{Fore.WHITE} Loading...")
        
        wordlist_progress = tqdm(wordlist_lines, desc="wordlist progress", unit="mot")

        for mot_line in wordlist_progress:
            mot_sep = mot_line.strip()
            mot_hashed = hashlib.md5(mot_sep.encode("utf-8")).hexdigest()


            if any(mot_hashed == hash_line.strip() for hash_line in hash_lines):
                wordlist_progress.close()
                print(f"\n{Fore.GREEN}[+]{Fore.WHITE} Password found :", mot_sep)
                return True

        wordlist_progress.close()
        print(f"{Fore.RED}[x]{Fore.WHITE} Password not found...")
    
    else:
        print(f"{Fore.RED}[x]{Fore.WHITE} The wordlist or hash file path is invalid.")


if __name__ == "__main__":
    main()