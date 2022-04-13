extension_lookup = {
    "Microsoft Office" : ["docx", "doc", "ppt", "pptx", "xls", "xlsx", "csv"],
    "Notepad" : ["txt"],
    "Python IDLE" : ["py"],
    "Visual Studio" : ["c", "h", "cpp", "hpp"]
}

file_path = input("Enter the file path : ")
path_sep = "\\" # Assume \ as path separator
fw_slash_count = file_path.count("/")
bk_slash_count = file_path.count("\\")
if fw_slash_count != 0 and bk_slash_count != 0:
    print("Mixed path entered! Please use one format!")
    exit()
elif fw_slash_count != 0:
    path_sep = "/"
else:
    path_sep = "\\"

path_split = file_path.split(path_sep)
file_name_with_ext = path_split[-1]

file_name_split = file_name_with_ext.split(".")
try:
    file_name, extension = file_name_split[0], file_name_split[1]
except:
    exit()

print(f"Detected file extension as {extension}")

for app in extension_lookup:
    handled_extensions = extension_lookup[app]
    for handled_extension in handled_extensions:
        if extension == handled_extension:
            print(f"File {file_name_with_ext} can be opened with {app}")
            exit()