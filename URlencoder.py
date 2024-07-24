import urllib.parse

def url_encoder(url):
    return urllib.parse.quote(url)
def url_decoder(encoded_url):
    return urllib.parse.unquote(encoded_url)

url= "https://www.google.com/search?q=url+encoder+tool+github&sca_esv=6dff3b47ea39d1e5&sca_upv=1&sxsrf=ADLYWILAWGUnFhZgJIhh3dc1yzXTxM8iHw%3A1721750334382&ei=PtOfZpH_Fs2Q4-EPvN3ikQ0&ved=0ahUKEwiRlsrow72HAxVNyDgGHbyuONIQ4dUDCA8&uact=5&oq=url+encoder+tool+github&gs_lp=Egxnd3Mtd2l6LXNlcnAiF3VybCBlbmNvZGVyIHRvb2wgZ2l0aHViMgoQIRigARjDBBgKSKwIULQDWLAHcAF4AJABAJgBlgGgAYoFqgEDMC41uAEDyAEA-AEBmAIDoAKSAsICChAAGLADGNYEGEfCAgcQIxiwAhgnwgIIEAAYgAQYogSYAwCIBgGQBgWSBwMxLjKgB6IS&sclient=gws-wiz-serp"
encoded_url= url_encoder(url)
decoded_url=url_decoder(encoded_url)
print("Original url:",url ,end="\n \n")
print("Encoded Url:",encoded_url,end="\n \n")
print("Decoded Url:",decoded_url,end="\n \n")
