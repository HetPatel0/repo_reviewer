def extract_code(files) :
    code_files =[]
    for file in files :
        try :
            content = file.decoded_content.decode("utf-8")

            code_files.append({
                "name" : file.name,
                "path" : file.path,
                "content" :content
            })
        except Exception :
            pass
    return code_files