from pathlib import Path

nums = [x*x for x in range(5)]
# List comprehension:
print(nums)  #[0, 1, 4, 9, 16]

nums = (x*x for x in range(5)) # <generator object <genexpr> at 0x000001C5D701D8A0>

# print(nums)

#  AI Example

# Suppose you have 10 lakh documents.

# Bad:

# documents = [process(doc) for doc in huge_dataset]

# Loads everything into memory.

# Better:  correct 

# documents = (process(doc) for doc in huge_dataset)

# Processes one document at a time.

# Very common in RAG systems.

# for i in nums:
#     print(i)

currentDir = Path(__file__).parent
file_path = currentDir / "uday.txt"

def readFile(filePath):
    with open(filePath , "r") as file:
        for line in file:
            yield line.strip()

for skill in readFile(file_path):
    print(skill)




# from pathlib import Path

# def load_documents(folder):
#     for file in Path(folder).iterdir():

#         if file.suffix in [".txt", ".md", ".py"]:

#             with open(file, "r", encoding="utf-8") as f:
#                 yield {
#                     "file_name": file.name,
#                     "content": f.read()
#                 }

# for doc in load_documents("."):
#     print(doc["file_name"])
#     print(doc["content"])


# from pathlib import Path

folder = Path(".")

for file in folder.iterdir():
    if file.is_file():
        print(file.name)    