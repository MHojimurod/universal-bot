from PIL import Image
from _pyio import TextIOWrapper


class Pdf:
    def image_pdf(images: list[str]) -> TextIOWrapper:
        all = []
        im1 = Image.open(images[0]).convert("RGB")
        images = images[1::]
        for i in range(len(images)):
            image = Image.open(images[i])
            im = image.convert('RGB')
            all.append(im)
        im1.save(im1[0:-4] + ".pdf", save_all=True, append_images=all)
        return open(im1[0:-4] + ".pdf", "rb")

    def pdf_img(pdf):
        from zipfile import ZipFile
        from pdf2image import convert_from_path
        import os
        images = convert_from_path(pdf, poppler_path="converter\\\pop\\bin")
        a = 0
        zipObj = ZipFile('sample.zip', 'w')
        for i in images:
            name = "{pdf}_{a}.png".format(pdf=pdf.split("/")[-1].split(".")[0], a=str(a))
            i.save(f"converter/pdf_img/{name}", "PNG")
            zipObj.write(f"converter/pdf_img/{name}")
            os.remove(f"converter/pdf_img/{name}")

            a += 1
        zipObj.close()

    # pdf_img("converter/all.pdf")

    def word_pdf(word):
        from docx2pdf import convert
        convert(word, word[0:-4] + "pdf")
        return open(word[0:-4] + "pdf", "rb")

    def pdf_word(pdf):
        from pdf2docx import parse

        parse(pdf, pdf[0:-4] + ".docx", start=0, end=None)
        return open(pdf[0:-4] + ".docx")



