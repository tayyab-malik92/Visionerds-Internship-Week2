from chunker import create_chunks
from pypdf import PdfReader
from colorama import Fore, Style, init
import time

init(autoreset=True)
#response time feature
start_time = time.time()


#ui ux
print(Fore.CYAN + "=" * 60)
print(Fore.GREEN + Style.BRIGHT + "        Visionerds Internship - Week 2 Day 7")
print(Fore.YELLOW + "                 PDF Chunking Project")
print(Fore.CYAN + "=" * 60)



print(Fore.BLUE + "\n Loading PDF...")

reader = PdfReader("sample.pdf")

print(Fore.GREEN + " PDF Loaded Successfully!")

print(Fore.YELLOW + f"\nTotal Pages : {len(reader.pages)}")

#text extracting feature

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

print(Fore.GREEN + "\n PDF Text Extracted Successfully!")

print(Fore.CYAN + "\nFirst 1000 Characters")
print(Fore.CYAN + "-" * 60)

print(text[:1000])

#word counting of pdf

words = text.split()

print(Fore.CYAN + "\nWord Statistics")
print(Fore.CYAN + "-" * 30)

print(Fore.YELLOW + f"Total Words : {len(words)}")

#chunking technique
chunks = create_chunks(
    text,
    chunk_size=400,
    overlap=100
)

print(Fore.GREEN + "\n Chunking Completed!")

print(Fore.CYAN + "\nChunk Statistics")
print(Fore.CYAN + "-" * 30)

print(Fore.YELLOW + f"Chunk Size   : 400")
print(Fore.YELLOW + f"Overlap      : 100")
print(Fore.YELLOW + f"Total Chunks : {len(chunks)}")

#display of chunks been made above

for index, chunk in enumerate(chunks, start=1):

    print(Fore.MAGENTA + "\n" + "=" * 60)
    print(Fore.WHITE + Style.BRIGHT + f"                 Chunk {index}")
    print(Fore.MAGENTA + "=" * 60)

    print(chunk)

    print(Fore.GREEN + f"\nWords : {len(chunk.split())}")

#saving of chunks

with open("chunks.txt", "w", encoding="utf-8") as file:

    for index, chunk in enumerate(chunks, start=1):

        file.write("=" * 60 + "\n")
        file.write(f"Chunk {index}\n")
        file.write("=" * 60 + "\n")
        file.write(chunk)
        file.write("\n\n")

print(Fore.GREEN + "\nChunks saved to chunks.txt")


end_time = time.time()
execution_time = end_time - start_time

print(Fore.CYAN + "\n" + "=" * 60)
print(Fore.GREEN + Style.BRIGHT + "           PROGRAM COMPLETED SUCCESSFULLY")
print(Fore.CYAN + "=" * 60)

print(Fore.YELLOW + f"📑 Pages Processed : {len(reader.pages)}")
print(Fore.YELLOW + f"📝 Total Words     : {len(words)}")
print(Fore.YELLOW + f"📦 Total Chunks    : {len(chunks)}")
print(Fore.YELLOW + f"⏱ Execution Time  : {execution_time:.2f} seconds")

print(Fore.CYAN + "=" * 60)