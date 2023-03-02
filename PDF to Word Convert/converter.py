import win32com.client
import os

word = win32com.client.Dispatch("word.application")
word.visible = 0

doc_pdf = "Website.pdf" #PDF FIle Name
input_file =os.path.abspath(doc_pdf)

wb = word.Documents.Open(input_file)
output_file = os.path.abspath(doc_pdf[0:-4] + "docx".format()) #Word File Name to be given
wb.SaveAs2(output_file,FileFormat = 16)
print("Pdf to Word Document is completed")
wb.Close()

word.Quit