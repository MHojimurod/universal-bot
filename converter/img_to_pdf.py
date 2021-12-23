from PIL import Image

def image_pdf(images):
    all = []
    im1 = Image.open(images[0]).convert("RGB") 
    images = images[1::]
    for i in range(len(images)):
        
        image = Image.open(images[i])
        im = image.convert('RGB')
        all.append(im)
    im1.save("all.pdf",save_all=True, append_images=all)
    return  open("all.pdf","rb")



def word_pdf(word):
    from docx2pdf import convert
   
    convert(word, word[0:-4]+"pdf")
    return open(word[0:-4]+"pdf","rb")

def pdf_word(pdf_file):
    from pdf2docx import parse
    
    parse(pdf_file, pdf_file[0:-4]+".docx", start=0, end=None)
    return open(pdf_file[0:-4]+".docx")